#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int giftsCalculatorPartOne(int number) {
    int sum = 0;
    int squareRoot = sqrt(number);
    for (int i = 1; i <= squareRoot; i++) {
        if (number % i == 0) {
            sum += i * 10;
            if (i != number / i) {
                sum += (number / i) * 10;
            }
        }
    }
    return sum;
}

int giftsCalculatorPartTwo(int number, vector<int>& elves) {
    int sum = 0;
    int squareRoot = sqrt(number);
    for (int i = 1; i <= squareRoot; i++) {
        if (number % i == 0) {
            if (elves[i] < 50) {
                sum += i * 11;
                elves[i]++;
            }
            int floorValue = number / i;
            if (i != floorValue && elves[floorValue] < 50) {
                sum += floorValue * 11;
                elves[floorValue]++;
            }
        }
    }
    return sum;
}

int findHousePartOne(int targetGifts) {
    int houseNumber = 1;
    while (true) {
        int giftsPerHouse = giftsCalculatorPartOne(houseNumber);
        if (giftsPerHouse >= targetGifts) {
            break;
        }
        houseNumber++;
    }
    return houseNumber;
}

int findHousePartTwo(int targetGifts) {
    int houseNumber = 1;
    vector<int> elves(targetGifts + 1, 0);  
    while (true) {
        int giftsPerHouse = giftsCalculatorPartTwo(houseNumber, elves);
        if (giftsPerHouse >= targetGifts) {
            break;
        }
        houseNumber++;
    }
    return houseNumber;
}

int main() {
    int number = 36000000;
    cout << "Part One: " << findHousePartOne(number) << endl;
    cout << "Part Two: " << findHousePartTwo(number) << endl;
    return 0;
}
