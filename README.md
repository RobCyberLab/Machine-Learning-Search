# 🔎Machine Learning Search🔍


In this project, we will use the database `features.db` to search for similar items using the inverted index and locality-sensitive hashing (LSH) techniques.

Note: Due to privacy policies, I am not allowed to post the dataset publicly.

---

## Table of Contents 📋
1. [Familiarization with Map-Reduce](#1-familiarization-with-map-reduce-)
2. [Constructing the Inverted Index](#2-constructing-the-inverted-index-)
3. [Searching the Inverted Index](#3-searching-the-inverted-index-)
4. [Constructing LSH Groups](#4-constructing-lsh-groups-)
5. [Searching with LSH](#5-searching-with-lsh-)
6. [Counting Function Calls](#6-counting-function-calls-)

---

## 1. Familiarization with Map-Reduce 🔄

Study the provided framework and the `dummyMapReduce.py` library, along with the example for counting words. Modify the given example so that the map method counts the occurrences of each word within the document and calls the `emit()` method only once for each word.

---

## 2. Constructing the Inverted Index 🔍

Using the previously built framework, create the `inverted.db` database, which contains the inverted index for the dataset.

---

## 3. Searching the Inverted Index 🔎

Implement the `search_inv()` function, which performs the search for similar items using the inverted index.

---

## 4. Constructing LSH Groups 🧩

Build the `lsh.db` database, which contains a table with the same number of rows as in `features.db`, with one column for each hash band. You can use constants `b=30` and `r=5` for this task.

---

## 5. Searching with LSH 🔑

Using the previous database, search for similar elements to a given item by implementing the `search_lsh()` function. Compare the results with those obtained from the inverted index. **Important**: It is essential to use the same minhash functions as those used when constructing the database.

---

## 6. Counting Function Calls 🧮

Measure how many times the distance calculation function is called on average for both types of searches.

