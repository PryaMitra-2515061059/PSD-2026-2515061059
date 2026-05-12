def cari_produk(data_produk, target_kode):
    l = 0
    r = len(data_produk) - 1

    while l <= r:
        m = (l + r) // 2
        print(f"Mengecek data Tengah: {data_produk[m][0]}")
        if data_produk[m][0] == target_kode:
            return m
        elif data_produk[m][0] < target_kode:
            print("Cari ke bagian kanan")
            l = m + 1
        else:
            print("Cari ke bagian kiri")
            r = m - 1
    return -1

def tampilkan_produk(data):
    print("\nProduk Mitz Store")
    print("Kode\tNama Produk\tStok")
    print("-" * 30)

    for produk in data:
        print(f"{produk[0]}\t{produk[1]}\t\t{produk[2]}")

def main():
    data_produk = [
        [101, "Headset", 25],
        [102, "Laptop", 10],
        [103, "Monitor", 8],
        [104, "Mouse", 40],
        [105, "Printer", 5],
        [106, "Scanner", 3],
        [107, "Speaker", 15]
    ]

    tampilkan_produk(data_produk)
    try:
        kode_cari = int(input("\nMasukkan kode produk yang dicari: "))
    except ValueError:
        print("Input harus berupa angka!")
        return
    hasil = cari_produk(data_produk, kode_cari)
    if hasil != -1:
        print("\nProduk Ditemukan")
        print(f"Kode Produk : {data_produk[hasil][0]}")
        print(f"Nama Produk : {data_produk[hasil][1]}")
        print(f"Stok        : {data_produk[hasil][2]}")
    else:
        print("\nProduk tidak ditemukan")

if __name__ == "__main__":
    main()