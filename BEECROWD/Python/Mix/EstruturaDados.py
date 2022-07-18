import sys

for line in sys.stdin:
    line = line.rstrip("\n")
    if len(line) == 1:
        nOper = int(line)
        inputList, outputList = [], []
    else:
        typeOper, resultNumber = map(int, line.split())
        if typeOper == 1:
            inputList.append(resultNumber)
        else:
            outputList.append(resultNumber)

print(inputList)
print(outputList)
