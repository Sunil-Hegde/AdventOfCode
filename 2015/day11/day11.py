def checkTriplets(s):
    i = 0
    while i < len(s) - 2:
        if ord(s[i+1]) == ord(s[i]) + 1 and ord(s[i+2]) == ord(s[i]) + 2:
            return True
        else:
            i += 1
    return False

def checkDoubles(s):
    count = 0
    i = 0
    while i < len(s) - 1:
        forbidden_chars = ['i', 'o', 'l']
        if s[i] in forbidden_chars:
            return False
        elif s[i] == s[i+1] and (i == len(s) - 2 or s[i+1] != s[i+2]):
            count += 1
        i += 1
    return count >= 2

def generatePassword(s):
    i = True
    while i:
        if checkDoubles(s) and checkTriplets(s):
            i = False
        else:
            index = len(s) - 1
            while index >= 0 and s[index] == 'z':
                index -= 1
            if index >= 0:
                s = s[:index] + chr(ord(s[index]) + 1) + 'a' * (len(s) - index - 1)
            else:
                s = 'a' + s
    return s

str = "hepxcrrq"
print("Part one: " + generatePassword(str))
str1 = "hepxxzaa"
print("Part two: " + generatePassword(str1))
