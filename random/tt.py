class HashMap:
    def __init__(self):
        self.MAX = 50
        self.map = [None for i in range(self.MAX)]

    def getHash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.MAX

    def add(self,key,value):
        hash_ = self.getHash(key)
        self.map[hash_] = value

    def get(self,key):
        hash_ = self.getHash(key)
        return self.map[hash_]

    def print(self):
        for index,val in enumerate(self.map):
            if val:
                print(f"{index}-->{val}")

hashmap = HashMap()

hashmap.add('wahab',16)
hashmap.add('peres',14)
hashmap.add('konate',15)


hashmap.print()

print(hashmap.get('peres'))
print(hashmap.get('wahab'))
