import sqlite3
import pickle
import hashlib
from scipy.spatial.distance import jaccard
import numpy as np
import mmh3

# Parametri pentru funcția de hash
m = 4294967311  # Un număr prim mare pentru funcția de hash
num_bands = 30  # Numărul de benzi
num_rows = 5    # Numărul de funcții de hash în fiecare bandă
b = num_bands  # Numărul de benzi
r = num_rows   # Numărul de funcții de hash în fiecare bandă

# Valorile date pentru A și B
A =  [3040831329, 344181016, 4092874986, 3169193523, 3031011324, 3036397236, 3634937517, 3196691928, 1934998059, 3363435602, 2829400386, 549796285, 1242990032, 3072292935, 1821377327, 2800329451, 2498470140, 416823146, 2299275286, 3904264885, 3447179001, 2797784338, 3433470437, 3786062912, 1340284981, 1281577582, 2450578736, 3887695828, 2090845611, 3261587629, 776741302, 4250154234, 1111481180, 1035483224, 3015885460, 2206492578, 1303950801, 4059193768, 1945000673, 217339847, 1582979032, 3175534119, 3087101015, 593742182, 3231677328, 1689492249, 1191352140, 3821049549, 1584378983, 2041422628, 1937901052, 2709174943, 2673998575, 3040919213, 2946327026, 1725546253, 3271764012, 3268420836, 2682492563, 2209917819, 3914969061, 3084186456, 2979942365, 678833412, 1103480447, 3023846805, 2351165381, 3687536312, 3938758891, 2630943224, 2852097092, 2450752052, 491925145, 757649888, 1094978291, 1822218252, 3712751592, 297974637, 2791601795, 3440661418, 709924059, 76389367, 393092633, 617152226, 2466763712, 1703513991, 590904013, 3911029349, 3075350335, 1277953756, 804075854, 3949913924, 3347291861, 561082633, 2692572965, 1807480413, 4148387977, 1013908906, 923206669, 690288231, 1894710442, 2869255175, 22044298, 1529787159, 3462748917, 2062374238, 3631904284, 838430865, 3417827604, 3918271984, 2720687447, 1388416295, 2006055959, 2229447586, 3183447699, 1210936404, 2479442373, 2167928465, 832791959, 1921377851, 2503059895, 2898774772, 1890973637, 18218043, 316110277, 296352885, 290558976, 748364964, 1687545135, 2831132526, 419146589, 3798181946, 240662364, 3864283291, 1727828447, 2496083427, 1533364645, 1905996227, 3411094388, 1025007339, 1414499656, 2401958671, 129730515, 2651138564, 1679661458, 2729528101, 3289814264, 1308142179, 3164912350, 2210438203]
B =  [1452215062, 2000250784, 3592998542, 136069891, 1598770269, 2821750160, 4050042032, 3935900166, 755924236, 2058543665, 2052952815, 853841261, 1771423390, 1718550357, 51997505, 1758247369, 2435671023, 507912112, 615853987, 3856907959, 247729543, 3955521555, 3401604504, 1912020466, 2831221797, 1457321664, 2405058626, 1660306454, 899739142, 69360885, 3050881920, 3924151985, 1720885297, 1609296936, 3297275090, 1706696685, 1331327052, 3426483625, 2704226660, 1412583117, 1812490769, 671020798, 1004701579, 2704599184, 4117341439, 1811330001, 3437820621, 2480485287, 2573744876, 1823765163, 784562086, 657254549, 2234323347, 3693882454, 605302980, 4207676931, 316932218, 1349526074, 1943613045, 2976184173, 1625085399, 764773913, 2429116919, 1187438140, 2212756308, 3124940913, 4086820664, 4003765513, 180127869, 343263321, 2073721387, 1815158444, 4021334381, 3010027678, 3723858787, 1366985052, 2855424368, 1725522221, 117002281, 3886121554, 3841682617, 2541580749, 680471371, 31798090, 3953753062, 3539986375, 964455759, 3514029158, 2371395001, 983692024, 3226795102, 4045465631, 3355658071, 3709908051, 737869800, 2398604149, 1563769101, 4058816372, 1032178513, 3362636126, 4046862390, 1334399668, 4193469580, 2216329985, 198340919, 2528399364, 3275629192, 1186335793, 3331939163, 1420186096, 2764899943, 74110242, 1603169026, 3922551755, 1980470568, 4107007805, 4045390752, 51107132, 1308887042, 4270316640, 3252078104, 3959224948, 3933108012, 2308680934, 2627738384, 1505079059, 602564248, 129711887, 2275742206, 3409506305, 79404781, 3529312997, 780253766, 657732363, 2559580634, 3872136453, 3231543276, 1663849015, 837649826, 842891213, 3432789107, 2946365959, 3575995690, 312065541, 2733713561, 2175037808, 2947807315, 3620478282, 2362571287, 3702750235]

