inputFile = '/home/sunil/Desktop/repos/AoC/2016/day7/instructions.txt'

def processData(inputFile):
    rawData = []
    with open(inputFile) as file:
        for line in file:
            line = line.strip()
            supernets = []
            hypernets = []
            current_segment = []
            in_brackets = False
            for x in line:
                if x == '[':
                    if current_segment:
                        supernets.append(''.join(current_segment))
                    current_segment = []
                    in_brackets = True
                elif x == ']':
                    if current_segment:
                        hypernets.append(''.join(current_segment))
                    current_segment = []
                    in_brackets = False
                else:
                    current_segment.append(x)
            if current_segment:
                if in_brackets:
                    hypernets.append(''.join(current_segment))
                else:
                    supernets.append(''.join(current_segment))
            rawData.append((supernets, hypernets))
    return rawData

def abbaFinder(segment):
    for i in range(len(segment) - 3):
        if segment[i] != segment[i + 1] and segment[i] == segment[i + 3] and segment[i + 1] == segment[i + 2]:
            return True
    return False

def extract_aba_patterns(segment):
    aba_patterns = set()
    for i in range(len(segment) - 2):
        if segment[i] != segment[i + 1] and segment[i] == segment[i + 2]:
            aba_patterns.add(segment[i:i+3])
    return aba_patterns

def find_bab_in_hypernets(aba_patterns, hypernets):
    bab_patterns = {aba[1] + aba[0] + aba[1] for aba in aba_patterns}
    for hypernet in hypernets:
        for i in range(len(hypernet) - 2):
            if hypernet[i] != hypernet[i + 1] and hypernet[i] == hypernet[i + 2]:
                bab = hypernet[i:i+3]
                if bab in bab_patterns:
                    return True
    return False

def count_tls(rawData):
    count = 0
    for supernets, hypernets in rawData:
        if any(abbaFinder(segment) for segment in supernets) and not any(abbaFinder(segment) for segment in hypernets):
            count += 1
    return count

def count_ssl(rawData):
    count = 0
    for supernets, hypernets in rawData:
        aba_patterns = set()
        for supernet in supernets:
            aba_patterns.update(extract_aba_patterns(supernet))
        if find_bab_in_hypernets(aba_patterns, hypernets):
            count += 1
    return count

inputData = processData(inputFile)
count_tls_ips = count_tls(inputData)
count_ssl_ips = count_ssl(inputData)

print("Count of IPs supporting TLS:", count_tls_ips)
print("Count of IPs supporting SSL:", count_ssl_ips)
