import sqlite3

def search_inv(search_text):
    conn_inverted = sqlite3.connect('inverted.db')
    cur_inverted = conn_inverted.cursor()

    # Cautăm n-gramul sub forma sa de șir
    cur_inverted.execute('''SELECT Ids FROM InvertedIndex WHERE Ngrams=?''', (search_text,))
    row = cur_inverted.fetchone()
    if row:
        # Daca am gasit n-gramul în baza de date, adaugam documentele gasite în rezultate
        results = row[0].split(', ')
    else:
        results = []

    conn_inverted.close()

    return results

# Citirea inputului de la tastatură și interpretarea sa ca o listă de cuvinte
search_text = input("Introduceți n-gramele sub forma ['a', 'b', 'c', 'd', 'e'] de listă de cuvinte separate prin virgulă și spațiu: ")

# Cautarea în baza de date
search_results = search_inv(search_text)

# Scrierea rezultatelor într-un fișier text folosind codec-ul utf-8
with open("result_inverted.txt", "w", encoding="utf-8") as file:
    if search_results:
        file.write("Rezultatele căutării:\n")
        for result in search_results:
            file.write("Document: {}\n".format(result))
    else:
        file.write("Niciun rezultat găsit pentru n-gramele introduse.")
