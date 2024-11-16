import sqlite3
import ast

# Conectare la baza de date features.db
conn_features = sqlite3.connect('features.db')
cur_features = conn_features.cursor()

# Conectare la baza de date inverted.db
conn_inverted = sqlite3.connect('inverted.db')
cur_inverted = conn_inverted.cursor()

# Creare tabelă în baza de date inverted.db pentru indexul inversat (dacă nu există deja)
cur_inverted.execute('''CREATE TABLE IF NOT EXISTS InvertedIndex (
                            Ngrams BLOB PRIMARY KEY,
                            Ids TEXT
                        )''')

# Interogare pentru a obține toate înregistrările din features.db
cur_features.execute('''SELECT * FROM Homeworks''')

# Parcurgere înregistrări din features.db și actualizare index inversat
for row in cur_features.fetchall():
    assign_student = row[1] + '_' + row[2]  # Combinăm assign și student pentru a forma un identificator unic
    ngrams = ast.literal_eval(row[3])  # Convertim n-gramurile din formatul BLOB la listă de liste de cuvinte

    # Parcurgem fiecare n-gram din lista de n-gramuri
    for ngram in ngrams:
        ngram_str = '["' + '", "'.join(ngram) + '"]'  # Construim șirul de caractere pentru n-gram
        # Verificăm dacă n-gramul există deja în indexul inversat
        cur_inverted.execute('''SELECT * FROM InvertedIndex WHERE Ngrams=?''', (ngram_str,))
        existing_entry = cur_inverted.fetchone()

        if existing_entry is None:  # Dacă n-gramul nu există deja, îl adăugăm în tabel
            cur_inverted.execute('''INSERT INTO InvertedIndex (Ngrams, Ids) VALUES (?, ?)''', (ngram_str, assign_student))
        else:  # Dacă n-gramul există deja, actualizăm lista de identificatori de documente
            ids = existing_entry[1].split(', ')
            if assign_student not in ids:
                ids.append(assign_student)
            ids_str = ', '.join(ids)
            cur_inverted.execute('''UPDATE InvertedIndex SET Ids=? WHERE Ngrams=?''', (ids_str, ngram_str))

# Salvăm modificările și închidem conexiunile la bazele de date
conn_inverted.commit()
conn_features.close()
conn_inverted.close()
