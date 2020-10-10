// C program to determine class
#include<stdio.h> 
#include<string.h>
#include<regex.h> 

char findClass(char str[]) 
{
	char arr[4]; 
	int i = 0; 
	while (str[i] != '.') 
	{ 
		arr[i] = str[i]; 
		i++; 
	} 
	i--; 

	int ip = 0, j = 1; 
	while (i >= 0) 
	{ 
		ip = ip + (str[i] - '0') * j; 
		j = j * 10; 
		i--; 
	} 

	// Class A 
	if (ip >=1 && ip <= 126) 
		return 'A'; 

	// Class B 
	else if (ip >= 128 && ip <= 191) 
		return 'B'; 

	// Class C 
	else if (ip >= 192 && ip <= 223) 
		return 'C'; 

	// Class D 
	else if (ip >= 224 && ip <= 239) 
		return 'D'; 

	// Class E 
	else
		return 'E'; 
}

int main() 
{ 
    printf("Enter the IPv4 address: ");
	char servIP[100];
	scanf("%s",servIP);
	regex_t regex;
    regcomp(&regex,"(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])", REG_EXTENDED);
    int regres = regexec(&regex, servIP, 0, NULL, 0);
    if(regres == 0) {
    	char ipClass = findClass(servIP); 
	    printf("This is a class %c IPv4 address.\n", ipClass);
    } else {
        printf("Invalid IP address");
    }
	return 0; 
} 
