#include <bits/stdc++.h> 
using namespace std; 

struct Position
{ 
	int a, b; 
}; 

bool checkOverlap(Position l1, Position r1, Position l2, Position r2) 
{ 
	 
	if (l1.a >= r2.a || l2.a >= r1.a) 
		return false; 

	
	if (l1.b <= r2.b || l2.b <= r1.b) 
		return false; 

	return true; 
} 


int main() 
{ 
	
	Position l1;
	Position r1;
	Position l2;
	Position r2;
	cout<<"Enter the top left Co-ordinates of the First Rectangle "<<endl;
	 cin>>l1.a;
	 cin>>l1.b;
	cout<<"Enter the top left Co-ordinates of the second Rectangle "<<endl;
	 cin>>l2.a;
	 cin>>l2.b;
	cout<<"Enter the bottom right Co-ordinates of the First Rectangle "<<endl;
	 cin>>r1.a;
	 cin>>r1.b;
	cout<<"Enter the bottom right Co-ordinates of the second Rectangle "<<endl;
	 cin>>r2.a;
	 cin>>r2.b;
	 
	 

	if (checkOverlap(l1, r1, l2, r2)) 
		printf("Rectangles Overlap"); 
	else
		printf("Rectangles Don't Overlap"); 
	return 0; 
}
