nSets = int(input())

nDiamonds = []
for i in range(nSets):
    posDiamond = list(filter(lambda char: char != ".", input()))
    quantDiamonds = 0
    print(len(posDiamond))
    for j in range(len(posDiamond)):
        if posDiamond[j] == "<":
            for k in range(len(posDiamond) - 1, -1, -1):
                print(k)
                if posDiamond[k] == ">":
                    posDiamond.pop(j)
                    posDiamond.pop(k)
                    quantDiamonds += 1

for num in nDiamonds:
    print(num)
