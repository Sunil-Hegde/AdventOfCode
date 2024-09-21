import re
instructions = '/home/sunil/Desktop/repos/AoC/2015/day19/instructions.txt'
molecule = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
def processInstructions(instructions):
    with open(instructions) as file:
        rawData = []
        for line in file:
            x = line.split();
            tempDict = {'from' : x[0], 'to' : x[-1]}
            rawData.append(tempDict)
    return rawData

def find(s, ch):
    return [ [i.start(), i.end()] for i in re.finditer(ch, s)]

def countUniqueMolecules(processedInstructions, molecule):
    final = []
    for i in processedInstructions:
        x = find(molecule,i['from'])
        for j in x:
            temp = molecule
            new_string = temp[:int(j[0])] + str(i['to']) + temp[int(j[1]):]
            if new_string not in final:
                final.append(new_string)
    return len(final)

def reverseSearch(molecule, processedInstructions):
    steps = 0
    while molecule != 'e':
        for i in processedInstructions:
            if i['to'] in molecule:
                molecule = molecule.replace(i['to'], i['from'], 1)
                steps += 1
    return steps

print("Part One: " + str(countUniqueMolecules(processInstructions(instructions), molecule)))
print("Part Two: " + str(reverseSearch(molecule, processInstructions(instructions))))

