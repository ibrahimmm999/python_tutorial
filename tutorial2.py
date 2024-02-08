# MATERI PERTEMUAN KEDUA

# LOGICAL OPERATORS
# and, or, dan not

# and : mengembalikan true ketika semua statement benar
# or : mengembalikan true ketika salah satu statement benar
# not : mengembalikan hasil kebalikan dari hasil aslinya

x = True
y = False

if (x or y == True):
    print("x dan y bernilai true")
else:
    print("x dan y bernilai false")

# IDENTITY OPERATORS

# is : mengembalikan true jika kedua variable memiliki objek yang sama (bukan value yang sama)
# is not : kebalikannya

x = ["banana", "apel"]

y = ["banana", "apel"]

y = x
z = x

if (z is y):
    print("SAMA")
else:
    print("BEDA")

# MEMBERSHIP OPERATORS

# in dan not in

x = ["banana", "apel"]
print("bananas" not in x)


# LOOPING

# WHILE
# selama kondisi di parameter while nya bernilai true, maka looping terus berjalan

i = 0

# BREAK : akan menyetop secara paksa loopingnya
while i < 10:
    print(i)
    if i == 8:
        break
    i = i + 1

# CONTINUE : akan menyetop iterasi yang sedang terjadi dan melanjutkan ke iterasi berikutnya
while i < 10:
    if i == 8:
        continue
    print(i)
    i = i + 1
    
# FOR IN 
# selama kondisi variabel looping masih terpenuhi maka loopingnya akan terus berjalan

# dpat digunakan untuk mengulang isi dari list, set, tuple, string, dictionary
    
for x in "banana":
    print(x)

# DI FOR IN JUGA ADA BREAK AND CONTINUE

# function range() : mengembalikan urutan angka, defaultnya mulai dari 0 dan bertambah 1, dan berakhir pada angka tertentu

for x in range(10):
    print(x)

for x in range(2,10):
    print(x)

for x in range(2, 10, 3):
    print(x)

# ELSE STATEMENT IN LOOPING FOR IN : code di dalam else akan dieksekusi ketika loop sudah selesai
# jika ada break statement, maka code di dalam else tidak akan dieksekusi

for x in range(5):
    print(x)
    if x==3:
        break
else:
    print("finished")

# NESTED LOOPS : loop di dalam loop

for i in range(3):
    for j in range(4):
        print(i,"x", end=" ")
    print()

# pass statement : digunakan ketika kita tidak ingin mengeksekusi code apapun dalam suatu kondisi
# for i in range(5):
#     if (i==3):
#         pass
#     print(i)

# STRING : bisa dikatakan sebagai array of substring
# elemen string di python dapat diakses dengan tanda kurung siku diikut index ke berapa, example : [2]
contoh = "Hello, world!"

print(contoh[0])

# len() function : untuk mengakses panjang dari string

print(f'panjang dari variabel contoh = {len(contoh)}')

for x in range(len(contoh)):
    print(x)

# CHECK STRING
# untuk memeriksa apakah ada suatu frasa atau karakter tertentu di dalam sebuah string

print("Hello" in contoh)

# SLICING STRING
# tentukan dulu indeks awal dan panjangnya berapa

print(contoh[2:5]) 
print(contoh[:5]) 
print(contoh[7:]) 
print(contoh[-5:-2]) 

# UPPER CASE

print(contoh.upper())

# LOWER CASE
print(contoh.lower())

# STRIP
# untuk menghilangkan spasi di awal dan akhir
strip = "       Hellow            "
print(strip.strip())

# REPLACE STRING
# mengubah string menjadi string lain

replace_this = "Hello world!"
print(replace_this.replace("o", "P"))

# SPLIT STRING
# membagi string menjadi substring jika menemukan suatu pemisah yang sudah ditentukan
x = "Hello world! halooooo"
print(x.split(" "))

x = "halo"
y = "world"
z = x + y
print(z)

