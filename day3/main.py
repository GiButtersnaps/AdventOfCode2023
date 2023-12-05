
def checkNeighbors(row: int, col: int, symbols: dict) -> bool:
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if symbols.get((i, j)):
                return True
    return False

def checkNeighbors2(row: int, col: int, symbols: dict) -> bool:
    result = {}
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if symbols.get((i, j)):
                result[(i, j)] = True
    return result


def getSumOfParts(input: str) -> int:
    schematic = []
    symbols = {}
    symbols.setdefault(False)
    sum = 0
    i = 0
    for line in input.splitlines():
        schematic.append([])
        j = 0
        for char in line:
            if not char.isdigit() and char != '.':
                print(char)
                symbols[(i, j)] = True
            schematic[i].append(char)
            j += 1
        i += 1
    # print(schematic)
    print(symbols)
    for i, row in enumerate(schematic):
        
        j = 0
        while j < len(row):
            currentPart = ''
            isValid = False
            if row[j].isdigit():
                while j < len(row) and row[j].isdigit():
                    if checkNeighbors(i, j, symbols=symbols):
                        isValid = True
                    currentPart += row[j]
                    # print(currentPart)
                    j += 1
                if isValid:
                    print(currentPart)
                    sum += int(currentPart)
                # print(currentPart)
            # print(currentPart)
            j += 1
    print(sum)

def getGears(input: str) -> int:
    schematic = []
    symbols = {}
    symbols.setdefault(False)
    sum = 0
    i = 0
    for line in input.splitlines():
        schematic.append([])
        j = 0
        for char in line:
            if char == '*':
                symbols[(i, j)] = True
            schematic[i].append(char)
            j += 1
        i += 1
    # print(schematic)
    # print(symbols)
    parts = []
    # iterate through scematic to find all parts and map them to their neighboring '*' s
    for i, row in enumerate(schematic):
        j = 0
        while j < len(row):
            currentPart = ''
            if row[j].isdigit():
                gears = {}
                coordinates = (i, j)
                while j < len(row) and row[j].isdigit():
                    gears.update(checkNeighbors2(i, j, symbols=symbols))
                    currentPart += row[j]
                    j += 1
                part = Part(x=coordinates[0], y=coordinates[1], value=int(currentPart))
                part.gears.update(gears)
                parts.append(part)
                # print(currentPart)
            # print(currentPart)
            j += 1
    gearMap = {}
    for part in parts:
        # print(part.gears)
        for gear in part.gears:
            if gear in gearMap:
                gearMap[gear].append(part)
            else:
                gearMap[gear] = [part]
    
    for gears in gearMap.values():
        count = 0
        gearTotal = 0
        for part in gears:
            print(part)
            if gearTotal == 0:
                gearTotal = part.value
            else:
                gearTotal *= part.value
            count += 1
        if count == 2:
            sum += gearTotal
    print(sum)

class Part:
    def __init__(self, x, y, value: int):
        self.coordinates = (x, y)
        self.value = value
        self.gears = {}

    

if __name__ == "__main__":
    input = open("input.txt").read()
    # getSumOfParts(input=input)
    getGears(input=input)

