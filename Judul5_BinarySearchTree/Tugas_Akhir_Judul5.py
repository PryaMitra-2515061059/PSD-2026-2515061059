class Node:
    def __init__(self, score, name):
        self.score = score
        self.name = name
        self.left = None
        self.right = None

class Leaderboard:
    def __init__(self):
        self.root = None

    def insert_node(self, root, score, name):
        if root is None:
            return Node(score, name)
        if score < root.score:
            root.left = self.insert_node(root.left, score, name)
        elif score > root.score:
            root.right = self.insert_node(root.right, score, name)
        return root

    def insert(self, score, name):
        self.root = self.insert_node(self.root, score, name)
    
    def find_min(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current

    def find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current

    def leaderboard(self, root):
        if root is None:
            return
        self.leaderboard(root.right)
        print(f"{root.name} - {root.score}")
        self.leaderboard(root.left)

    def search_score(self, root, score):
        if root is None:
            return None
        if score == root.score:
            return root
        if score < root.score:
            return self.search_score(root.left, score)
        return self.search_score(root.right, score)
    
    def height(self, root):
        if root is None:
            return -1
        height_left = self.height(root.left)
        height_right = self.height(root.right)
        return 1 + max(height_left, height_right)

    def delete_node(self, root, score):
        if root is None:
            return None
        if score < root.score:
            root.left = self.delete_node(root.left, score)
        elif score > root.score:
            root.right = self.delete_node(root.right, score)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min_node(root.right)
                root.score = successor.score
                root.right = self.delete_node(root.right, successor.score)
        return root

    def delete(self, score):
        self.root = self.delete_node(self.root, score)
    
    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0
        return root.score + self.sum_nodes(root.left) + self.sum_nodes(root.right)


def main():
    lb = Leaderboard()
    pilih = 0
    while pilih != 9:
        print("\nLeaderboard Mitz Adventure")
        print("1. Tambah Pemain")
        print("2. Hapus Pemain")
        print("3. Tampilkan Leaderboard")
        print("4. Cari Score")
        print("5. Top Leaderboard")
        print("6. Bottom Leaderboard")
        print("7. Jumlah Pemain dan Total Score")
        print("8. Tinggi Leaderboard")
        print("9. Keluar")

        pilih = int(input("Pilih: "))

        if pilih == 1:
            nama = input("Nama pemain : ")
            Score = int(input("Score : "))
            lb.insert(Score, nama)
            print("Leaderboard Telah Diperbarui")
        elif pilih == 2:
            Score = int(input("Score yang dihapus: "))
            lb.delete(Score)
            print("Berhasil Dihapus Dari Leaderboard")
        elif pilih == 3:
            print("\nLeaderboard")
            lb.leaderboard(lb.root)
        elif pilih == 4:
            Score = int(input("Cari Score : "))
            hasil = lb.search_score(lb.root, Score)
            if hasil:
                print(f"Pemilik Score {Score} adalah : {hasil.name}")
            else:
                print("Score tidak ditemukan")
        elif pilih == 5:
            top = lb.find_max(lb.root)
            if top:
                print(f"Top Leaderboard adalah : {top.name} dengan Score {top.score}")
            else:
                print("Leaderboard kosong")
        elif pilih == 6:
            bot = lb.find_min(lb.root)
            if bot:
                print(f"Bottom Leaderboard adalah : {bot.name} dengan Score {bot.score}")
            else:
                print("Leaderboard kosong")
        elif pilih == 7:
            print(f"Jumlah Pemain: {lb.count_nodes(lb.root)}")
            print(f"Total Score: {lb.sum_nodes(lb.root)}")
        elif pilih == 8:
            print(f"Tinggi Leaderboard: {lb.height(lb.root)}")
        elif pilih == 9:
            print("Selamat Tinggal Ditunggu Highscore barunya di Leaderboard Mitz Adventure 😊")

if __name__ == "__main__":
    main()