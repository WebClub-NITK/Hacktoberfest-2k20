ip = list(map(int, input("Enter the IPv4 Address: ").split(".")))

def findClass():
	if ip[0] >= 1 and ip[0] <= 126:
		return 'A'
	if ip[0] >= 128 and ip[0] <= 191:
		return 'B'
	if ip[0] >= 192 and ip[0] <= 223:
		return 'C'
	if ip[0] >= 224 and ip[0] <= 239:
		return 'D'
	if ip[0] >= 240 and ip[0] <= 255:
		return 'E'

print("This is a class %s IPv4 address."%findClass())
