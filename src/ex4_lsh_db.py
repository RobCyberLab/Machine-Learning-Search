import os
import random
import sqlite3
import hashlib
import json

m = 4294967311  # A large prime number for hash function
num_bands = 30  # Number of bands
num_rows = 5  # Number of hash functions in each band

# Check if the coefficients file exists
coefficients_file = "hash_coefficients.txt"
if os.path.isfile(coefficients_file):
    # If the file exists, load the coefficients from it
    with open(coefficients_file, "r") as file:
        coefficients = file.read().splitlines()
    A = list(map(int, coefficients[:num_bands * num_rows]))
    B = list(map(int, coefficients[num_bands * num_rows:]))
else:
    # Generate random coefficients for hash functions
    A = [random.randint(1, m - 1) for _ in range(num_bands * num_rows)]
    B = [random.randint(0, m - 1) for _ in range(num_bands * num_rows)]

    # Save the coefficients to the file
    with open(coefficients_file, "w") as file:
        file.write("A: ")
        file.write(', '.join(map(str, A)) + '\n')
        file.write("B: ")
        file.write(', '.join(map(str, B)) + '\n')

print("A = ", A)
print("B = ", B)

# A = [3040831329, 344181016, 4092874986, 3169193523, 3031011324, 3036397236, 3634937517, 3196691928, 1934998059, 3363435602, 2829400386, 549796285, 1242990032, 3072292935, 1821377327, 2800329451, 2498470140, 416823146, 2299275286, 3904264885, 3447179001, 2797784338, 3433470437, 3786062912, 1340284981, 1281577582, 2450578736, 3887695828, 2090845611, 3261587629, 776741302, 4250154234, 1111481180, 1035483224, 3015885460, 2206492578, 1303950801, 4059193768, 1945000673, 217339847, 1582979032, 3175534119, 3087101015, 593742182, 3231677328, 1689492249, 1191352140, 3821049549, 1584378983, 2041422628, 1937901052, 2709174943, 2673998575, 3040919213, 2946327026, 1725546253, 3271764012, 3268420836, 2682492563, 2209917819, 3914969061, 3084186456, 2979942365, 678833412, 1103480447, 3023846805, 2351165381, 3687536312, 3938758891, 2630943224, 2852097092, 2450752052, 491925145, 757649888, 1094978291, 1822218252, 3712751592, 297974637, 2791601795, 3440661418, 709924059, 76389367, 393092633, 617152226, 2466763712, 1703513991, 590904013, 3911029349, 3075350335, 1277953756, 804075854, 3949913924, 3347291861, 561082633, 2692572965, 1807480413, 4148387977, 1013908906, 923206669, 690288231, 1894710442, 2869255175, 22044298, 1529787159, 3462748917, 2062374238, 3631904284, 838430865, 3417827604, 3918271984, 2720687447, 1388416295, 2006055959, 2229447586, 3183447699, 1210936404, 2479442373, 2167928465, 832791959, 1921377851, 2503059895, 2898774772, 1890973637, 18218043, 316110277, 296352885, 290558976, 748364964, 1687545135, 2831132526, 419146589, 3798181946, 240662364, 3864283291, 1727828447, 2496083427, 1533364645, 1905996227, 3411094388, 1025007339, 1414499656, 2401958671, 129730515, 2651138564, 1679661458, 2729528101, 3289814264, 1308142179, 3164912350, 2210438203]
# B = [1452215062, 2000250784, 3592998542, 136069891, 1598770269, 2821750160, 4050042032, 3935900166, 755924236, 2058543665, 2052952815, 853841261, 1771423390, 1718550357, 51997505, 1758247369, 2435671023, 507912112, 615853987, 3856907959, 247729543, 3955521555, 3401604504, 1912020466, 2831221797, 1457321664, 2405058626, 1660306454, 899739142, 69360885, 3050881920, 3924151985, 1720885297, 1609296936, 3297275090, 1706696685, 1331327052, 3426483625, 2704226660, 1412583117, 1812490769, 671020798, 1004701579, 2704599184, 4117341439, 1811330001, 3437820621, 2480485287, 2573744876, 1823765163, 784562086, 657254549, 2234323347, 3693882454, 605302980, 4207676931, 316932218, 1349526074, 1943613045, 2976184173, 1625085399, 764773913, 2429116919, 1187438140, 2212756308, 3124940913, 4086820664, 4003765513, 180127869, 343263321, 2073721387, 1815158444, 4021334381, 3010027678, 3723858787, 1366985052, 2855424368, 1725522221, 117002281, 3886121554, 3841682617, 2541580749, 680471371, 31798090, 3953753062, 3539986375, 964455759, 3514029158, 2371395001, 983692024, 3226795102, 4045465631, 3355658071, 3709908051, 737869800, 2398604149, 1563769101, 4058816372, 1032178513, 3362636126, 4046862390, 1334399668, 4193469580, 2216329985, 198340919, 2528399364, 3275629192, 1186335793, 3331939163, 1420186096, 2764899943, 74110242, 1603169026, 3922551755, 1980470568, 4107007805, 4045390752, 51107132, 1308887042, 4270316640, 3252078104, 3959224948, 3933108012, 2308680934, 2627738384, 1505079059, 602564248, 129711887, 2275742206, 3409506305, 79404781, 3529312997, 780253766, 657732363, 2559580634, 3872136453, 3231543276, 1663849015, 837649826, 842891213, 3432789107, 2946365959, 3575995690, 312065541, 2733713561, 2175037808, 2947807315, 3620478282, 2362571287, 3702750235]





