file = open("/Users/saranilacarsoy/Documents/AdventOfCode/day3/2022-day3Input.txt", "r").read().split("\n")

alphabeth = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def position(letter):
    return alphabeth.find(letter) + 1

def compareHalves(row):
    firstHalf = row[:len(row)//2]
    secondHalf = row[len(row)//2:]
    commons = (set(firstHalf) & set(secondHalf))

    for i in commons:
        return position(i)

def divideToChunks():
    x = [file[i:i + 3] for i in range(0, len(file), 3)]
    count2 = 0

    for i in x:
        common = (set(i[0]) & set(i[1]) & set(i[2]))
        count2 += position(list(common)[0])
    print(count2)

count = 0
for row in file:
    count += compareHalves(row)

#print(count)

divideToChunks()