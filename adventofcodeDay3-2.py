def calculate(numbersArg, leaveOnes):
    numbers = numbersArg
    index = 0
    while len(numbers) > 1:
        zeros = 0
        ones = 0
        for number in numbers:
            zeros += 1 - number[index]
            ones += number[index]
        leave = int(leaveOnes(zeros, ones))
        numbers = [x for x in numbers if x[index] == leave]
        index += 1
    return numbers

with open('adventofcode_day3_task1.txt') as f:
    lines = f.readlines()

vectors = []
for line in lines:
    item = []
    for symbol in line:
        if symbol == '\n':
            vectors.append(item)
        else:
            item.append(int(symbol))

oxygen = calculate(vectors, lambda zeros, ones: zeros <= ones)[0]
co2 = calculate(vectors, lambda zeros, ones: zeros > ones)[0]
        
oxygenStr = ""
co2Str = ""

for x in oxygen:
    oxygenStr += str(x)

for x in co2:
    co2Str += str(x)

oxygen = int(oxygenStr, 2)
co2 = int(co2Str, 2)

print(f"Oxygen: {oxygen}, CO2: {co2}, x: {oxygen * co2}")
