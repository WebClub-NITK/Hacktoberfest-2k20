'''
Assuming classful addressing, given an IPv4 address, find its address class. 
If the entered IP address is invalid, your program should output an appropriate 
error message. Please follow the Input / Output format as shown below:

Example:
Enter the IPv4 address: 194.200.20.55
This is a class C IPv4 address.

resource: https://www.geeksforgeeks.org/introduction-of-classful-ip-addressing/
'''

print('Enter the IPV4 address: ', end='')
ip_address = input()

print()

ip_address.split('.')
# To break each octect of the ip address
bit0 = int(ip_address.split('.')[0])
bit1 = int(ip_address.split('.')[1])
bit2 = int(ip_address.split('.')[2])
bit3 = int(ip_address.split('.')[3])

# Add extra condition in case someone put a value greater than 255 in other bits
if (bit0 >= 0 and bit0 <= 127):
	print('This is a class A IPv4 address.')
elif ((bit0 >= 127 and bit0 <= 191) and (bit1 >= 0 and bit1 <= 255)):
	print('This is a class B IPv4 address.')
elif ((bit0 >= 192 and bit0 <= 223) and (bit1 >= 0 and bit1 <= 255) 
	and (bit2 >= 0 and bit2 <= 255)):
	print('This is a class C IPv4 address.')
elif ((bit0 >= 224 and bit0 <= 239) and (bit1 >= 0 and bit1 <= 255) 
	and (bit2 >= 0 and bit2 <= 255) and (bit3 >= 0 and bit3 <= 255)):
	print('This is a class D IPv4 address.')
elif ((bit0 >= 240 and bit0 <= 255) and (bit1 >= 0 and bit1 <= 255) 
	and (bit2 >= 0 and bit2 <= 255) and (bit3 >= 0 and bit3 <= 254)):
	print('This is a class E IPv4 address.')	
else:
	print('Invalid IP address')




