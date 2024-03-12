#include<iostream>
#include<string>
using namespace std;

string answerfunction(const string& lines) {
    string newString;
    int i = 0;
    int length = lines.length();

    while (i < length) {
        if (lines[i] != lines[i + 1]) {
            newString += '1';
            newString += lines[i];
            i++;
        } else {
            int count = 1;
            do {
                count += 1;
                i++;
            } while (lines[i] == lines[i + 1]);
            newString += to_string(count);
            newString += lines[i];
            i++;
        }
    }

    return newString;
}

int main() {
    string lines = "1321131112";
    for (int i = 0; i < 40; i++) {
        lines = answerfunction(lines);
    }
    int final = lines.length();
    std::cout << "Part One: "<< final << std::endl;
    string lines1 = "1321131112";
    for (int i = 0; i < 50; i++) {
        lines1 = answerfunction(lines1);
    }
    int final1 = lines1.length();
    std::cout << "Part Two: " << final1 << std::endl;
}
