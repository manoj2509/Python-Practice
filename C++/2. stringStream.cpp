#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    stringstream ss;
   // Complete this function
    vector <int> v;
    int a;
    char ch;
    int i = 0;
    ss << str;
    while(ss != '\0')   {
        ss >> a;
        ss >> ch;
        v.push_back(a);
        i++;
    }
    return v;
    
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}

