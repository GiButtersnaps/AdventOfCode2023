#Solution to Day 1 of advent of code
def getNumber(line: str) -> int:
    i = 0
    j = len(line) - 1
    first, second = -1 , -1
    while(i < len(line) and j >= 0):
        if first > -1 and second > -1:
            break
        if line[i].isdigit() and first == -1:
            first = int(line[i])
        if line[j].isdigit() and second == -1:
            second = int(line[j])
        i += 1
        j -= 1
    digit = (first * 10) + second
    return digit

def getTotal(input: str) -> int:
    sum = 0
    lines = input.splitlines()
    for line in lines:
        sum += getNumber(line)
    return sum

def getNumberWithStrings(line: str) -> int:
    i = 0 
    j = len(line) - 1
    first, second = -1, -1 
    digitTrie = build_trie(digits)
    reversedDigitTrie = build_trie(reverseListOfStrings(digits))
    while (i < len(line) and j >= 0):
        if first > -1 and second > -1:
            break
        if first == -1:
            if line[i].isdigit():
                first = int(line[i])
            elif line[i] in digitTrie.root.children:
                first = checkForDigit(line[i:], digitTrie.root)
        if second == -1:
            if line[j].isdigit():
                second = int(line[j])
            elif line[j] in reversedDigitTrie.root.children:
                second = checkForDigitReversed(line[:j + 1], reversedDigitTrie.root)
        i += 1
        j -= 1
    digit = (first * 10) + second
    return digit

def reverseListOfStrings(strings: list) -> list:
    reversedList = []
    for string in strings:
        reversedList.append(string[::-1])
    return reversedList

def getTotalWithStrings(input: str) -> int:
    sum = 0
    lines = input.splitlines()
    for line in lines:
        sum += getNumberWithStrings(line)
    return sum 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

digits = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

digitToInt = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def build_trie(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie

def checkForDigit(line: str, node: TrieNode) -> int:
    pot_digit = ""
    digit = -1
    for char in line:
        if node.is_end_of_word:
            digit = digitToInt[pot_digit]
            break
        if char in node.children:
            pot_digit += char
            node = node.children[char]
        else:
            break
    return digit
        
        

def checkForDigitReversed(line: str, node: TrieNode):
    pot_digit = ""
    digit = -1
    for char in reversed(line):
        if node.is_end_of_word:
            digit = digitToInt[pot_digit[::-1]]
            break
        if char in node.children:
            pot_digit += char
            node = node.children[char]
        else:
            break
    return digit


if __name__ == "__main__":
    input = open("input.txt").read()
    total = getTotal(input)
    print(f"Sum of all lines: {total}")
    total = getTotalWithStrings(input)
    print(f"Sum of all lines: {total}")
