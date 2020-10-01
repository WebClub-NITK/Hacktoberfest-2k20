// Title: Decrypt affine cypher
// Algorithm:
	// D ( x ) = a^-1 ( x - b ) mod m
	// a^-1 : modular multiplicative inverse of a modulo m. i.e., it satisfies the equation
	// 1 = a a^-1 mod m .
#include<bits/stdc++.h> 
using namespace std; 

string decrypt_cipher(string cipher,int a,int b){
	// priginal messgae
	string msg = ""; 
	int a_inv = 0; 
	int flag = 0;
	int m = cipher.length();
	//Find a^-1 (the multiplicative inverse of a in the group of integers modulo m.) 
	for (int i = 0; i < 26; i++) { 
		flag = (a * i) % 26;
		//Check if (a*i)%26 == 1, then i will be the multiplicative inverse of a 
		if (flag == 1) { 
			a_inv = i;
		} 
	} 
	for (int i = 0; i < cipher.length(); i++) { 
		if(cipher[i]!=' '){
			/*Applying decryption formula a^-1 ( x - b ) mod m {here x is cipher[i]} and added 'A' 
			to bring it in range of ASCII alphabet[ 65-90 | A-Z ] */
			msg = msg +	(char) (((a_inv * ((cipher[i]+'A' - b)) % 26)) + 'A'); 
		}
		else{
			//else simply append space characte 
			msg += cipher[i];
		}
	} 
	return msg; 
}

// testing 
int main{ 
	string decrypted;
	cout<<"Enter decrypted output to encrypt: "<<endl;
	cin>>decrypted;
	int a,b;
	cout<<"Enter A and B:"<<endl;
	cin>>a>>b;
	cout << "Decrypted Message is: " << decrypt_cipher(decrypted,a,b); 
	return 0; 
} 