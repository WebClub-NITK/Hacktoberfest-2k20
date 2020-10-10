#include<iostream>
#include<string>

using namespace std;

int main(){
    string ip_addr;
    cout << "Enter the IPv4 address: ";
    cin >> ip_addr;
    string delimiter = ":";
    string token = ip_addr.substr(0, ip_addr.find(delimiter)); 
    int ip = stoi(token);

    // Check for valid ip
    if(ip<0 || ip>255){
        cout << "Not a valid ip address";
    }
    else{
        if(ip>=0 && ip<=127){
            cout << "This is a class A IPv4 address.";
        }
        if(ip>=128 && ip<=191){
            cout << "This is a class B IPv4 address.";
        }
        if(ip>=192 && ip<=223){
            cout << "This is a class C IPv4 address.";
        }
        if(ip>=224 && ip<=239){
            cout << "This is a class D IPv4 address.";
        }
        if(ip>=240 && ip<=255){
            cout << "This is a class E IPv4 address.";
        }
    }
    return 0;

}