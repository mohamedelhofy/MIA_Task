#include <bits/stdc++.h>
using namespace std;
int main(){
    int x=0;
    int &y=x;
    cout<< y<<endl;
    x=8;
    cout<< y<<endl;
    y=9;
    cout<< x<<endl;
    return 0;
}