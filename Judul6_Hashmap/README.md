Tugas Akhir Percobaan 6 : Hash Map

Judul Proyek : System Loot Drop Pada Game Mitz Adventure

System Loot Drop pada Game Mitz Adventure merupakan sebuah program yang dibuat untuk mengelola sistem drop item dari setiap monster menggunakan konsep struktur data HashMap. Program ini menyimpan data monster sebagai key dan daftar loot (item drop beserta persentase peluangnya) sebagai value. Dengan menggunakan teknik hashing dan open addressing, data dapat disimpan, dicari, dan dihapus dengan cepat tanpa harus melakukan pencarian satu per satu seperti pada struktur data biasa. Hal ini membuat proses pengambilan data loot menjadi lebih efisien terutama ketika jumlah monster dalam game semakin banyak.

Selain itu, sistem ini juga memiliki fitur lengkap seperti menambahkan loot monster baru, mencari loot berdasarkan nama monster, menampilkan seluruh data loot, hingga menghapus monster dari sistem. Fitur linear probing digunakan untuk mengatasi tabrakan data (collision) saat dua key menghasilkan index yang sama. Dengan adanya sistem ini, pengelolaan item drop dalam game Mitz Adventure menjadi lebih terstruktur, cepat, dan mudah dikembangkan untuk fitur game yang lebih kompleks di masa depan seperti rare drop system atau boss loot system.

Source Code :

<img width="1648" height="5308" alt="code" src="https://github.com/user-attachments/assets/db3a8581-9bc2-4dc2-8cee-1bdde4d92dd2" />

