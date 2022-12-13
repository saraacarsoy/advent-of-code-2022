file = open("/Users/saranilacarsoy/Documents/AdventOfCode/advent-of-code-2022/day4/2022-Day4Input.txt", "r").read().split("\n")

amount = 0
amount1=0
totalArr = []

def compareAreas(arr1, arr2):
    global amount
    global amount1
    global interval

    sharedElements = sorted(set(arr1) & set(arr2))


    if(len(sharedElements) > 0):
        amount1 += 1
        

    if(sharedElements == list(arr1) or sharedElements == list(arr2)):
        totalArr.append(row)
        amount += 1

def formatRow(row):

    elves = row.split(",")
    arr = []

    for i in elves:
        elfArray = [int(numeric_string) for numeric_string in i.split("-")]
        arr.append(range(elfArray[0], elfArray[1]+1))
    
    compareAreas(arr[0], arr[1])        

for row in file:
    formatRow(row)

print(amount1)