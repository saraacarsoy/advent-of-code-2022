file = open("/Users/saranilacarsoy/Documents/AdventOfCode/advent-of-code-2022/day10/2022-Day10Input.txt", "r").read().split("\n")

arr = []
n = 20

def checkMove(row):
    move_amount = row.split(" ")[-1]

    if (move_amount == "noop"):
        arr.append(0)
    else:
        arr.append(0)
        arr.append(int(move_amount))

for row in file:
    checkMove(row)

total_stregth = 0
def syncCycles():
    global n
    global total_stregth

    count = 1


    for x in arr[:n-1]:
        count += x

    strength = n * count
    total_stregth += strength

    n = n + 40


while (n < 221):
    syncCycles()

print(total_stregth)