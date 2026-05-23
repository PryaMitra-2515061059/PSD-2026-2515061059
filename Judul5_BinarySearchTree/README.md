Tugas Akhir Percobaan 5 : Binary Search Tree

Judul Proyek : Leaderboard Pada Game Mitz Adventure


Source Code :



1.	Membuat class Node untuk menyimpan data score pemain dan nama pemain. 
2.	Membuat function __init__ untuk inisialisasi object Node. 
3.	Menyimpan nilai score pemain ke dalam variabel score. 
4.	Menyimpan nama pemain ke dalam variabel name. 
5.	Membuat child kiri dengan nilai awal None. 
6.	Membuat child kanan dengan nilai awal None. 
7.	(Kosong) 
8.	Membuat class Leaderboard untuk mengelola data leaderboard menggunakan Binary Search Tree. 
9.	Membuat function __init__ pada class Leaderboard. 
10.	Membuat root awal dengan nilai None. 
11.	(Kosong) 
12.	Membuat function insert_node untuk menambahkan node baru ke dalam tree. 
13.	Mengecek apakah root kosong. 
14.	Membuat node baru jika root kosong. 
15.	Mengecek apakah score lebih kecil dari root. 
16.	Menambahkan node ke bagian kiri tree secara rekursif. 
17.	Mengecek apakah score lebih besar dari root. 
18.	Menambahkan node ke bagian kanan tree secara rekursif. 
19.	Mengembalikan root setelah proses insert selesai. 
20.	(Kosong) 
21.	Membuat function insert untuk memanggil proses insert node. 
22.	Menambahkan data ke tree melalui function insert_node. 
23.	(Kosong) 
24.	Membuat function find_min untuk mencari score terkecil. 
25.	Mengecek apakah root kosong. 
26.	Mengembalikan None jika tree kosong. 
27.	Menyimpan root ke variabel current. 
28.	Melakukan perulangan selama node kiri masih ada. 
29.	Berpindah ke node paling kiri. 
30.	Mengembalikan node dengan score terkecil. 
31.	(Kosong) 
32.	Membuat function find_max untuk mencari score terbesar. 
33.	Mengecek apakah root kosong. 
34.	Mengembalikan None jika tree kosong. 
35.	Menyimpan root ke variabel current. 
36.	Melakukan perulangan selama node kanan masih ada. 
37.	Berpindah ke node paling kanan. 
38.	Mengembalikan node dengan score terbesar. 
39.	(Kosong) 
40.	Membuat function leaderboard untuk menampilkan isi leaderboard. 
41.	Mengecek apakah root kosong. 
42.	Menghentikan function jika tree kosong. 
43.	Menampilkan subtree kanan terlebih dahulu secara rekursif. 
44.	Menampilkan nama pemain dan score. 
45.	Menampilkan subtree kiri secara rekursif. 
46.	(Kosong) 
47.	Membuat function search_score untuk mencari score tertentu. 
48.	Mengecek apakah root kosong. 
49.	Mengembalikan None jika score tidak ditemukan. 
50.	Mengecek apakah score sama dengan root. 
51.	Mengembalikan node jika score ditemukan. 
52.	Mengecek apakah score lebih kecil dari root. 
53.	Mencari score di subtree kiri secara rekursif. 
54.	Mencari score di subtree kanan secara rekursif. 
55.	(Kosong) 
56.	Membuat function height untuk menghitung tinggi tree. 
57.	Mengecek apakah root kosong. 
58.	Mengembalikan -1 jika tree kosong. 
59.	Menghitung tinggi subtree kiri. 
60.	Menghitung tinggi subtree kanan. 
61.	Mengembalikan tinggi terbesar ditambah 1. 
62.	(Kosong) 
63.	Membuat function delete_node untuk menghapus node dari tree. 
64.	Mengecek apakah root kosong. 
65.	Mengembalikan None jika tree kosong. 
66.	Mengecek apakah score lebih kecil dari root. 
67.	Menghapus node di subtree kiri secara rekursif. 
68.	Mengecek apakah score lebih besar dari root. 
69.	Menghapus node di subtree kanan secara rekursif. 
70.	Menjalankan proses jika node ditemukan. 
71.	Mengecek apakah child kiri kosong. 
72.	Mengembalikan child kanan jika child kiri kosong. 
73.	Mengecek apakah child kanan kosong. 
74.	Mengembalikan child kiri jika child kanan kosong. 
75.	Menjalankan proses jika node memiliki dua child. 
76.	Mencari successor dari subtree kanan. 
77.	Mengganti score root dengan score successor. 
78.	Menghapus node successor dari subtree kanan. 
79.	Mengembalikan root setelah proses delete selesai. 
80.	(Kosong) 
81.	Membuat function delete untuk memanggil proses delete node. 
82.	Menghapus node berdasarkan score. 
83.	(Kosong) 
84.	Membuat function count_nodes untuk menghitung jumlah pemain. 
85.	Mengecek apakah root kosong. 
86.	Mengembalikan 0 jika tree kosong. 
87.	Menghitung jumlah node secara rekursif. 
88.	(Kosong) 
89.	Membuat function sum_nodes untuk menghitung total seluruh score. 
90.	Mengecek apakah root kosong. 
91.	Mengembalikan 0 jika tree kosong. 
92.	Menjumlahkan seluruh score secara rekursif. 
93.	(Kosong) 
94.	Membuat function main sebagai program utama. 
95.	Membuat object lb dari class Leaderboard. 
96.	Membuat variabel pilih dengan nilai awal 0. 
97.	Melakukan perulangan selama pilihan bukan 9. 
98.	Menampilkan judul program leaderboard. 
99.	Menampilkan menu tambah pemain. 
100.	Menampilkan menu hapus pemain. 
101.	Menampilkan menu leaderboard. 
102.	Menampilkan menu cari score. 
103.	Menampilkan menu top leaderboard. 
104.	Menampilkan menu bottom leaderboard. 
105.	Menampilkan menu jumlah pemain dan total score. 
106.	Menampilkan menu tinggi leaderboard. 
107.	Menampilkan menu keluar program. 
108.	(Kosong) 
109.	Meminta input pilihan menu dari user. 
110.	(Kosong) 
111.	Mengecek apakah user memilih menu 1. 
112.	Meminta input nama pemain. 
113.	Meminta input score pemain. 
114.	Menambahkan data pemain ke leaderboard. 
115.	Menampilkan pesan bahwa leaderboard berhasil diperbarui. 
116.	Mengecek apakah user memilih menu 2. 
117.	Meminta input score yang akan dihapus. 
118.	Menghapus data score dari leaderboard. 
119.	Menampilkan pesan berhasil dihapus. 
120.	Mengecek apakah user memilih menu 3. 
121.	Menampilkan judul leaderboard. 
122.	Menampilkan seluruh isi leaderboard. 
123.	Mengecek apakah user memilih menu 4. 
124.	Meminta input score yang dicari. 
125.	Mencari score di leaderboard. 
126.	Mengecek apakah hasil pencarian ditemukan. 
127.	Menampilkan nama pemilik score jika ditemukan. 
128.	Menjalankan kondisi jika score tidak ditemukan. 
129.	Menampilkan pesan score tidak ditemukan. 
130.	Mengecek apakah user memilih menu 5. 
131.	Mencari score tertinggi. 
132.	Mengecek apakah data ditemukan. 
133.	Menampilkan top leaderboard. 
134.	Menjalankan kondisi jika leaderboard kosong. 
135.	Menampilkan pesan leaderboard kosong. 
136.	Mengecek apakah user memilih menu 6. 
137.	Mencari score terendah. 
138.	Mengecek apakah data ditemukan. 
139.	Menampilkan bottom leaderboard. 
140.	Menjalankan kondisi jika leaderboard kosong. 
141.	Menampilkan pesan leaderboard kosong. 
142.	Mengecek apakah user memilih menu 7. 
143.	Menampilkan jumlah pemain. 
144.	Menampilkan total score seluruh pemain. 
145.	Mengecek apakah user memilih menu 8. 
146.	Menampilkan tinggi leaderboard. 
147.	Mengecek apakah user memilih menu 9. 
148.	Menampilkan pesan penutup program. 
149.	(Kosong) 
150.	Mengecek apakah file dijalankan sebagai program utama. 
151.	Menjalankan function main(). 
