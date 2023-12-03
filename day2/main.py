#Solution to Day 2 of Advent of Code

def getGames(lines: str) -> list:
    games = []
    
    for line in lines.splitlines():
        gamestr, roundstr = line.split(':')
        games.append(Game(getGameNumber(gamestr), getRoundsFromString(roundstr)))
    return games

def checkGames(games: list) -> int:
    sum = 0
    for game in games:
       sum += game.checkIfValidGame(12, 13, 14)
    return sum

def checkMinGames(games: list) -> int:
    sum = 0
    for game in games:
       sum += game.checkMinCubesSum()
    return sum
        
    
def getGameNumber(gameInfo: str) -> int:
    return int(gameInfo[5:])
        
def getRoundsFromString(roundInfo: str) ->  list:
    rounds = []
    roundStrs = roundInfo.split(';')
    for round in roundStrs:
        rounds.append(parseRound(round))
    return rounds

def parseRound(round: str):
    values = {"red" : 0, "green" : 0, "blue": 0}
    
    parts = round.split(",")
    for part in parts:
        quantity, color = part.split()
        values[color] = int(quantity)
    
    round = Round(values["red"], values["green"], values["blue"])
    return round


class Game:
    def __init__(self, game_number: int, rounds: list):
        self.game_number = game_number
        self.rounds = rounds

    def checkIfValidGame(self, redTot: int, greenTot: int, blueTot: int) -> int:
        for round in self.rounds:
            if round.red > redTot or round.green > greenTot or round.blue > blueTot:
                return 0
        return self.game_number

    def checkMinCubesSum(self) -> int:
        minR = -1
        minG = -1
        minB = -1
        for round in self.rounds:
            print(round.red, round.green, round.blue)
            if round.red > minR or minR == -1:
                minR = round.red
            if round.green > minG or minG == -1:
                minG = round.green
            if round.blue > minB or minB == -1:
                minB = round.blue
        print(minR * minG * minB)

        return max(minR, 1) * max(minG,1) * max(minB, 1)


    

class Round:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue



if __name__ == "__main__":
    input = open("input.txt").read()
    games = getGames(input)
    print(checkGames(games))
    print(checkMinGames(games))

