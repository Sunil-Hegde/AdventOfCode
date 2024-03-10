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
    int totalEncodedCount = 0;

    while (std::getline(inputFile, line)) {
        int codeCount = line.size();
        std::string encodedString = "\"";
        for (char c : line) {
            if (c == '\\' || c == '\"') {
                encodedString += '\\';
            }
            encodedString += c;
        }
        encodedString += "\"";

        int encodedCount = encodedString.size();
        totalCodeCount += codeCount;
        totalEncodedCount += encodedCount;
    }

    inputFile.close();

    int difference = totalEncodedCount - totalCodeCount;

    std::cout << "Total Code Count: " << totalCodeCount << std::endl;
    std::cout << "Total Encoded Count: " << totalEncodedCount << std::endl;
    std::cout << "Difference: " << difference << std::endl;

    return 0;
}
