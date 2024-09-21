from collections import Counter

def processData(inputFile):
    char_lists = []
    with open(inputFile) as file:
        for line in file:
            line = line.strip()
            for i, char in enumerate(line):
                if i >= len(char_lists):
                    char_lists.append([])
                char_lists[i].append(char)
    
    most_common_letters = []
    least_common_letters = []
    for char_list in char_lists:
        countLetters = Counter(char_list)
        most_common = countLetters.most_common(1)[0][0]  
        least_common = countLetters.most_common()[-1][0]  
        most_common_letters.append(most_common)
        least_common_letters.append(least_common)
    
    return ''.join(most_common_letters), ''.join(least_common_letters)

inputFile = '/home/sunil/Desktop/repos/AoC/2016/day6/instructions.txt'
most_common_letters, least_common_letters = processData(inputFile)

print("Most common letters: ", most_common_letters)
print("Least common letters: ", least_common_letters)
