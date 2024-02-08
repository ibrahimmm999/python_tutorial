# MATERI PERTEMUAN PERTAMA

# 1. PRINT -> MENAMPILKAN SESUATU DI TERMINAL
print("Hello World")
print("Hello World", end="!")
print()


# 2. VARIABLES -> UNTUK MENYIMPAN SEBUAH VALUE / DATA
# Pada implementasi di dunia nyata, penamaan variabel sebaiknya memiliki makna yang jelas 

# pemberian nama variable di python memiliki aturan yang diberi nama SNAKE CASE
# aturan ini menggunakan garis bawah (underscore) sebagai pemisah antar kata dan setiap katanya diawali huruf kecil

# contoh : guest_name, new_location, first_name

nilai = 34
nama, umur, kota = "John", 19, "Jakarta"
x = y = z = "x, y, dan z akan memiliki nilai yang sama"
print(nama, umur, kota)
print(x + "\n"+ y+ "\n"+ z)

# Bentuk Print yang Sering Dipakai :
print(f'Nilai {nama} adalah {nilai}') # BENTUK PRINT DENGAN FORMAT
##################################################################


# 3. INPUT -> MEMINTA INPUT USER DARI TERMINAL
input_nama = input("Masukkan nama : ")
print("Halo", input_nama)


# 4. KOMENTAR -> MEMBERI CATATAN ATAU MENULISKAN SESUATU TANPA DIEKSEKUSI PROGRAM

"""
yang berada di antara 3 tanda petik ini juga komentar
multiline comments
*) Komentar tidak akan dieksekusi oleh komputer
"""


# 5. TIPE DATA
'''
Jenis tipe data di python : 
1. Text Type:	str
2. Numeric Types:	int, float, complex
3. Sequence Types:	list, tuple, range
4. Mapping Type:	dict
5. Set Types:	set, frozenset
6. Boolean Type:	bool
7. Binary Types:	bytes, bytearray, memoryview
8. None Type:	NoneType

Yang akan dipelajari : str (string), int (integer/bilangan bulat), float (decimal), list, tuple, dict (dictionary), set, bool (boolean)

'''
# string
string = "ini adalah string"
spesific_string = str("Hello World")
multiline_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# integer
bilangan_bulat = 9
spesific_int = int(20)

# float
bilangan_decimal = 9.5343
spesific_float = float(43.5)

# list
list_name = ["Andi", "Budi", "Joko", "Heri"]
spesific_list = list(("Andi", "Budi", "Joko", "Heri"))

# tuple
fruits = ("apple", "banana", "cherry")
spesific_tuple = tuple(("apple", "banana", "cherry"))

# dict
user = {"name" : "John", "age": 32, "city": "New York"}
spesific_dict = dict(name="John", age=36)

# set
fruits = {"apple", "banana", "cherry"}
spesific_set = set(("apple", "banana", "cherry"))

# bool
# 0, "", (), [], {}, None = false
# selain diatas = true
isPassword = True
spesific_bool = bool(4)


# 6. COMPARE VALUES (hasil compare berinilai boolean)

"""
Operator    |   Name                    |   Example
            |                           |   
==          |   Sama dengan             |   x == y
!=          |   Tidak sama dengan       |   x != y
>           |   Lebih besar             |   x > y
<           |   Lebih kecil             |   x < y
>=          |   Lebih besar sama dengan |   x >= y
<=          |   Lebih kecil sama dengan |   x <= y
            |                           |
"""         

print("Hasil compare 10 > 9 adalah", 10 > 9)
print("Hasil compare 10 == 9 adalah", 10 == 9 )
print("Hasil compare 10 < 9 adalah", 10 < 9 )
print("Hasil compare 10 <= 9 adalah", 10 <= 11 )
print("Hasil compare 10 <= 9 adalah", 10 >= 10 )

# 7. ARITHMETIC OPERATORS

'''

+ -> tambah
- -> kurang
* -> kali
/ -> bagi
** -> pangkat
% -> modulus (sisa bagi)
// -> pembagian ke bawah

'''

# 8. CONDITIONAL (IF ELSE)

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")