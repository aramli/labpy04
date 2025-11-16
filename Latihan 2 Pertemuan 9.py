data_mahasiswa = []

while True:
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    tugas = float(input("Masukkan nilai Tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = (0.3 * tugas) + (0.35 * uts) + (0.35 * uas)

    data_mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    })

    lanjut = input("Tambah data lagi? (y/t): ").lower()
    if lanjut == "t":
        break

print("\nDaftar Nilai Mahasiswa:")
print("===============================================================================================")
print("No |       Nama      |       NIM      |    Tugas    |     UTS     |     UAS     |    Akhir   ")
print("===============================================================================================")

no = 1
for mhs in data_mahasiswa:
    print(f"{no:2} | {mhs['nama']:<15} | {mhs['nim']:^13}  | {mhs['tugas']:^11.1f} | {mhs['uts']:^11.1f} | {mhs['uas']:^11.1f} | {mhs['nilai_akhir']:9.1f}")
    no+=1
print("===============================================================================================")
