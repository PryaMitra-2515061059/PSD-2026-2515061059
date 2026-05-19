Tugas Akhir Percobaan 4 : Stack dan Queue

Judul Proyek : Membuat Save File Pada Game Mitz Adventure

Program ini merupakan implementasi struktur data stack pada sistem save game sederhana bernama “Mitz Adventure”. Stack digunakan untuk menyimpan data save file dengan konsep LIFO (Last In First Out), yaitu data terakhir yang disimpan akan menjadi data pertama yang dihapus atau ditampilkan kembali. Program ini memungkinkan pengguna untuk menyimpan save game baru, menghapus save terakhir, melihat save terbaru, dan menampilkan seluruh data save yang tersimpan di dalam stack.

Pada program ini terdapat beberapa fungsi utama seperti save_game() untuk menambahkan save file, delete_save() untuk menghapus save terakhir, latest_save() untuk melihat save terbaru, dan show_saves() untuk menampilkan seluruh data save game. Program dijalankan menggunakan menu interaktif berbasis terminal sehingga pengguna dapat memilih fitur yang tersedia dengan mudah. Implementasi ini menggambarkan bagaimana stack digunakan pada sistem penyimpanan data di dunia nyata, khususnya pada fitur save game dalam sebuah permainan.

Source Code :
<img width="1118" height="2476" alt="code" src="https://github.com/user-attachments/assets/f8328175-6684-49c6-a135-f06f708f62a7" />

1.	Membuat class GameSave untuk sistem save game. 
2.	Membuat nilai awal pada program. 
3.	Menyimpan jumlah maksimal save file. 
4.	Membuat list kosong untuk menyimpan data save game. 
5.	Mengatur posisi awal stack menjadi kosong dengan nilai -1. 
6.	(kosong) 
7.	Membuat fungsi untuk mengecek apakah stack penuh. 
8.	Mengecek apakah posisi top sudah mencapai batas maksimal. 
9.	(kosong) 
10.	Membuat fungsi untuk mengecek apakah stack kosong. 
11.	Mengecek apakah nilai top sama dengan -1. 
12.	(kosong) 
13.	Membuat fungsi untuk menyimpan save game baru. 
14.	Mengecek apakah save slot sudah penuh. 
15.	Menampilkan pesan jika save slot penuh. 
16.	Menghentikan proses penyimpanan. 
17.	Menambahkan posisi top satu langkah ke atas. 
18.	Menyimpan nama save file ke dalam stack. 
19.	Menampilkan pesan bahwa save game berhasil disimpan. 
20.	(kosong) 
21.	Membuat fungsi untuk menghapus save file terakhir. 
22.	Mengecek apakah stack kosong. 
23.	Menampilkan pesan jika save file tidak ditemukan. 
24.	Menghentikan proses penghapusan. 
25.	Menampilkan pesan bahwa save file berhasil dihapus. 
26.	Mengurangi posisi top untuk menghapus data terakhir. 
27.	(kosong) 
28.	Membuat fungsi untuk melihat save file terakhir. 
29.	Mengecek apakah stack kosong. 
30.	Menampilkan pesan jika belum ada save file. 
31.	Menghentikan proses. 
32.	Menampilkan save file terakhir yang tersimpan. 
33.	(kosong) 
34.	Membuat fungsi untuk menampilkan semua save game. 
35.	Mengecek apakah data save kosong. 
36.	Menampilkan pesan jika tidak ada save game. 
37.	Menghentikan proses. 
38.	Menampilkan judul daftar save game. 
39.	Melakukan perulangan untuk menampilkan seluruh save game dari terakhir ke awal. 
40.	Menampilkan seluruh data save game. 
41.	(kosong) 
42.	Membuat fungsi utama program. 
43.	Membuat object game dari class GameSave. 
44.	Menjalankan menu program secara berulang. 
45.	Menampilkan judul menu program. 
46.	Menampilkan menu save game. 
47.	Menampilkan menu hapus save terakhir. 
48.	Menampilkan menu melihat save terakhir. 
49.	Menampilkan menu menampilkan semua save game. 
50.	Menampilkan menu keluar program. 
51.	Menerima input pilihan menu dari user. 
52.	Mengecek apakah user memilih menu save game. 
53.	Menerima input nama save file dari user. 
54.	Menjalankan fungsi untuk menyimpan save game. 
55.	Mengecek apakah user memilih menu hapus save terakhir. 
56.	Menjalankan fungsi untuk menghapus save terakhir. 
57.	Mengecek apakah user memilih menu melihat save terakhir. 
58.	Menjalankan fungsi untuk melihat save terakhir. 
59.	Mengecek apakah user memilih menu tampilkan semua save game. 
60.	Menjalankan fungsi untuk menampilkan semua save game. 
61.	Mengecek apakah user memilih menu keluar program. 
62.	Menampilkan pesan penutup program. 
63.	Menghentikan program menggunakan break. 
64.	Menampilkan pesan jika pilihan menu tidak valid. 
65.	(kosong) 
66.	Mengecek apakah file dijalankan langsung sebagai program utama. 
67.	Menjalankan fungsi main() untuk memulai program.

Output Menu 1 :

<img width="692" height="510" alt="Output 1" src="https://github.com/user-attachments/assets/8872fcdc-2d27-40ef-aba7-a65907c4ee7d" />

Output Menu 2 :

<img width="600" height="155" alt="Output 2" src="https://github.com/user-attachments/assets/df91bfbf-e52f-4483-8fb7-e303190d69aa" />

Output Menu 3 :

<img width="543" height="149" alt="Output 3" src="https://github.com/user-attachments/assets/21c20daa-7746-4333-b2a0-d3d800067fc9" />

Output Menu 4 :

<img width="435" height="223" alt="Output 4" src="https://github.com/user-attachments/assets/9f96dad4-ff00-403a-b471-f01017342392" />

Output Menu 0 :

<img width="254" height="138" alt="Output 0" src="https://github.com/user-attachments/assets/29bfe10a-e3f4-4bd6-a4e1-d04588721c18" />

link : https://youtu.be/QWkD2Rsvj3Q
