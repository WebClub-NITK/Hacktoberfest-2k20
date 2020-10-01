 #include<bits/stdc++.h>
 using namespace std;
 bool isValid(string s) {
        int n=s.length(), i=0, digits=0, dots=0;
        
        for(;i<n && isspace(s[i]); i++);
        
        if(i<n && s[i]=='+' || s[i]=='-')
        ++i;
        
        for(;i<n && isdigit(s[i]) || s[i]=='.' ; i++)
        {
            if(isdigit(s[i]))
            ++digits;
            
            else if(++dots>1)
                return 0;
        }
        
        if(!digits)
        return 0;
        
        if(s[i]=='e')
        {
            ++i;
            if(s[i]=='+' || s[i]=='-')
            ++i;
            
            digits=0;
            for(;i<n && isdigit(s[i]) ; i++)
            ++digits;
            
            if(!digits)
            return 0;
        }
        
        for(;i<n && isspace(s[i]); i++);
        
        return i==n;
    }

int main(){
    string s;
    cin>>s;
    if(isValid(s))cout<<"true";
    else cout<<"false";
    return 0;
}