1.	Mendefinisikan class untuk menyimpan status slot hash table. 
2.	Menentukan status slot kosong. 
3.	Menentukan status slot terisi. 
4.	Menentukan status slot terhapus. 
5.	(kosong) 
6.	Mendefinisikan class yang mewakili satu slot data. 
7.	Membuat constructor objek slot. 
8.	Menginisialisasi key menjadi kosong. 
9.	Menginisialisasi value menjadi kosong. 
10.	Mengatur status awal slot sebagai kosong. 
11.	(kosong) 
12.	Mendefinisikan class hash table untuk sistem loot monster. 
13.	Membuat constructor hash table. 
14.	Menyimpan ukuran tabel. 
15.	Membuat kumpulan slot sesuai ukuran tabel. 
16.	(kosong) 
17.	Mendefinisikan fungsi hash. 
18.	Menghasilkan indeks penyimpanan berdasarkan key. 
19.	(kosong) 
20.	Mendefinisikan fungsi insert untuk menambah data. 
21.	Menghitung indeks awal menggunakan hash. 
22.	Menyiapkan variabel penampung posisi slot terhapus. 
23.	(kosong) 
24.	Memulai proses pencarian slot menggunakan linear probing. 
25.	Menghitung posisi slot yang sedang diperiksa. 
26.	Mengecek apakah slot saat ini terisi data. 
27.	Mengecek apakah key yang dicari sudah ada. 
28.	Memperbarui value jika key ditemukan. 
29.	Mengakhiri proses update. 
30.	Mengecek apakah slot berstatus terhapus. 
31.	Memastikan belum ada slot terhapus yang tersimpan sebelumnya. 
32.	Menyimpan posisi slot terhapus pertama. 
33.	Menangani kondisi ketika slot kosong ditemukan. 
34.	Mengecek apakah sebelumnya ditemukan slot terhapus. 
35.	Menggunakan posisi slot terhapus tersebut. 
36.	Menyimpan key baru. 
37.	Menyimpan value baru. 
38.	Mengubah status menjadi terisi. 
39.	Mengakhiri proses insert. 
40.	Mengecek apakah terdapat slot terhapus setelah proses probing selesai. 
41.	Menyimpan key pada slot terhapus. 
42.	Menyimpan value pada slot terhapus. 
43.	Mengubah status slot menjadi terisi. 
44.	Mengembalikan hasil berhasil. 
45.	Mengembalikan hasil gagal jika tabel penuh. 
46.	(kosong) 
47.	Mendefinisikan fungsi pencarian data. 
48.	Menghitung indeks awal pencarian. 
49.	Memulai proses probing untuk pencarian. 
50.	Menghitung posisi slot yang diperiksa. 
51.	Mengecek apakah slot kosong. 
52.	Mengembalikan nilai kosong karena data tidak ditemukan. 
53.	Mengecek apakah slot berisi key yang dicari. 
54.	Mengembalikan data yang ditemukan. 
55.	Mengembalikan nilai kosong jika data tidak ditemukan. 
56.	(kosong) 
57.	Mendefinisikan fungsi untuk menampilkan isi tabel. 
58.	Menampilkan judul daftar loot monster. 
59.	Melakukan perulangan untuk setiap slot. 
60.	Menampilkan nomor indeks slot. 
61.	Mengecek apakah slot kosong. 
62.	Menampilkan informasi bahwa slot kosong. 
63.	Mengecek apakah slot terhapus. 
64.	Menampilkan informasi bahwa slot terhapus. 
65.	Menangani kondisi selain kosong dan terhapus. 
66.	Menampilkan key dan value yang tersimpan. 
67.	(kosong) 
68.	Mendefinisikan fungsi penghapusan data. 
69.	Menghitung indeks awal key yang akan dihapus. 
70.	Memulai probing untuk mencari data. 
71.	Menghitung posisi slot yang diperiksa. 
72.	Mengecek apakah slot kosong. 
73.	Mengembalikan gagal karena data tidak ditemukan. 
74.	Mengecek apakah key ditemukan. 
75.	Mengubah status menjadi terhapus. 
76.	Menghapus key dari slot. 
77.	Menghapus value dari slot. 
78.	Mengembalikan hasil berhasil. 
79.	Mengembalikan hasil gagal jika data tidak ditemukan. 
80.	(kosong) 
81.	Mendefinisikan class pengelola loot system. 
82.	Membuat constructor loot system. 
83.	Membuat objek hash table sebagai media penyimpanan. 
84.	(kosong) 
85.	Mendefinisikan fungsi menambahkan loot monster. 
86.	Memasukkan data monster ke hash table. 
87.	(kosong) 
88.	Mendefinisikan fungsi mengambil loot monster. 
89.	Mencari data monster pada hash table. 
90.	Mengecek apakah data ditemukan. 
91.	Mengembalikan daftar loot monster. 
92.	Mengembalikan nilai kosong jika tidak ditemukan. 
93.	(kosong) 
94.	Mendefinisikan fungsi menghapus monster. 
95.	Menjalankan proses penghapusan. 
96.	Mengecek apakah penghapusan berhasil. 
97.	Menampilkan pesan berhasil dihapus. 
98.	Menangani kondisi penghapusan gagal. 
99.	Menampilkan pesan monster tidak ditemukan. 
100.	(kosong) 
101.	Mendefinisikan fungsi untuk menampilkan seluruh loot. 
102.	Memanggil fungsi display dari hash table. 
103.	(kosong) 
104.	Mendefinisikan fungsi utama program. 
105.	Membuat objek sistem loot. 
106.	(kosong) 
107.	Menambahkan data loot untuk monster Dragon. 
108.	Menambahkan data loot untuk monster Zombie. 
109.	Menambahkan data loot untuk monster Vampire. 
110.	Menambahkan data loot untuk monster Skeleton. 
111.	Menambahkan data loot untuk monster Clown. 
112.	Menampilkan seluruh isi loot system. 
113.	(kosong) 
114.	Membuat daftar monster yang akan dicari. 
115.	Melakukan perulangan untuk setiap monster. 
116.	Menampilkan nama monster yang sedang diperiksa. 
117.	Mengambil data loot monster. 
118.	Mengecek apakah loot ditemukan. 
119.	Melakukan perulangan untuk setiap item loot. 
120.	Menampilkan nama item dan persentase drop rate. 
121.	Menangani kondisi loot tidak ditemukan. 
122.	Menampilkan pesan monster tidak ditemukan. 
123.	(kosong) 
124.	Menampilkan informasi monster yang akan dihapus. 
125.	Menghapus data monster Zombie. 
126.	Menghapus data monster Skeleton. 
127.	(kosong) 
128.	Menampilkan judul daftar loot setelah penghapusan. 
129.	Menampilkan kembali isi loot system. 
130.	(kosong) 
131.	Mengecek apakah file dijalankan secara langsung sebagai program utama. 
132.	Menjalankan fungsi utama program.

Output :

<img width="446" height="737" alt="Output" src="https://github.com/user-attachments/assets/cb56ca47-cb14-4ad2-83b6-35f7fb4020c4" />


Link : 
