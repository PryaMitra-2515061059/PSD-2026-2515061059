Tugas Akhir Percobaan 2 : Sorting

Judul Proyek : Sistem Pengurutan Ranking Peserta Lomba

Program ini dibuat untuk mengelola dan mengurutkan data peserta berdasarkan nilai atau skor yang dimiliki. Dalam banyak situasi, seperti penilaian lomba, ujian, atau seleksi, diperlukan suatu sistem sederhana yang mampu menyusun peringkat secara otomatis agar hasilnya lebih cepat, akurat, dan mudah dipahami. Oleh karena itu, program ini memanfaatkan konsep dasar struktur data berupa array (list) serta algoritma pengurutan untuk membantu menyelesaikan permasalahan tersebut secara efisien.

Pada implementasinya, program menggunakan algoritma Bubble Sort untuk mengurutkan data peserta secara descending (dari nilai tertinggi ke terendah). Selain itu, program juga dilengkapi dengan validasi input untuk memastikan data yang dimasukkan sesuai dengan yang diharapkan, sehingga meminimalisir kesalahan saat proses berjalan. Dengan adanya program ini, pengguna dapat dengan mudah memasukkan data peserta, memprosesnya, dan langsung mendapatkan hasil peringkat yang terstruktur dan rapi.

Source Code :

<img width="710" height="1388" alt="code" src="https://github.com/user-attachments/assets/2f5d0dfd-341f-48eb-80ee-10dcc7167391" />

1. Mendefinisikan fungsi tukar dengan parameter array arr serta indeks i dan j untuk menukar posisi data.

2. Membuat variabel sementara temp untuk menyimpan nilai arr[i].

3. Mengisi arr[i] dengan nilai dari arr[j].

4. Mengisi arr[j] dengan nilai dari temp (nilai awal arr[i]).

5. (baris kosong)

6. Mendefinisikan fungsi bubble_sort dengan parameter data.

7. Menyimpan panjang data ke dalam variabel n.

8. Melakukan perulangan sebanyak n kali.

9. Inisialisasi variabel swapped sebagai False untuk mengecek apakah terjadi pertukaran.

10. Perulangan untuk membandingkan elemen dari indeks 0 sampai n-i-1.

11. Mengecek apakah skor saat ini lebih kecil dari skor berikutnya (untuk sorting descending).

12. Memanggil fungsi tukar untuk menukar posisi data.

13. Mengubah swapped menjadi True karena terjadi pertukaran.

14. Jika tidak ada pertukaran sama sekali dalam satu iterasi.

15. Maka perulangan dihentikan lebih awal (optimasi).

16. (baris kosong)

17. Mendefinisikan fungsi main sebagai fungsi utama program.

18. Mencoba mengambil input jumlah peserta dari user.

19. Mengubah input menjadi integer dan menyimpannya ke variabel n.

20. Jika terjadi kesalahan input (bukan angka).

21. Menampilkan pesan error "Input tidak valid!".

22. Menghentikan fungsi dengan return.

23. (baris kosong)

24. Membuat list kosong data untuk menyimpan peserta.

25. Menampilkan pesan untuk memasukkan nama dan skor peserta.

26. Perulangan sebanyak jumlah peserta.

27. Mengambil input nama peserta ke-(i+1).

28. Perulangan tak hingga untuk validasi input skor.

29. Mencoba mengambil input skor dan mengubahnya ke integer.

30. Memasukan Skor ke Peserta

31. Menambahkan tuple (nama, skor) ke dalam list data.

32. Menghentikan loop jika input valid.

33. Jika terjadi error (input bukan angka).

34. Menampilkan pesan bahwa skor harus berupa angka.

35. (baris kosong)

36. Memanggil fungsi bubble_sort untuk mengurutkan data.

37. Menampilkan teks "Ranking peserta:".

38. Perulangan untuk menampilkan hasil ranking.

39. Menampilkan peringkat, nama peserta, dan skor.

40. (baris kosong)

41. Mengecek apakah file dijalankan sebagai program utama. Jika iya, maka fungsi main akan dijalankan.

Output :

<img width="268" height="214" alt="Screenshot 2026-05-05 170054" src="https://github.com/user-attachments/assets/44271af2-df91-4a85-b232-d8c8c36f1c27" />

Memasukan Jumlah Peserta dan Memberi nama serta skor ke Peserta sesuai dengan jumlah yang sudah di inputkan

<img width="187" height="110" alt="Screenshot 2026-05-05 170103" src="https://github.com/user-attachments/assets/ea7baefe-705a-45ef-8937-ac9c3d06b2ed" />

Hasil Setelah dilakukannya sorting

Link : https://youtu.be/4OFwLVwHpLg
