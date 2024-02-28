#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
    const int gridSize = 1000;
    vector<int> lights(gridSize * gridSize, 0);  // Initialize all lights to off

    ifstream inputFile("instructions.txt");  // Replace "instructions.txt" with your input file name
    string line;

    while (getline(inputFile, line)) {
        stringstream ss(line);
        string command;
        ss >> command;

        int x1, y1, x2, y2;
        char dummy; // To handle "through" keyword
        ss >> x1 >> y1 >> dummy >> x2 >> y2;

        for (int i = x1; i <= x2; ++i) {
            for (int j = y1; j <= y2; ++j) {
                int index = i * gridSize + j;
                if (command == "toggle") {
                    lights[index] = 1 - lights[index]; // Toggle the lights
                } else if (command == "on") {
                    lights[index] = 1; // Turn on the lights
                } else if (command == "off") {
                    lights[index] = 0; // Turn off the lights
                }
            }
        }
    }

    // Count the number of lit lights
    int litCount = 0;
    for (int light : lights) {
        litCount += light;
    }

    cout << "Number of lit lights: " << litCount << endl;

    return 0;
}
