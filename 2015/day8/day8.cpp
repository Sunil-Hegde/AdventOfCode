#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream inputFile("instructions.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Error opening file." << std::endl;
        return 1;
    }

    std::string line;
    int totalCodeCount = 0;
    int totalMemoryCount = 0;

    while (std::getline(inputFile, line)) {
        int codeCount = line.size();

        line = line.substr(1, line.size() - 2);

        int memoryCount = 0;
        for (size_t i = 0; i < line.size(); ++i) {
            if (line[i] == '\\') {
                ++i; 
                if (line[i] == '\\' || line[i] == '\"') {
                    memoryCount += 1;
                } else if (line[i] == 'x') {
                    memoryCount += 1;
                    i += 2; 
                }
            } else {
                memoryCount += 1;
            }
        }

        totalCodeCount += codeCount;
        totalMemoryCount += memoryCount;
    }

    inputFile.close();

    int difference = totalCodeCount - totalMemoryCount;

    std::cout << "Total Code Count: " << totalCodeCount << std::endl;
    std::cout << "Total Memory Count: " << totalMemoryCount << std::endl;
    std::cout << "Difference: " << difference << std::endl;

    return 0;
}
