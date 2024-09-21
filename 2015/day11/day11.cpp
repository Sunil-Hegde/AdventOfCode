#include<iostream>
#include<stdlib.h>
using namespace std;

bool checkTriplets(string str){
    int i = 0;
    while(str[i] != '\0' && str[i+1] != '\0' && str[i+2] != '\0'){
        if(str[i+1] == str[i] + 1 && str[i+2] == str[i] + 2){
            return true;
        } else {
            i++;
        }
    }
    return false;
}

bool checkDoubles(string str){
    int count = 0;
    int i = 0;
    while(str[i] != '\0' && str[i+1] != '\0'){
        if(str[i] == 'i' || str[i] == 'o' || str[i] == 'l'){
            return false;
        } else if((str[i] == str[i+1]) && str[i+1] != str[i+2]){
            count++;
        }
        i++;
    }
    return (count >= 2) ? true : false;
}

string generatePassword(string str) {
    int size = str.size();
    bool i = true;
    while (i) {
        if (checkDoubles(str) && checkTriplets(str)) {
            i = false;
        } else {
            int index = size - 1;
            while (index >= 0 && str[index] == 'z') {
                str[index] = 'a';
                index--;
            }
            if (index >= 0)
                str[index]++;
            else
                str.insert(0, "a");
        }
    }
    return str;
}

int main(){
    string str = "hepxcrrq";
    string passwordPartOne = generatePassword(str);
    cout<<"Part One: " <<passwordPartOne<<endl;
    string str1 = "hepxxzaa";
    string passwordPartTwo = generatePassword(str1);
    cout<<"Part Two: " <<passwordPartTwo<<endl;
    return 0;
}
