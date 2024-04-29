def checkTriplets(str):
    i = 0
    while i<len(str)-1:
        if ord(str[i+1]) == ord(str[i]) + 1 and ord(str[i+2]) == ord(str[i])+2:
            return True
        else:
            i+=1
    return False

def checkDoubles(str):
    count = 0
    i = 0
    while i<len(str)-1:
        z = ['i', 'o', 'l']
        if z in str:
            return False
        elif ((ord(str[i]) == ord(str[i+1])) and (ord(str[i+1]) != ord(str[i+2]))):
            count+=1
        i+=1
    return (count >= 2) 


    