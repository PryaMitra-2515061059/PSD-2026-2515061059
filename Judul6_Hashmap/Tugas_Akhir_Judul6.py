class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2

class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY

class MitzAdventurelootDropRate:
    def __init__(self, size=5):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (hash(key) % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def display(self):
        print("\nDROP RATE MONSTER DI MITZ ADVENTURE")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"{self.table[i].key} -> {self.table[i].value}")
    
    def delete(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return False
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                self.table[i].state = SlotState.DELETED
                self.table[i].key = None
                self.table[i].value = None
                return True
        return False

class LootSystem:
    def __init__(self):
        self.map = MitzAdventurelootDropRate()
        
    def add_monster_loot(self, monster, loot_list):
        self.map.insert(monster, loot_list)

    def get_loot(self, monster):
        entry = self.map.search(monster)
        if entry:
            return entry.value
        return None
    
    def remove_monster(self, monster):
        result = self.map.delete(monster)
        if result:
            print(f"{monster} berhasil dihapus dari loot system")
        else:
            print(f"{monster} tidak ditemukan")

    def all_loot(self):
        self.map.display()

def main():
    game_loot = LootSystem()

    game_loot.add_monster_loot("Dragon", [("Sword", 5), ("Gold", 50), ("Gem", 45)]) 
    game_loot.add_monster_loot("Zombie", [("Bone", 60), ("Rotten Flesh", 40)])
    game_loot.add_monster_loot("Vampire", [("Blood", 80), ("Cloak", 20)])
    game_loot.add_monster_loot("Skeleton", [("Arrow", 50), ("Bow", 50)])
    game_loot.add_monster_loot("Clown", [("Balloon", 90), ("Joke Book", 10)])
    game_loot.all_loot()

    monsters = ["Dragon", "Zombie", "Vampire", "Skeleton", "Clown", "Ghost"]
    for m in monsters:
        print(f"\nLOOT {m.upper()}")
        loot = game_loot.get_loot(m)
        if loot:
            for item, rate in loot:
                print(f"- {item}: {rate}%")
        else:
            print("Monster tidak ditemukan")
    
    print("\nMonster yang akan dihapus: Zombie, Skeleton")
    game_loot.remove_monster("Zombie")
    game_loot.remove_monster("Skeleton")

    print("\nList Loot setelah penghapusan:")
    game_loot.all_loot()

if __name__ == "__main__":
    main()