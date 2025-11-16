#membuat list demgan 5 element bebas
random = [8, 16, 32, 64, 128]

#menampilkan list
print(random)
#menampilkan element ke 3 pada list
print(random[2])
#menampilkan elemet ke 2 hingga element ke 4
print(random[1:4])
#menampilkan element terakhir pada list (pengunaan -1 lebih efektif untuk mencari element terakhir)
print(random[-1])

#mengubah element ke 4 dengan nilai lainnya
random[3] = 100
print(random)

#mengubah element ke 4 sampai dengan element terakhir
random[3:] = [200, 400]
print(random)

#ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
B = random[:2]
print(B)

#tambah list B dengan nilai string
B.append("ramli")
print(B)

#tambah list B dengan 3 nilai
B.extend([555, 666, 777])
print(B)

#gabungkan list B dengan list A
gabungan = B + random
print(gabungan)
