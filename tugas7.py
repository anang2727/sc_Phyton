deret = [1,3,2,19,21,100,19,99,85,11,15,17,25]
print("\n1. Akses List Per indeks:")
print(deret[1])
print(deret[5])
print(deret[0])

print("\n2. Meningtegrasi isi list:")
for i in deret:
    print(i, end=" ")

print("\n\3. panjang List = ",len(deret))
print("\4. Banyaknya Angka 19 =",str(deret.count(19)))
print("\n5. Menambah Elemen List dengan Append :")
deret.append(0) #-- Menambah isi list dengan angka 0
deret.append(2) #-- Menambah isi list dengan angka 2
deret.append(4) #-- Menambah isi list dengan angka

deret.append(6) #-- Menambah isi list dengan angka 6
print(deret)
print("\n6. Mencari posisi suatu Nilai dengan Index: ")
print(deret.index(21)) #-- Angka 21 terletek dibaris ke 7
print(deret.index(11)) #-- Angka 11 terletak dibaris ke 12
print(deret.index(1)) #-- Angka 1 terletek dibaris ke 0
print("\n7. menyisipkan suatu nilai ke posisi tertentu: ")
deret.insert(2,101) #-- Menyisipkan angka 101 di baris ke 2 --
deret.insert(0,102) #-- Menyisipkan angka 102 di baris ke 0 --
deret.insert(12,103) #-- Menyisipkan angka 103 di baris ke 12 --
print(deret)
print("\n8. membuang nilai tertentu dengan pop() :")
deret.pop(0) #-- Menghapus elemen list di baris ke 0 --
deret.pop(2) #-- Menghapus elemen list di baris ke 2 --
deret.pop(11) #-- Menghapus elemen list di baris ke 12 --
print(deret)
print("\n9. Membuang nilai tertentu dengan remove(): ")
deret.remove(85) #-- Menghapus nilai 85 di list deret --
deret.remove(3) #-- Menghapus nilai 3 di list deret --
deret.remove(0) #-- Menghapus nilai 0 di list deret --
print(deret)
print("\n10. Menyambung list dengan extend() :")
angka1=[3,5,7,9,11]
deret.extend(angka1)
print(deret)
print("\n11. Membalik urutan list dengan reverse() : ")
deret.reverse()
print(deret)
print("\n 12. Mengurutkan urutan list dari nilai terkecil ke nilai terbesar dengan sort() : ")
deret.sort()
print(deret)
print("\n13. Mencari nilai maksimum dengan max() : ")
print(max(deret))
print("\n14. Mencari nilai minimum dengan min() : ")
print(min(deret))
print("\n15. mencari total nilai dengan sum() :")
print(max(deret))