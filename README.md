# Praktikum4
Tugas Pemrograman Dasar Pertemuan Ke 9 <br>

NAMA    : Andi Ramli Hidayat <br>
NIM     : 312510385 <br>
KELAS   : TI.25 C.5

# Latihan 1
<ul>
  <li>Flowchart</li>
  <img src="https://github.com/aramli/labpy04/raw/main/img/11.png" width="400"/>
  <li>Program</li>
  <img src="https://github.com/aramli/labpy04/raw/main/img/8.png" width="400"/>
  <li>Hasil Program</li>
  <img src="https://github.com/aramli/labpy04/raw/main/img/9.png" width="400"/><br>
  <img src="https://github.com/aramli/labpy04/raw/main/img/10.png" width="400"/>
  
  <li>Penjelasan Kode</li>
  <img src="https://github.com/aramli/labpy04/raw/main/img/1.png" width="700"/><br>
  1. Pertama-tama, program membuat sebuah list kosong bernama data_mahasiswa. List ini akan digunakan untuk menyimpan semua data mahasiswa yang dimasukkan selama program berjalan. Setiap data mahasiswa nantinya akan disimpan dalam bentuk dictionary, lalu dimasukkan ke dalam list ini.
<br><br>
 <img src="https://github.com/aramli/labpy04/raw/main/img/2.png" width="700"/><br>
  2. Selanjutnya, program masuk ke dalam perulangan while True, yang artinya akan terus berjalan tanpa batas sampai pengguna memutuskan untuk berhenti. Di dalam perulangan ini, pengguna diminta untuk mengisi beberapa informasi penting, yaitu nama mahasiswa, NIM, serta nilai tugas, UTS, dan UAS. Semua input ini diambil dari pengguna menggunakan fungsi input(), dan untuk nilai-nilai numerik seperti tugas, UTS, dan UAS, input tersebut langsung dikonversi menjadi tipe data float agar bisa dihitung.
<br><br>
<img src="https://github.com/aramli/labpy04/raw/main/img/3.png" width="700"/><br>
  3. Setelah semua nilai dimasukkan, program langsung menghitung nilai akhir mahasiswa. Rumus yang digunakan adalah kombinasi dari tiga komponen: 30% dari nilai tugas, 35% dari nilai UTS, dan 35% dari nilai UAS. Hasil dari perhitungan ini disimpan dalam variabel nilai_akhir.
<br><br>
<img src="https://github.com/aramli/labpy04/raw/main/img/4.png" width="700"/><br>
  4. Setelah nilai akhir dihitung, semua data mahasiswa—termasuk nama, NIM, nilai tugas, UTS, UAS, dan nilai akhirnya—dibungkus dalam sebuah dictionary. Dictionary ini kemudian ditambahkan ke dalam list data_mahasiswa menggunakan metode .append(). Dengan begitu, setiap kali pengguna memasukkan data baru, data tersebut akan tersimpan dalam list utama.
<br><br>
  <img src="https://github.com/aramli/labpy04/raw/main/img/5.png" width="700"/><br>
  5. Setelah satu data selesai dimasukkan, program akan menanyakan kepada pengguna apakah ingin menambahkan data lagi. Pertanyaan ini ditangani dengan input("Tambah data lagi? (y/t): "). Jika pengguna menjawab dengan huruf "t", maka perulangan akan dihentikan menggunakan break, dan program akan lanjut ke tahap berikutnya.
<br><br>
  <img src="https://github.com/aramli/labpy04/raw/main/img/6.png" width="700"/><br>
  6. Setelah keluar dari perulangan, program mencetak judul dan header tabel untuk menampilkan semua data mahasiswa. Baris-baris ini menggunakan karakter = untuk membuat garis pemisah, dan print() dengan format tertentu untuk memastikan setiap kolom memiliki lebar yang konsisten dan mudah dibaca.
<br><br>
  <img src="https://github.com/aramli/labpy04/raw/main/img/7.png" width="700"/><br>
  7. Program kemudian menggunakan perulangan for untuk menampilkan setiap data mahasiswa yang telah disimpan dalam list. Setiap elemen dalam list adalah sebuah dictionary, sehingga program mengambil nilai-nilai seperti nama, NIM, dan nilai-nilai lainnya dari dictionary tersebut. Format string digunakan untuk mengatur tata letak kolom agar rapi—misalnya, nama diratakan ke kiri, NIM diratakan ke tengah, dan nilai-nilai ditampilkan dengan satu angka di belakang koma.
<br><br>
</ul>
