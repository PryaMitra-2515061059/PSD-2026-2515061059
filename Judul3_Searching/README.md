Tugas Akhir Percobaan 3 : Searching

Judul Proyek : Mencari data Produk Di Toko Mitz Store

Program ini digunakan untuk mencari data produk pada sebuah toko atau gudang menggunakan metode Binary Search. Data produk disimpan dalam bentuk list yang sudah terurut berdasarkan kode produk, sehingga proses pencarian dapat dilakukan lebih cepat dibandingkan pencarian biasa. Pengguna dapat memasukkan kode produk yang ingin dicari, lalu program akan menampilkan informasi produk seperti nama barang dan jumlah stok jika data ditemukan.

Selain itu, program ini juga menampilkan daftar produk yang tersedia sebelum proses pencarian dilakukan. Metode Binary Search bekerja dengan cara membagi data menjadi dua bagian dan memeriksa posisi tengah hingga data ditemukan atau tidak ada lagi data yang dapat dicari. Program seperti ini banyak digunakan pada sistem inventaris toko, manajemen gudang, kasir, maupun aplikasi pencarian data karena efisien untuk menangani data dalam jumlah besar.

Source Code :

<img width="1088" height="2006" alt="code" src="https://github.com/user-attachments/assets/a6967b60-421c-488a-9f8a-01ca24d01ed7" />

1. Mendefinisikan fungsi `cari_produk` untuk mencari kode produk menggunakan metode Binary Search.

2. Membuat variabel batas kiri pencarian dimulai dari indeks 0.

3. Membuat variabel batas kanan pencarian berdasarkan jumlah data produk dikurangi 1.

4. 

5. Perulangan berjalan selama batas kiri masih lebih kecil atau sama dengan batas kanan.

6. Menghitung posisi tengah data.

7. Menampilkan kode produk yang sedang diperiksa pada posisi tengah.

8. Mengecek apakah kode produk di posisi tengah sama dengan kode yang dicari.

9. Mengembalikan indeks data jika produk ditemukan.

10. Mengecek apakah kode produk di tengah lebih kecil dari target.

11. Menampilkan bahwa pencarian dilanjutkan ke bagian kanan.

12. Menggeser batas kiri ke kanan dari posisi tengah.

13. Kondisi jika kode produk di tengah lebih besar dari target.

14. Menampilkan bahwa pencarian dilanjutkan ke bagian kiri.

15. Menggeser batas kanan ke kiri dari posisi tengah.

16. Mengembalikan nilai `-1` jika produk tidak ditemukan.

17. 

18. Mendefinisikan fungsi untuk menampilkan daftar produk.

19. Menampilkan judul daftar produk toko.

20. Menampilkan header tabel produk.

21. Menampilkan garis pemisah tabel.

22. 

23. Perulangan untuk membaca setiap data produk.

24. Menampilkan kode produk, nama produk, dan stok.

25. 

26. Mendefinisikan fungsi utama program.

27. Membuat list data produk.

28. Data produk Headset dengan stok 25.

29. Data produk Laptop dengan stok 10.

30. Data produk Monitor dengan stok 8.

31. Data produk Mouse dengan stok 40.

32. Data produk Printer dengan stok 5.

33. Data produk Scanner dengan stok 3.

34. Data produk Speaker dengan stok 15.

35. Penutup list data produk.

36. 

37. Memanggil fungsi untuk menampilkan daftar produk.

38. Mencoba menjalankan input dari pengguna.

39. Meminta pengguna memasukkan kode produk yang ingin dicari.

40. Menangani kesalahan jika input bukan angka.

41. Menampilkan pesan kesalahan input.

42. Menghentikan program jika terjadi kesalahan.

43. Memanggil fungsi pencarian produk.

44. Mengecek apakah produk ditemukan.

45. Menampilkan pesan bahwa produk ditemukan.

46. Menampilkan kode produk.

47. Menampilkan nama produk.

48. Menampilkan jumlah stok produk.

49. Kondisi jika produk tidak ditemukan.

50. Menampilkan pesan bahwa produk tidak ditemukan.

51. 

52. Mengecek apakah file dijalankan langsung.

53. Menjalankan fungsi utama program.

Output Produk Tidak Ditemukan :

<img width="292" height="343" alt="Output Gagal" src="https://github.com/user-attachments/assets/b8a431dc-f4b7-4667-a69b-17bac04fa915" />

Output Produk Ditemukan :

<img width="307" height="379" alt="Output Berhasil" src="https://github.com/user-attachments/assets/672b99d8-28f3-451c-847a-fd7953c9dd1f" />

Link : https://youtu.be/acRzdKvW0PE
