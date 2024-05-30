#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

struct instruction {
    string opcode;
    char operand;
    int offset;
};

instruction processData(const string& line) {
    instruction temp;
    stringstream ss(line);
    ss >> temp.opcode;
    if (temp.opcode == "jmp") {
        ss >> temp.offset;
        temp.operand = ' '; // Use space to indicate no operand
    } else if (temp.opcode == "jie" || temp.opcode == "jio") {
        char comma;
        ss >> temp.operand >> comma >> temp.offset;
    } else {
        ss >> temp.operand;
        temp.offset = 0; // Default offset for non-jump instructions
    }
    return temp;
}

int executeInstructions(int size, instruction instructions[], int a = 0, int b = 0) {
    int i = 0;
    while (i < size && i >= 0) {
        if (instructions[i].opcode == "hlf") {
            if (instructions[i].operand == 'a') {
                a /= 2;
            } else if (instructions[i].operand == 'b') {
                b /= 2;
            }
            i++;
        } else if (instructions[i].opcode == "tpl") {
            if (instructions[i].operand == 'a') {
                a *= 3;
            } else if (instructions[i].operand == 'b') {
                b *= 3;
            }
            i++;
        } else if (instructions[i].opcode == "inc") {
            if (instructions[i].operand == 'a') {
                a += 1;
            } else if (instructions[i].operand == 'b') {
                b += 1;
            }
            i++;
        } else if (instructions[i].opcode == "jmp") {
            i += instructions[i].offset;
        } else if (instructions[i].opcode == "jie") {
            if (instructions[i].operand == 'a' && a % 2 == 0) {
                i += instructions[i].offset;
            } else if (instructions[i].operand == 'b' && b % 2 == 0) {
                i += instructions[i].offset;
            } else {
                i++;
            }
        } else if (instructions[i].opcode == "jio") {
            if (instructions[i].operand == 'a' && a == 1) {
                i += instructions[i].offset;
            } else if (instructions[i].operand == 'b' && b == 1) {
                i += instructions[i].offset;
            } else {
                i++;
            }
        }
    }
    return b;
}

int returnLineCount(){
    ifstream my_file("instructions.txt");
    if (!my_file.is_open()) {
        cerr << "Failed to open file" << endl;
        return 1;
    }

    // Count the lines
    int line_count = 0;
    string line;
    while (getline(my_file, line)) {
        ++line_count;
    }
    my_file.close();
    return line_count;
}

int main() {
    int line_count = returnLineCount();
    instruction* instructions = new instruction[line_count];

    ifstream my_file("instructions.txt");
    if (!my_file.is_open()) {
        cerr << "Failed to re-open file" << endl;
        delete[] instructions;
        return 1;
    }
    string line;
    for (int i = 0; i < line_count && getline(my_file, line); ++i) {
        instructions[i] = processData(line);
    }
    my_file.close();
    std::cout << "Part One: "<< executeInstructions(line_count, instructions) << endl;
    std::cout << "Part Two: "<< executeInstructions(line_count, instructions, 1, 0) << endl;

    delete[] instructions;
    return 0;
}
