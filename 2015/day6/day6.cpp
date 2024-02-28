#include <iostream>
using namespace std;

int main() {
    int a = 1000, b = 1000, c = 5, d = 2;
    int array[a][b][c][d] = {0};
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            for (int k = 0; k < c; k++) {
                switch (k) {
                    case 0:
                        array[i][j][k][0] = i;
                        array[i][j][k][1] = j;
                        break;
                    case 1:
                        array[i][j][k][0] = i;
                        array[i][j][k][1] = 9 - j;
                        break;
                    case 2:
                        array[i][j][k][0] = 9 - i;
                        array[i][j][k][1] = j;
                        break;
                    case 3:
                        array[i][j][k][0] = 9 - i;
                        array[i][j][k][1] = 9 - j;
                        break;
                    default:
                        break;
                }
            }
        }
    }
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            cout << "[";
            for (int k = 0; k < c; k++) {
                for (int l = 0; l < d; l++) {
                    if (l == 0) {
                        cout << "[" << array[i][j][k][l] << ",";
                    } else if (l == 1) {
                        cout << array[i][j][k][l] << "]";
                    }
                }
                if (k != c - 1) {
                    cout << "] , ";
                } else if (k == c - 1) {
                    cout << "]";
                }
            }
            cout << "] ";
        }
        cout << endl;
    }

    return 0;
}
