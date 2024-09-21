def answer_function(lines):
    new_string = ""
    i = 0
    length = len(lines)

    while i < length:
        if i + 1 < length and lines[i] != lines[i + 1]:
            new_string += '1' + lines[i]
            i += 1
        else:
            count = 1
            while i + 1 < length and lines[i] == lines[i + 1]:
                count += 1
                i += 1
            new_string += str(count) + lines[i]
            i += 1

    return new_string

def main():
    lines = "1321131112"
    for _ in range(40):
        lines = answer_function(lines)
    
    final = len(lines)
    print("Part One:", final)

    lines1 = "1321131112"
    for _ in range(50):
        lines1 = answer_function(lines1)

    final1 = len(lines1)
    print("Part Two:", final1)

if __name__ == "__main__":
    main()
