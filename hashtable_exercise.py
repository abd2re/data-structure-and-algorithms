class HashMap:
    def __init__(self,MAX):
        self.MAX = MAX
        self.arr = [[] for i in range(self.MAX)]

    def hash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.hash(key)
        found = False

        for idx, elem in enumerate(self.arr[h]):
            if elem[0] == key and len(elem) == 2:
                self.arr[h][idx] = (key,value)
                found = True
                break

        if found is False:
            self.arr[h].append((key,value))

    def __delitem__(self, key):
        h = self.hash(key)

        for idx, elem in enumerate(self.arr[h]):
            if elem[0] == key:
                del self.arr[h][idx]


    def __getitem__(self, key):
        h = self.hash(key)
        for elem in self.arr[h]:
            if elem[0] == key:
                return elem[1]



    def get_keys(self):
        keys = []
        for adress in self.arr:
            if len(adress) >= 1:
                for i in adress:
                    keys.append(i[0])

        return keys

    def get_values(self):
        values = map(lambda data: self[data], self.get_keys())
        return list(values)




import csv
file = open('//wsl$/Ubuntu/home/abd2re/data-structures/nyc_weather.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
data = []
for row in csvreader:
        data.append(row)


hashmap = HashMap(len(data))

for elem in data:
    hashmap[elem[0]] = elem[1]

print(hashmap['Jan 8'])

print(hashmap.get_keys())
print(hashmap.get_values())


print('------')

# 1.1

average = []
for idx, elem in enumerate(data):
    if idx == 7:
        break
    average += [int(hashmap[elem[0]])]

print(sum(average)/len(average))

# 1.2

print(max(hashmap.get_values()))