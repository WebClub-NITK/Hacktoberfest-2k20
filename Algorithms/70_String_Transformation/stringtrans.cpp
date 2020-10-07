 
#include<bits/stdc++.h> 
using namespace std; 
  

int minimumOps(string& A, string& B) 
{ 
    int m = A.length(), n = B.length(); 
  
    
    if (n != m) 
       return -1; 
    int count[256]; 
    memset(count, 0, sizeof(count));
    int res = 0; 
    for (int i=n-1, j=n-1; i>=0; ) 
    { 
        
        while (i>=0 && A[i] != B[j]) 
        { 
            i--; 
            res++; 
        } 
  
        
        if (i >= 0) 
        { 
            i--; 
            j--; 
        } 
    } 
    return res; 
} 
  

int main() 
{ 
    string A ; 
    string B ;
    getline(cin,A);
    getline(cin,B);
    cout << "Minimum operations required is " << minimumOps(A, B); 
    return 0; 
} 
