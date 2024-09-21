import hashlib

def findPasscode(inputString):
    index = 0
    passcode = []
    while len(passcode) < 8:
        temp = inputString + str(index)
        firstHash = hashlib.md5(temp.encode()).hexdigest()
        while firstHash[:5] != '00000':
            index += 1
            temp = inputString + str(index)
            firstHash = hashlib.md5(temp.encode()).hexdigest()
        passcode.append(firstHash[5])
        index += 1
    passcode_str = ''.join(passcode)
    return passcode_str

def findPasscodePartTwo(inputString):
    index = 0
    passcode = [-1,-1,-1,-1,-1,-1,-1,-1]
    while -1 in passcode:
        temp = inputString + str(index)
        firstHash = hashlib.md5(temp.encode()).hexdigest()
        while firstHash[:5] != '00000':
            index += 1
            temp = inputString + str(index)
            firstHash = hashlib.md5(temp.encode()).hexdigest()
        if firstHash[5].isdigit():
            if int(firstHash[5]) < 8 and passcode[int(firstHash[5])] == -1:
                passcode[int(firstHash[5])] = firstHash[6]
        index += 1
    passcode_str = ''.join(passcode)
    return passcode_str

firstInput = "wtnhxymk"
passcode = findPasscode(firstInput)
passcodeTwo = findPasscodePartTwo(firstInput)
print(passcode)
print(passcodeTwo)

    
