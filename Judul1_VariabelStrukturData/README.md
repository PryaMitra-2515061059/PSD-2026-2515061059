Tugas Akhir Percobaan 1

Judul Proyek : Sistem Data Nilai Siswa

Proyek ini merupakan sebuah sistem yang dirancang untuk mempermudah tenaga pendidik dalam mengelola dan memantau perkembangan akademik siswa secara terorganisir. Sistem ini menggunakan konsep List 2D pada Python, di mana data nilai disusun dalam matriks yang merepresentasikan hubungan antara baris sebagai identitas siswa dan kolom sebagai berbagai mata pelajaran.

Source Code :

<img width="1834" height="2648" alt="code" src="https://github.com/user-attachments/assets/ea585b8b-8228-4ed9-9f06-710167672b89" />

1. Mendefinisikan fungsi bernama menu untuk membungkus kode yang menampilkan daftar pilihan.

2. Mencetak judul sistem ke layar dengan baris baru di awal (\n).

3. Mencetak opsi pertama menu.

4. Mencetak opsi kedua menu.

5. Mencetak opsi ketiga menu.

6. Mencetak opsi nol untuk menghentikan program.

7. 

8. Mendefinisikan fungsi utama program tempat seluruh logika inti berjalan.

9. Membuat list yang berisi nama-nama mata pelajaran sebagai kolom.

10. Menghitung total mata pelajaran (5) dan menyimpannya di variabel jumlah_mapel.

11. Meminta user memasukkan angka untuk menentukan berapa banyak baris (siswa) yang akan masukan.

12. Membuat List 2D (matriks) berisi angka 0 dengan ukuran sesuai jumlah siswa dan mata pelajaran.

13. 

14. Membuat variabel "bendera" untuk menjaga agar perulangan program tetap berjalan.

15. Memulai perulangan utama selama variabel running bernilai True.

16. Memanggil fungsi menu yang sudah didefinisikan di awal untuk tampil ke layar.

17. Memulai blok penanganan error agar program tidak crash jika user salah input.

18. Mengambil input pilihan menu dari user dan mengubahnya menjadi bilangan bulat (integer).

19. Menangkap error jika user memasukkan sesuatu yang bukan angka (misal: huruf).

20. Menampilkan pesan peringatan jika terjadi ValueError.

21. Mengulang perulangan dari awal menu jika terjadi error input.

22. 

23. Mengecek jika user memilih menu nomor 1.

24. Mencetak Tabel Nilai Siswa

25. Menentukan lebar kolom (10 karakter) agar tampilan tabel rapi dan sejajar.

26. Membuat baris judul tabel (Siswa + Nama Mapel) dengan format rata kiri.

27. Mencetak baris judul (header) ke layar.

28. Mencetak garis pembatas yang panjangnya menyesuaikan jumlah kolom.

29. Melakukan perulangan untuk setiap baris (siswa).

30. Mengambil nilai-nilai pelajaran satu siswa, diubah ke string, dan diformat agar rapi sesuai lebar kolom.

31. Mencetak label "Siswa X" diikuti oleh deretan nilainya dalam satu baris.

32. 

33. Mengecek jika user memilih menu nomor 2.

34. Mencetak judul bagian input nilai.

35. Perulangan untuk mengakses setiap siswa satu per satu.

36. Memberi tahu user siswa mana yang sedang diisi nilainya.

37. Perulangan di dalam untuk mengakses setiap mata pelajaran siswa tersebut.

38. Melakukan perulangan tanpa henti sampai user memasukkan nilai yang valid.

39. Mencoba mengambil input nilai.

40. Meminta input nilai untuk mata pelajaran tertentu.

41. Melakukan validasi apakah nilai berada di rentang 0 sampai 100.

42. Jika valid, simpan nilai tersebut ke dalam koordinat List 2D yang tepat.

43. Keluar dari perulangan while True untuk lanjut ke mata pelajaran berikutnya.

44. Jika nilai di luar 0-100.

45. Memberi tahu user bahwa input nilai salah.

46. Menangkap error jika user menginput huruf saat diminta nilai angka.

47. Menampilkan pesan Input error pastikan anda memasukkan angka.

48. 

49. Mengecek jika user memilih menu nomor 3.

50. Mencetak judul bagian rata-rata.

51. Perulangan untuk menghitung rata-rata tiap siswa.

52. Menjumlahkan semua nilai dalam satu baris siswa, lalu dibagi total mata pelajaran.

53. Mencetak hasil rata-rata dengan format 2 angka di belakang koma.

54. 

55. Mengecek jika user memilih menu nomor 0.

56. Mengubah running menjadi False agar perulangan berhenti.

57. Mencetak pesan Program ditutup. See you next time!

58. Jika user memasukkan angka yang tidak ada di menu.

59. Memberi tahu bahwa menu tersebut tidak ada.

60. 

61. Baris standar Python untuk memastikan fungsi main() hanya berjalan jika file ini dieksekusi langsung.

62. Memanggil fungsi utama untuk menjalankan seluruh program.

Output :
Jumlah Siswa dan Menu
<img width="231" height="121" alt="image" src="https://github.com/user-attachments/assets/f7b5a067-3114-44b8-b0ac-ee2fc02037d4" />

Menu 1
Sebelum di inputkan Nilai
<img width="433" height="147" alt="image" src="https://github.com/user-attachments/assets/a0085eea-27a9-4b2d-968d-e08f3c2a7e56" />

Setelah di inputkan Nilai
<img width="439" height="150" alt="image" src="https://github.com/user-attachments/assets/0f3c456f-9f33-4f29-93b7-8b0d9c1523b4" />

Menu 2
<img width="261" height="363" alt="image" src="https://github.com/user-attachments/assets/0eee3ce5-1884-4b4a-bb21-5e06e33d1947" />

Menu 3
<img width="174" height="115" alt="image" src="https://github.com/user-attachments/assets/e48b8569-bc89-4b0a-93cd-91ef2020dbd8" />

Menu 0
<img width="256" height="41" alt="image" src="https://github.com/user-attachments/assets/c3668c7b-8816-469d-b450-413b46c36b50" />

Link : 
