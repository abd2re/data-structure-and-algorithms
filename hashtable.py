class HashTable:
    def __init__(self):
        self.max = 50
        self.arr = [[] for i in range(self.max)]

    def get_hash(self,input):
        h = 0
        for char in input:
            h += ord(char)
        return h % self.max

    def __getitem__(self,key):
        h = self.get_hash(key)
        for elem in self.arr[h]:
            if elem[0] == key:
                return elem[1]


    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False

        for idx, elem in enumerate(self.arr[h]):
            if elem[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
                break

        if not found:
            self.arr[h].append((key,value))


    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx, elem in enumerate(self.arr[h]):
            if elem[0] == key:
                del self.arr[h][idx]





hashmap = HashTable()

hashmap['wahab'] = 10
hashmap['aziz'] = 10
hashmap['ziza'] = 17
hashmap['aziz'] = 1
#del hashmap['wahab']
#del hashmap['aziz']
print(hashmap['ziza'])
print(hashmap['aziz'])

print(hashmap.arr)

