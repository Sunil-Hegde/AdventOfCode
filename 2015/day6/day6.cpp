    #include <iostream>
    #include <string>
    #include <sstream>
    #include <fstream>
    #include<stdlib.h>
    #define gridSize 1000
    using namespace std;
    typedef struct instr{
        string instruction;
        int x0, x1, y0, y1;
        struct instr *next;
    }instr;

    instr *processLine(instr *head, string line) {
        instr *newNode = new instr(); 
        newNode->next = nullptr; 
        string temp;
        char s;
        stringstream ss(line);
        ss >> newNode->instruction >> newNode->x0 >> s >> newNode->x1 >> temp >> newNode->y0 >> s >> newNode->y1;
        if (head == nullptr) { 
            head = newNode;
        } else {
            instr *tempNode = head;
            while (tempNode->next != nullptr) { 
                tempNode = tempNode->next;
            }
            tempNode->next = newNode; 
        }
        return head;
    }

    void traversal(instr *head){
        while(head != NULL){
            cout << head->instruction << " " << head->x0 << " " << head->x1 << " " << head->y0 << " " << head->y1 << endl;
            head = head->next;
        }
    }

    int lightsPartOne(int lights[gridSize][gridSize], instr *head){
        while(head != NULL){
            if (head->instruction == "turnon"){
                for(int i = head->x0;i<=head->y0;i++){
                    for(int j = head->x1;j<=head->y1;j++){
                        lights[i][j] = 1;
                    }
                }
            } else if (head->instruction == "turnoff"){
                for(int i = head->x0;i<=head->y0;i++){
                    for(int j = head->x1;j<=head->y1;j++){
                        lights[i][j] = 0;
                    }
                }
            } else if (head->instruction == "toggle"){
                for(int i = head->x0;i<=head->y0;i++){
                    for(int j = head->x1;j<=head->y1;j++){
                        if (lights[i][j] == 0)
                            lights[i][j] = 1;
                        else if (lights[i][j] == 1)
                            lights[i][j] = 0;
                    }
                }
            }
            head = head->next;
        }
        int count = 0;
        for (int i = 0; i < gridSize; i++){
            for(int j = 0; j<gridSize; j++){
                if(lights[i][j] == 1){
                    count+=1;
                }
            }
        }
        return count;
    }

    int lightsPartTwo(int lights[gridSize][gridSize], instr *head) {
    while (head != NULL) {
        if (head->instruction == "turnon") {
            for (int i = head->x0; i <= head->y0; i++) {
                for (int j = head->x1; j <= head->y1; j++) {
                    lights[i][j] += 1;
                }
            }
        } else if (head->instruction == "turnoff") {
            for (int i = head->x0; i <= head->y0; i++) {
                for (int j = head->x1; j <= head->y1; j++) {
                    if (lights[i][j] > 0){
                        lights[i][j] -= 1;
                    }
                }
            }
        } else if (head->instruction == "toggle") {
            for (int i = head->x0; i <= head->y0; i++) {
                for (int j = head->x1; j <= head->y1; j++) {
                    lights[i][j] += 2;
                }
            }
        }
        head = head->next;
    }

    int totalBrightness = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridSize; j++) {
            totalBrightness += lights[i][j];
        }
    }

    return totalBrightness;
}

int main() {
    ifstream my_file("instruction1.txt");
    if(!my_file) {
        cout << "Error: Unable to open the file." << endl;
        return 1; 
    }
    string line;
    instr *head = NULL;
    while (!my_file.eof()) {
        getline(my_file, line);
        head = processLine(head, line);
    }
    my_file.close();

    int lights[gridSize][gridSize] = {0};
    int count1 = lightsPartOne(lights, head);
    cout<<"Part One: "<<count1<<endl;
    int count2 = lightsPartTwo(lights, head);
    cout<<"Part Two: "<<count2<<endl;
    return 0;
}
