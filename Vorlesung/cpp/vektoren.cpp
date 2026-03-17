#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> v1 ={0,1,2,3,4,5,6,7,8,9};

/*
    cout << v1[0]<< "," <<v1[4]<< endl;

for (auto& x: v1){
    cout << x << endl;
}*/
for (int i =0; i<10; i++){
    cout << v1[i]<<"|";
}
cout<< endl;
    return 0;
}