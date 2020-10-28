
#include <bits/stdc++.h> 

using namespace std;
 
#define R 2
#define C 3 

void modify(bool matx[R][C]) 
{ 
	bool row[R]; 
	bool col[C]; 

	int i, j; 
	
	
	for (i = 0; i < R; i++) 
	{ 
	row[i] = 1; 
	} 

	for (i = 0; i < C; i++) 
	{ 
	col[i] = 1; 
	} 

	
	for (i = 0; i < R; i++) 
	{ 
		for (j = 0; j < C; j++) 
		{ 
			if (matx[i][j] == 0) 
			{ 
				row[i] = 0; 
				col[j] = 0; 
			} 
		} 
	} 

	
	for (i = 0; i < R; i++) 
	{ 
		for (j = 0; j < C; j++) 
		{ 
			if ( row[i] == 0 || col[j] == 0 ) 
			{ 
				matx[i][j] = 0; 
			} 
		} 
	} 
} 


void printMatrix(bool matx[R][C]) 
{ 
	int i, j; 
	for (i = 0; i < R; i++) 
	{ 
		for (j = 0; j < C; j++) 
		{ 
			cout << matx[i][j]; 
		} 
		cout << endl; 
	} 
} 

// Main Code 
int main() 
{ 
bool matx[R][C] = { { 1, 1, 1}, 
					{1, 1, 0}, 
					}; 

	cout << "The Original Matrix \n"; 
	printMatrix(matx); 

	modify(matx); 

	printf("Final Matrix \n"); 
	printMatrix(matx); 

	return 0; 
} 

