#include <bits/stdc++.h>
using namespace std;
const int MAX=100;
struct Course{
    string name;
    int credit;
    float score;
    float grade;
};

struct Student {
    string name;
    int id;
    int NOC; // number of course
    Course course[MAX];
    float gpa;
};
void printSTD( Student std){
    cout << "name" << std.name << endl;
    cout << "id" << std.id << endl;
    cout << "NOC" << std.NOC << endl;
    for(int i=0;i<std.NOC;i++){
        cout << "Course("<< i+1<<") ";
        cout << std.course[i].name<<endl<<std.course[i].credit<<endl<<std.course[i].score<<endl;
    }
}
int main(){
    Student std;
    cout << "Enter name of stundent: ";
    getline(cin,std.name);
    cout << "Enter id of stundent: ";
    cin >> std.id;
    cout << "Enter num of course: ";
    cin >> std.NOC;  
    for(int i=0;i<std.NOC;i++){
        cout << "Enter Course("<< i+1<<") name  ";
        cin.ignore();
        getline(cin,std.course[i].name);
        cout << "Enter Course("<< i+1<<") credit  ";
        cin >> std.course[i].credit;
        cout << "Enter Course("<< i+1<<") score  ";
        cin >> std.course[i].score; 
    }
    printSTD(std);
    return 0;
}