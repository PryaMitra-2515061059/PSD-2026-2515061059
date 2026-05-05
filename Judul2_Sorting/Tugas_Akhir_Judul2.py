def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j][1] < data[j + 1][1]:
                tukar(data, j, j + 1)
                swapped = True
        if not swapped:
            break

def main():
    try:
        n = int(input("Masukkan jumlah peserta: "))
    except ValueError:
        print("Input tidak valid!")
        return

    data = []
    print("Masukkan nama dan skor peserta:")
    for i in range(n):
        nama = input(f"Nama peserta ke-{i+1}: ")
        while True:
            try:
                skor = int(input(f"Skor {nama}: "))
                data.append((nama, skor))
                break
            except ValueError:
                print("Input skor harus angka!")

    bubble_sort(data)
    print("\nRanking peserta:")
    for i in range(len(data)):
        print(f"{i+1}. {data[i][0]} - {data[i][1]}")

if __name__ == "__main__":
    main()