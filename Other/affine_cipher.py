# Program to Encrypt and Decrypt Affine Cipher
# Programmed by : Aravindha Hariharan M

message = input("Enter the Text to be Encrpyted: ")
a,b = [int(i) for i in input("Enter the Key value: ").split(",")]
def egcd(a,b):
  x,y,u,v=0,1,1,0
  while a!=0:
    q,r=b//a,b%a
    m,n=x-u*q,y-v*q
    b,a,x,y,u,v=a,r,u,v,m,n
  gcd=b
  return gcd,x,y

def modinv(a, m):
  gcd, x, y = egcd(a, m)
  if gcd != 1:
      return None
  else:
      return x % m

cipher_text=""
for i in message:
  cipher_text+=chr((a* (ord(i)-ord("A")) + b )%26+ord("A"))

print("Cipher Text : "+cipher_text)

decrypted_text=""
for i in cipher_text:
  decrypted_text+=chr(modinv(a, 26)*(ord(i) - ord('A') - b)% 26+ ord('A'))

print("Decrypted Message: "+decrypted_text)