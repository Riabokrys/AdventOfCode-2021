import statistics

class Item:
    def __init__(self, x : str = None):
        self.bits = []
        if x != None:
            self.add(x)

    def add(self, x: str):
        self.bits.append(int(x))

with open('F:\\SERHII\\Tobii\\adventofcode\\2021\\adventofcode_day3_task1.txt') as f:
    lines = f.readlines()

items = []
vectors = []
for line in lines:
    item = Item()
    for i, symbol in enumerate(line):
        if symbol == '\n':
            items.append(item)
        elif i >= len(vectors):
            item.add(symbol)
            vector = Item(symbol)
            vectors.append(vector)
        else:
            item.add(symbol)
            vectors[i].add(symbol)

oxigenItems = items
co2Items = items

for i, vector in enumerate(vectors):
    mode = statistics.mode(vector.bits)
    if len(oxigenItems) == 1 and len(co2Items) == 1:
        break
    if len(oxigenItems) > 1:
        oxigenItems = list(filter(lambda x: x.bits[i] == mode, oxigenItems))
    if len(co2Items) > 1:
        co2Items = list(filter(lambda x: x.bits[i] != mode, co2Items))
        
oxigenStr = ""
co2Str = ""

for x in oxigenItems[0].bits:
    oxigenStr += str(x)

for x in co2Items[0].bits:
    co2Str += str(x)

oxigen = int(oxigenStr, 2)
co2 = int(co2Str, 2)

print(f"Oxigen: {oxigen}, CO2: {co2}, x: {oxigen * co2}")