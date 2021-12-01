import sys

inputFileName = sys.argv[1]

depths = []
with open(inputFileName) as inputFile:
    lines = inputFile.readlines()
    depths = [int(line) for line in lines]
    
numberGreaterThanPrevious = 0
prevDepth = 9999999
for i in depths:
    if i > prevDepth:
        numberGreaterThanPrevious = numberGreaterThanPrevious + 1
    prevDepth = i
print(numberGreaterThanPrevious)
