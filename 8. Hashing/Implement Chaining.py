
class MyHash:
    BUCKET:int
    # table = [None]*BUCKET
    def __init__(self, b):
        self.BUCKET = b
        table = [None]*self.BUCKET

    def my_hash(self, b:int):
        self.BUCKET = b
        table = [None]*b

    def insert(self, key):
        i = key % self.BUCKET
        self.table[i].append(key)

    def remove(self, key):
        i = key % self.BUCKET
        self.table[i].remove(key)

    def search(self, key):
        i = key % self.BUCKET
        for x in self.table[i]:
            if(x == key):
                return True
        return False