def custom_hash(input_string):
    input_bytes = input_string.encode('utf-8')
    hash_object = hashlib.sha256(input_bytes)
    hash_hex = hash_object.hexdigest()
    return int(hash_hex, 16)


def minhash(s, band, row):
    a = A[band * num_rows + row]
    b = B[band * num_rows + row]
    perm = [(a * abs(custom_hash(x)) + b) % m for x in s]
    if len(perm) > 0:
        return min(perm)
    else:
        return 0


def compute_bands(content):
    bands = []
    for band in range(num_bands):
        h = []
        for row in range(num_rows):
            h.append(minhash(content, band, row))
        bands.append(h)
    return bands


# Connect to the features.db database
conn_features = sqlite3.connect('features.db')

# Create or connect to the lsh.db database
conn_lsh = sqlite3.connect('lsh.db')

# Create the lsh_table if it doesn't exist already
cursor_lsh = conn_lsh.cursor()
cursor_lsh.execute(f"""
    CREATE TABLE IF NOT EXISTS lsh_table (
        id TEXT PRIMARY KEY,
        {", ".join(f"band{i}" for i in range(1, num_bands + 1))}
    )
""")


def insert_lsh(connection, lsh_row):
    cursor = connection.cursor()
    # Convertim listele din lsh_row în șiruri JSON
    lsh_row_json = [json.dumps(band) for band in lsh_row[1:]]  # Ignorăm primul element (ID-ul)
    cursor.execute('''INSERT INTO lsh_table VALUES (?, {})'''.format(', '.join(['?'] * len(lsh_row_json))), [lsh_row[0]] + lsh_row_json)
    connection.commit()


# Iterate over each row in features.db
for row in conn_features.execute("SELECT * FROM Homeworks"):
    # Construct the ID by concatenating values from the "Assign" and "Student" columns
    homework_id = f"{row[1]}_{row[2]}"

    # Calculate band hashes for each column
    bands = compute_bands(row[3:])

    # Define lsh_row
    lsh_row = [homework_id] + [list(band) for band in bands]

    # Check if the ID already exists in the lsh_table
    cursor_lsh.execute("SELECT COUNT(*) FROM lsh_table WHERE id=?", (homework_id,))
    row_count = cursor_lsh.fetchone()[0]

    if row_count == 0:  # If the ID doesn't already exist, insert the row
        # Insert the row into the lsh_table
        insert_lsh(conn_lsh, lsh_row)
    else:
        # Print a message if the ID already exists in the lsh_table
        print(f"ID '{homework_id}' already exists. Skipping insertion.")

conn_lsh.commit()

# Validate the number of rows
count_features = conn_features.execute("SELECT COUNT(*) FROM Homeworks").fetchone()[0]
count_lsh = cursor_lsh.execute("SELECT COUNT(*) FROM lsh_table").fetchone()[0]

if count_features != count_lsh:
    print("Different number of rows!")
else:
    print("Data processed successfully!")

# Close the database connections
conn_lsh.close()
conn_features.close()
