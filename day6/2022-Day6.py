file = open("/Users/saranilacarsoy/Documents/AdventOfCode/advent-of-code-2022/day6/2022-Day6Input.txt", "r").read()

sub_strs = [file[i:i+14] for i in range(0, len(file), 1)]

def findMarker():
    marker = ""
    for i in sub_strs:
        if(len(i) == len(set(i))):
            marker = i
            break

    print(sub_strs.index(marker) + 14)

findMarker()