# Define functions to parse input content, compute MinHash signatures, and search for similar documents
def parse_input_content(content):
    parsed_content = []
    for sublist in content:
        instruction_str = ''.join(sublist)
        parsed_content.append(instruction_str)
    return parsed_content

# Funcție pentru calculul hash personalizat
def custom_hash(input_string):
    input_bytes = str(input_string).encode('utf-8')
    hash_object = hashlib.sha256(input_bytes)
    hash_hex = hash_object.hexdigest()
    return int(hash_hex, 16)


# Funcție pentru calculul minhash
def minhash(s, band, row):
    a = A[band * num_rows + row]
    b = B[band * num_rows + row]
    perm = [(a * abs(custom_hash(x)) + b) % m for x in s]
    if len(perm) > 0:
        min_hash = min(perm)
    else:
        min_hash = 0
    return min_hash

# Funcție pentru calculul benzilor și semnăturilor MinHash
def compute_bands(content):
    minhash_signatures = []  # Lista pentru a stoca semnăturile MinHash calculate

    for band in range(num_bands):
        h = []
        for row in range(num_rows):
            h.append(minhash(content, band, row))
        minhash_signatures.append(h)  # Adăugăm semnăturile MinHash calculate la lista de semnături

    # Returnăm atât semnăturile MinHash calculate, cât și benzile
    return minhash_signatures


def get_content(assign, student):
    try:
        connection = sqlite3.connect('features.db')
        cursor = connection.cursor()

        cursor.execute('''SELECT * FROM Homeworks WHERE Assign = ? AND Student = ?''', (assign, student))
        row = cursor.fetchone()

        if row is None:
            print("Content not found in the database.")
            connection.close()
            return None
        else:
            bands = row[3:]
            print("Content retrieved from the database:", bands)  # Adăugați această instrucțiune de imprimare pentru a verifica conținutul
            connection.close()
            return bands
    except Exception as e:
        print(f"Error: {e}")
        if connection:
            connection.close()
        return None


# Funcție pentru crearea grupurilor bazate pe semnăturile LSH
def create_groups(lsh_list):
    band_groups = [{} for i in range(b * r)]
    for id, bands in lsh_list:
        for band, H in enumerate(bands):
            # print("Band Groups: ", band_groups)
            # print("LSH List:", lsh_list)

            if H in band_groups[band]:
                band_groups[band][H].add(id)
            else:
                band_groups[band][H] = {id}
    return band_groups

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 0  # Returnăm 0 dacă seturile sunt vide
    return intersection / union

def search_lsh(assign, student, threshold, lsh_list):
    band_groups = create_groups(lsh_list)
    content = get_content(assign, student)
    if content is None:
        return None  # Return None if content is not found
    sorted_content = sorted(content)
    hashes = compute_bands(sorted_content)
    bands = [str(band) for band in hashes]
    elements_to_remove = {assign + "_" + student}
    candidates = set()

    similar_files = 0  # Definim similar_files ca o variabilă locală pentru a număra fișierele similare

    # Iterăm prin band_groups pentru a găsi fișierele candidat
    for band, H in enumerate(bands):
        if H in band_groups[band]:
            for element in band_groups[band][H]:
                assign2, student2 = element.split('_')
                if assign != assign2:
                    elements_to_remove.add(element)
                else:
                    candidates.add(element)
        else:
            print("H not found in band_groups[band].")

    candidates -= elements_to_remove

    print("\nCandidates for similarity comparison:", candidates)

    for file in candidates:
        assign, student = file.split('_')
        doc_content = get_content(assign, student)
        if doc_content is None:
            continue  # Sărim dacă conținutul documentului candidat nu este găsit

        # Printează numele fișierului găsit
        print("Found similar file:", assign, student)

        similarity = jaccard_similarity(set(content), set(doc_content))

        if similarity >= threshold:
            similar_files += 1  # Incrementăm similar_files pentru fiecare fișier similar găsit


def get_lsh():
    connection = sqlite3.connect('lsh.db')
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT * FROM lsh_table''')
        rows = cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
        connection.close()
        return None

    lsh_list = []
    for row in rows:
        lsh_list.append([row[0], row[1:]])

    connection.close()
    return lsh_list

def print_minhash_signatures():
    lsh_list = get_lsh()
    for item in lsh_list:
        print(f"Assignment: {item[0]}, MinHash Signatures: {item[1]}, {item[2]}")

# Funcția principală
def main():
    lsh_list = get_lsh()  # Obținem lista lsh_list o singură dată și o folosim în toate apelurile search_lsh()
    while True:
        print("\n1. Print MinHash Signatures")
        print("2. Search")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print_minhash_signatures()
        elif choice == "2":
            assign = input("Assignment: ")
            student = input("Student: ")
            threshold = 0.7
            similar_files = search_lsh(assign, student, threshold, lsh_list)  # Capturăm valoarea returnată
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()