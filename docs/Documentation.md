#  Project Instructions 🧪

---

## Table of Contents 📚

1. [Introduction](#introduction)
2. [Exercise 1: Familiarization with Map-Reduce](#exercise-1-familiarization-with-map-reduce-)
3. [Exercise 2: Construction of the Inverted Index](#exercise-2-construction-of-the-inverted-index-)
4. [Exercise 3: Search in the Inverted Index](#exercise-3-search-in-the-inverted-index-)
5. [Exercise 4: Construction of Groups Based on LSH](#exercise-4-construction-of-groups-based-on-lsh-)
6. [Exercise 5: Search Based on LSH](#exercise-5-search-based-on-lsh-)

---

## Introduction 📖

**Advanced Search Techniques**  
In this laboratory, we will use the database `features.db`, created in the previous laboratory, to search for similar elements using the techniques of inverted index and locality-sensitive hashing (LSH).

---

## Exercise 1: Familiarization with Map-Reduce 🔍

### Problem:
Familiarize yourself with the Map-Reduce framework: Study the framework provided in the `dummyMapReduce.py` library and the example for counting words. Modify the given example so that the map method counts the occurrences of each word in the document and calls the emit() method only once for each word.

### Solution:
This program uses the MapReduce model to count words in a set of documents. The input documents are defined in the `DOCUMENTS` variable, which is a list of tuples, each containing a document name and its content. In the `map()` method, each document is processed, and the words are identified and counted. For each word and its count, a key-value pair is emitted using the `emit()` method. After processing, the result is written to a text file using the `write_to_file()` method. The resulting file, `word_count_result.txt`, contains each word found in the input documents along with its total occurrences.

### Result:
The output will be a file containing the word counts for each document.

---

## Exercise 2: Construction of the Inverted Index 🔄

### Problem:
Using the previous framework, build the `inverted.db` database that contains the inverted index for the given collection.

### Solution:
The Python script will create or update the `InvertedIndex` table in the `inverted.db` database with n-grams and associated identifiers (assign+student) extracted from the `Homeworks` table in the `features.db` database. The script will avoid creating duplicate entries for already existing n-grams in the `InvertedIndex` table. If an entry already exists for a specific n-gram, the script will update the list of document identifiers associated with that n-gram.

### Result:
The `inverted.db` database will contain entries showing which documents contain each n-gram.

---

## Exercise 3: Search in the Inverted Index 🔍

### Problem:
Implement the `search_inv()` function to search for similar elements using the inverted index.

### Solution:
The Python code performs a search in an SQLite database for the n-grams specified by the user and writes the results to a text file. Specifically, a function `search_inv(search_text)` is defined, which receives a text representing the searched n-grams and searches for these n-grams in the SQLite database. The user inputs the n-grams via the keyboard (in the form of `["jmp", "movabs", "sub", "add", "or"]`). The n-grams are searched in the database using the `search_inv` function, and the results are written to a file named `result_inverted.txt`, using the UTF-8 codec to handle Unicode characters correctly. If no results are found for the entered n-grams, a corresponding message is written in the file.

### Result:
The output will show the documents containing the searched n-grams.

---

## Exercise 4: Construction of Groups Based on LSH 🏷️

### Problem:
Create the `lsh.db` database, which contains a table with the same number of rows as `features.db`, and one column for each hash band (you can use the constants `b = 30` and `r = 5`).

### Solution:
1. **Generating Coefficients for Hash Functions**: Random coefficients are generated for the hash functions in a file called `hash_coefficients.txt`. These coefficients are used to calculate the minimum hash functions in LSH.
2. **Custom Hash Function**: This function takes a string and returns an integer that represents the SHA-256 hash of the string, converted to a hexadecimal format and then into an integer.
3. **Minhash Function**: This calculates the minimum hash values for a given input for each band and row in the band using the previously generated hash coefficients.
4. **Compute Bands Function**: This function calculates the bands for the given content.
5. **Connecting and Creating the Database**: The program connects to an SQLite database and creates a table called `lsh_table` to store the minimum hash values calculated for each object.
6. **Processing Each Row from `features.db`**: Each row from the `features.db` database, containing homework assignments, is processed, and for each, the minimum hash values are calculated and inserted into `lsh_table`.

This code performs a data preprocessing step to find approximate duplicates using Locality Sensitive Hashing and stores the results in a separate database.

### Result:
The table will contain as many entries as there are files. Each band will have 946 entries.

---

## Exercise 5: Search Based on LSH 🔍

### Problem:
Using the previous database, search for similar elements for a given element by implementing the `search_lsh()` function. Compare the results with those obtained using the inverted index.

### Solution:
The coefficients `A` and `B` are saved in `hash_coefficients.txt` and are used for the `search_lsh()` function:
1. **Setting Parameters and Hash Functions**: The necessary parameters for the hash functions and the coefficients `A` and `B` are defined. Functions for parsing input content, calculating custom hash values, calculating MinHash signatures, and creating groups based on LSH signatures are also defined.
2. **`get_content()` Function**: This function is used to obtain the content (MinHash bands) for a specific homework and student from the `features.db` database.
3. **`create_groups()` Function**: This function groups documents that have the same signatures into the same bands.
4. **`jaccard_similarity()` Function**: This calculates the Jaccard similarity between two sets.
5. **`search_lsh()` Function**: This function is used to search for similar files for a specific homework and student using the MinHash signatures and LSH. It identifies candidates for similarity comparison by grouping LSH signatures and then calculates the Jaccard similarity between the given file's content and the found candidates.
6. **`get_lsh()` Function**: This retrieves the LSH signatures stored in the `lsh.db` database.
7. **`print_minhash_signatures()` Function**: Displays the MinHash signatures of the documents stored in the `lsh.db` database.

This application can be used to find similar documents in a database using hashing techniques and Jaccard similarity. The user can input a homework and student, and the program will find similar documents.

### Result:
The cases of similarity with a score of 1 are handled. It is observed that for the Inverted Index, there may be more cases of similarity, while LSH may miss some similarities. LSH can be too restrictive:
- **Inverted Index**: More cases of similarity.
- **LSH**: Fewer cases of similarity.

---

### Test Results 📊
- **Inverted Index**: Displays more similar cases between documents.
- **LSH**: Might miss some similarities, as it's more restrictive.
