#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#define gridSize 100
using namespace std;

int processedData[gridSize][gridSize];
int tempData[gridSize][gridSize];
int nextGrid[gridSize][gridSize];

void processData(string line, int i){
    for (int j = 0; j < line.length(); j++){
        if (line[j] == '#'){
            processedData[i][j] = 1;
        } else if (line[j] == '.'){
            processedData[i][j] = 0;
        } 
    }
}

void animatePartOne(int array[gridSize][gridSize]) {
    int directions[8][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridSize; j++) {
            int lightsOn = 0;

            for (int k = 0; k < 8; k++) {
                int ni = i + directions[k][0];
                int nj = j + directions[k][1];
                if (ni >= 0 && ni < gridSize && nj >= 0 && nj < gridSize && array[ni][nj] == 1) {
                    lightsOn++;
                }
            }

            if ((array[i][j] == 1 && (lightsOn == 2 || lightsOn == 3)) || (array[i][j] == 0 && lightsOn == 3)) {
                nextGrid[i][j] = 1;
            } else {
                nextGrid[i][j] = 0;
            }
        }
    }
    for (int i = 0;i < 100; i++){
        for (int j = 0; j < 100; j++){
            tempData[i][j] = nextGrid[i][j];
        }
    }
}

void animatePartTwo(int array[gridSize][gridSize]) {
    int directions[8][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridSize; j++) {
            int lightsOn = 0;

            for (int k = 0; k < 8; k++) {
                int ni = i + directions[k][0];
                int nj = j + directions[k][1];
                if (ni >= 0 && ni < gridSize && nj >= 0 && nj < gridSize && array[ni][nj] == 1) {
                    lightsOn++;
                }
            }

            if ((array[i][j] == 1 && (lightsOn == 2 || lightsOn == 3)) || (array[i][j] == 0 && lightsOn == 3)) {
                nextGrid[i][j] = 1;
            } else {
                nextGrid[i][j] = 0;
            }
        }
    }

    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridSize; j++) {
            tempData[i][j] = nextGrid[i][j];
        }
    }
    tempData[0][0] = 1;
    tempData[0][99] = 1;
    tempData[99][0] = 1;
    tempData[99][99] = 1;
}



int count(int array[gridSize][gridSize]){
    int total = 0;
    for (int i = 0;i < 100; i++){
        for (int j = 0; j < 100; j++){
            if (array[i][j] == 1){
                total++;
            }
        }
    }
    return total;
}

void executePartOne(){
    ifstream my_file("input.txt");
    if(!my_file) {
        cout << "Error: Unable to open the file." << endl;
        return;
    }
    string line;
    int i = 0;
    while (!my_file.eof()) {
        getline(my_file, line);
        processData(line, i);
        i++;
    }
    my_file.close();

    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            tempData[i][j] = processedData[i][j];
        }
    }
    for (int i = 0; i < 100; i++) {
        animatePartOne(tempData);
    }
    int total = count(nextGrid);
    cout << "Part One: " << total << endl;
}

void executePartTwo(){
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            tempData[i][j] = processedData[i][j];
        }
    }
    for (int i = 0; i < 100; i++) {
        animatePartTwo(tempData);
    }
    int total = count(nextGrid);
    cout << "Part Two: " << total << endl;
}
int main(){
    executePartOne();
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            tempData[i][j] = 0;
            nextGrid[i][j] = 0;
        }
    }
    executePartTwo();
    return 0;
}
