#include<iostream>
using namespace std;

typedef struct coordinate{
    int x;
    int y;
}coordinate;

coordinate coordinateGenerator(coordinate current){
    coordinate next;
    if (current.x == 1 && current.y == 1) {
        next.x = 1;
        next.y = 2;
    } else if (current.y == 1) {
        next.x = 1;
        next.y = current.x + 1;
    } else {
        next.x = current.x + 1;
        next.y = current.y - 1;
    }
    return next;
}

int main(){
    coordinate current;
    current.x = 1;
    current.y = 2;
    long previous = 20151125;
    long now = 1;
    int i = 1;
    while(current.x != 3029 || current.y != 2947){
        now = (previous * 252533) % 33554393;
        previous = now;
        current = coordinateGenerator(current);
        i++;
    }
    now = (previous * 252533) % 33554393;
    cout << "Current coordinates: (" << current.x << ", " << current.y << ") - Code: " << now << endl;
    return 0;
}
