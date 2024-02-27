#include <iostream>
#include <fstream>
#include <string>

int vowel_count(const std::string& s) {
    int count = 0;
    for (char c : s) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
    }
    return count;
}

bool has_repeat(const std::string& s) {
    for (size_t i = 1; i < s.length(); ++i) {
        if (s[i - 1] == s[i]) {
            return true;
        }
    }
    return false;
}

bool has_forbidden(const std::string& s) {
    return (s.find("ab") != std::string::npos) ||
           (s.find("cd") != std::string::npos) ||
           (s.find("pq") != std::string::npos) ||
           (s.find("xy") != std::string::npos);
}

bool nice_part1(const std::string& s) {
    return (vowel_count(s) >= 3) && has_repeat(s) && !has_forbidden(s);
}

bool has_disjoint_pair(const std::string& s) {
    for (size_t i = 0; i < s.length() - 2; ++i) {
        std::string xy = s.substr(i, 2);
        if (s.find(xy, i + 2) != std::string::npos) {
            return true;
        }
    }
    return false;
}

bool has_xyx(const std::string& s) {
    for (size_t i = 2; i < s.length(); ++i) {
        if (s[i - 2] == s[i]) {
            return true;
        }
    }
    return false;
}

bool nice_part2(const std::string& s) {
    return has_disjoint_pair(s) && has_xyx(s);
}

int main() {
    std::ifstream file("day5input.txt");
    if (!file.is_open()) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }

    std::string line;
    int nice_count_part1 = 0;
    int nice_count_part2 = 0;

    while (std::getline(file, line)) {
        if (nice_part1(line)) {
            nice_count_part1++;
        }
        if (nice_part2(line)) {
            nice_count_part2++;
        }
    }

    std::cout << "Part 1 Nice Strings: " << nice_count_part1 << std::endl;
    std::cout << "Part 2 Nice Strings: " << nice_count_part2 << std::endl;

    return 0;
}
