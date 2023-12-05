def getGameCardValues(input: str):
    sum = 0
    games = input.splitlines()
    for game in games:
        winningNums, myNumsStrings = game.split(':')[1].split('|')
        myNums = {}
        myNums.setdefault(False)
        # print(myNumsStrings.split())
        for num in myNumsStrings.split():
            myNums[num] = True
        value = 0
        for num in winningNums.split():
            if myNums.get(num):
                if value == 0:
                    value = 1
                else:
                    value = value * 2
        sum += value

    print(sum)

def getCardValue(games: list, gameNum: int) -> int:
    sum = 1
    if gameNum >= len(games):
        return 0
    if gameTotals.get(gameNum) != None:
        return gameTotals.get(gameNum)
    winningNums, myNumsStrings = games[gameNum].split(':')[1].split('|')
    myNums = {}
    myNums.setdefault(False)
    print(winningNums)
    for num in myNumsStrings.split():
        myNums[num] = True
    value = 0
    for num in winningNums.split():
        if myNums.get(num):
            value += 1
    for i in range(1, value + 1):
        sum += getCardValue(games, gameNum + i)
    gameTotals[gameNum] = sum
    return sum


def getNumberOfScratchCards(input: str):
    sum = 0
    games = input.splitlines()
    for i in range(len(games)):
        sum += getCardValue(games, i)
    print(sum)

        
        

if __name__ == "__main__":
    input = open("input.txt").read()
    global gameTotals
    gameTotals = {}
    getGameCardValues(input=input)
    getNumberOfScratchCards(input=input)