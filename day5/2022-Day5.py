file = open("/Users/saranilacarsoy/Documents/AdventOfCode/advent-of-code-2022/day5/2022-Day5Input.txt", "r").read().split("\n")

#remove from left and add to the left

dicts = {
    "1": ['N', 'T', 'B', 'S', 'Q', 'H', 'G', 'R'],
    "2": ['J', 'Z', 'P', 'D', 'F', 'S', 'H'],
    "3": ['V', 'H', 'Z'],
    "4": ['H', 'G', 'F', 'J', 'Z', 'M'],
    "5": ['R', 'S', 'M', 'L', 'D', 'C', 'Z', 'T'],
    "6": ['J', 'Z', 'H', 'V', 'W', 'T', 'M'],
    "7": ['Z', 'L', 'P', 'F', 'T'],
    "8": ['S', 'W', 'V', 'Q'],
    "9": ['C', 'N', 'D', 'T', 'M', 'L', 'H', 'W']
}

def getElementsToMove(amount, from_arr, to_arr):
    cargo = []
    arr = dicts[from_arr]

    cargo = arr[:amount]
    flipped_cargo = cargo[::-1]

    del dicts[from_arr][:amount] # remove from 

    # for i in cargo:
    for i in flipped_cargo:
        dicts[to_arr].insert(0, i) # add to


def getMovement(row):
    movements = row.split(" ", 6)

    move_amount = int(movements[1])
    from_arr =  movements[3]
    to_arr = movements[5]

    getElementsToMove(move_amount, from_arr, to_arr)


for row in file:
    getMovement(row)

print(dicts)