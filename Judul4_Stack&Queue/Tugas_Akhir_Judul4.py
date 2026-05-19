class GameSave:
    def __init__(self, max_save=10):
        self.MAX = max_save
        self.save_stack = [None] * self.MAX
        self.top = -1

    def is_full(self):
        return self.top == self.MAX - 1

    def is_empty(self):
        return self.top == -1
    
    def save_game(self, checkpoint):
        if self.is_full():
            print("Slot save penuh, tidak dapat menyimpan game")
            return
        self.top += 1
        self.save_stack[self.top] = checkpoint
        print(f"Game berhasil disimpan di Save File : {checkpoint}")

    def delete_save(self):
        if self.is_empty():
            print("Tidak dapat menemukan Save File")
            return
        print(f"Save File {self.save_stack[self.top]} Berhasil DiHapus")
        self.top -= 1

    def latest_save(self):
        if self.is_empty():
            print("Kamu belum mempunyai Save File")
            return
        print(f"Save File terakhir: {self.save_stack[self.top]}")

    def show_saves(self):
        if self.is_empty():
            print("Data save kosong")
            return
        print("\nSave Game Mitz Adventure")
        for i in range(self.top, -1, -1):
            print(f"{i+1}. {self.save_stack[i]}")

def main():
    game = GameSave()
    while True:
        print("\nMenu Save Game Mitz Adventure")
        print("1. Save Game")
        print("2. Hapus Save File Terakhir")
        print("3. Lihat Save Terakhir")
        print("4. Tampilkan Semua Save")
        print("0. Keluar")
        pilih = int(input("Pilih menu : "))
        if pilih == 1:
            checkpoint = input("Masukkan nama Save File : ")
            game.save_game(checkpoint)
        elif pilih == 2:
            game.delete_save()
        elif pilih == 3:
            game.latest_save()
        elif pilih == 4:
            game.show_saves()
        elif pilih == 0:
            print("Selamat Melanjutkan Petualangan")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
