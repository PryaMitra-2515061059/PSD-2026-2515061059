def menu():
    print("\nSISTEM DATA NILAI SISWA")
    print("1. Tampilkan Semua Nilai")
    print("2. Input/Update Nilai Siswa")
    print("3. Lihat Rata-rata Per Siswa")
    print("0. Keluar")

def main():
    mata_pelajaran = ["MTK", "B.Indo", "B.Ing", "Agama", "PPKN"]
    jumlah_mapel = len(mata_pelajaran)
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    nilai_siswa = [[0 for _ in range(jumlah_mapel)] for _ in range(jumlah_siswa)]
    
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilih menu : "))
        except ValueError:
            print("Masukkan angka yang ada di menu")
            continue

        if choice == 1:
            print("\nTabel Nilai Siswa")
            width = 10
            header = f"{'Siswa':<{width}}" + "".join([f"{m[:6]:<{width}}" for m in mata_pelajaran])
            print(header)
            print("-" * (width * (len(mata_pelajaran) + 1)))
            for i in range(jumlah_siswa):
                baris_nilai = "".join([f"{str(n):<{width}}" for n in nilai_siswa[i]])
                print(f"{'Siswa ' + str(i+1):<{width}}{baris_nilai}")

        elif choice == 2:
            print("\nInput Nilai")
            for i in range(jumlah_siswa):
                print(f"> Mengisi nilai untuk Siswa {i+1}:")
                for j in range(jumlah_mapel):
                    while True:
                        try:
                            val = int(input(f"  Masukkan nilai {mata_pelajaran[j]}: "))
                            if 0 <= val <= 100:
                                nilai_siswa[i][j] = val
                                break
                            else:
                                print("Nilai harus antara 0 - 100")
                        except ValueError:
                            print("Input error pastikan anda memasukkan angka.")

        elif choice == 3:
            print("\nRata-rata Nilai Siswa")
            for i in range(jumlah_siswa):
                rata_rata = sum(nilai_siswa[i]) / jumlah_mapel
                print(f"Siswa {i+1}: {rata_rata:.2f}")

        elif choice == 0:
            running = False
            print("Program ditutup. See you next time!")
        else:
            print("Pilihan tidak tersedia.")

if __name__ == "__main__":
    main()