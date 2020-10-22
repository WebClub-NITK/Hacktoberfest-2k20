#include<bits/stdc++.h>
#include<math.h>

using namespace std;
// find gcd
int gcd(int a, int b) {
   return (a==0)?b:gcd(b%a,a);
}
int gcdExtended(int a, int b, int *x, int *y)  
{  
    // Base Case  
    if (a == 0)  
    {  
        *x = 0;*y = 1;  
        return b;  
    }  
  
    int x1, y1; // To store results of recursive call  
    int gcd1 = gcdExtended(b%a, a, &x1, &y1);  
  
    // Update x and y using results of  
    // recursive call  
    *x = y1 - (b/a) * x1;  
    *y = x1;  
  
    return gcd1;  
} 

int power(int x, unsigned int y, int p)  // to calculate x^y%p;
{  
    int res = 1;     // Initialize result  
  
    x = x % p; // Update x if it is more than or  
                // equal to p 
   
    if (x == 0) return 0; // In case x is divisible by p; 
  
    while (y > 0)  
    {  
        // If y is odd, multiply x with result  
        if (y & 1)  
            res = (res*x) % p;  
  
        // y must be even now  
        y = y>>1; // y = y/2  
        x = (x*x) % p;  
    }  
    return res;  
}


int main() {
   //2 random prime numbers
   srand(time(0));
   double p = 13;
   double q = 11;
   double n=p*q;//calculate n
   double track;
   //phi is the no of coprimes less than n
   double phi= (p-1)*(q-1);//calculate phi
   //public key
   //e stands for encryption key
   double e=7;
   //for checking that 1 < e < phi(n) and gcd(e, phi(n)) = 1; i.e., e and phi(n) are coprime.
   while(e<phi) {
      track = gcd(e,phi);
      if(track==1)
         break;
      else
         e++;
   }
   //private key
   //d stands for decryption key
   //choosing d such that it satisfies d*e = 1 mod phi
   //choosing d such that, d is modular multiplicative inverse of e w.r.t phi
   //i.e ed is congruent to 1 with respect to the modulus .
   int x=0,y=0;
   int gcd=gcdExtended(e,phi,&x,&y);
   double d=(int)(x+phi)%(int)phi;
   double message =rand()%(int)n;
   double c = power(message,e,n); //encrypt the Message.
   double m = power(c,d,n);       // Decrypt the Message.

   cout<<"Original Message = "<<message<<"\n";
   cout<<"Encrypted message = "<<c<<"\n";
   cout<<"Decrypted message = "<<m<<"\n";
   cout<<"Message==Decrypted: ";bool b=(message==m) ? true:false;cout<<b<<"\n";
   return 0;
}