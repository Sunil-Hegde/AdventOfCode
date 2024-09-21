def vowel_count(s):
    return sum(1 for c in s if c in 'aeiou')

def has_repeat(s):
    i = 1
    while i < len(s):
        if s[i-1] == s[i]:
            return True
        i += 1
    return False

def has_forbidden(s):
    return 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s

def nice_part1(s):
    return vowel_count(s) >= 3 and has_repeat(s) and not has_forbidden(s)

def day5_part1():
    print(sum(1 for line in open('day5input.txt') if nice_part1(line)))

def has_disjoint_pair(s):
    i = 0
    while i < len(s) - 1:
        xy = s[i:i+2]
        if xy in s[i+2:]:
            return True
        i += 1
    return False

def has_xyx(s):
    i = 2
    while i < len(s):
        if s[i-2] == s[i]:
            return True
        i += 1
    return False

def nice_part2(s):
    return has_disjoint_pair(s) and has_xyx(s)

def day5_part2():
    print(sum(1 for line in open('day5input.txt') if nice_part2(line)))

# Run the functions
day5_part1()
day5_part2()
