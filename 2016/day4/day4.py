from collections import Counter
inputFile = '/home/sunil/Desktop/repos/AoC/2016/day4/instructions.txt'

def processData(inputFile):
    rawData = []
    with open(inputFile) as file:
        for line in file:
            lineData = [[], [], []]
            keyCode = ""
            roomCode = ""
            checksum = ""
            flag = 0
            for letter in line:
                if letter.isalpha() and flag == 0:
                    keyCode+=letter
                elif letter.isalpha() and flag == 1:
                    checksum+=letter
                elif letter.isdigit():
                    roomCode+=letter
                elif letter == '[':
                    flag = 1
            lineData[0], lineData[1], lineData[2] = keyCode, int(roomCode), checksum
            rawData.append(lineData)
    return rawData


def letterCounter(line):
    letter_counts = Counter(line)
    sorted_letters = sorted(letter_counts.items(), key=lambda item: (-item[1], item[0]))
    most_common_letters = sorted_letters[:5]
    result = ''.join(letter for letter, count in most_common_letters)
    return result

def shift_letter(letter, shift):
    shifted_letter = chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
    return shifted_letter

def checkerAndAdder(rawData):
    roomSum = 0
    roomNumber = 0
    for code in rawData:
        if letterCounter(code[0]) == code[2]:
            roomSum += code[1]
            newName = ""
            shiftNumber = code[1] % 26
            for letter in code[0]:
                shiftedLetter = shift_letter(letter, shiftNumber)
                newName+=shiftedLetter
            if newName == "northpoleobjectstorage":
                roomNumber = code[1]
    return roomSum, roomNumber

processedData = processData(inputFile)
finalSum, roomnumber = checkerAndAdder(processedData)
print(finalSum)
print(roomnumber)

