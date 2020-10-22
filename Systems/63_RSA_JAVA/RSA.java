import java.util.Random;
import java.math.BigInteger;
import java.security.SecureRandom;

class RSA_algorithm
{
	//this is the e parameter after calculations
	private BigInteger publicKey;
	
	//this is the d parameter after the calculations
	private BigInteger privateKey;
	
	//this is n=p*q
	private BigInteger n;
	
	//we need random number generator
	private SecureRandom random;
	
	public RSA_algorithm()
	{
		this.random = new SecureRandom();
	}
	
	public BigInteger encryptMessage(BigInteger message)
	{
		return encrypt(this.publicKey, this.n, message);
	}
	
	public BigInteger decryptMessage(BigInteger cipherText)
	{
		return decrypt(this.privateKey, this.n, cipherText);
	}
	
	private BigInteger decrypt(BigInteger d, BigInteger n, BigInteger cipherText)
	{
		//we use modular exponentiation in decryption as well: cipher^d mod n
		BigInteger messageInt = cipherText.modPow(d, n);
        return messageInt;
	}
	
	//the cipher text will be a huge integer
	private BigInteger encrypt(BigInteger e, BigInteger n, BigInteger message)
	{
        BigInteger messageInt = message;
		
		//we have to use modular exponentiation message^e mod n is the cipher text
		return messageInt.modPow(e, n);
	}
	
	public void generateKeys(int keyDigits)
	{
		//p is large prime number
		BigInteger p = BigInteger.probablePrime(keyDigits, random);
		
		//q is a large prime number
		BigInteger q = BigInteger.probablePrime(keyDigits, random);
		
		//n=p*q this is the trap-door function
		this.n = p.multiply(q);
		
		//Euler's totient phi function
		BigInteger phi = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));
		
		//e<phi is comprime to phi so gcd(e, phi) = 1
		BigInteger e = generatePublicFactor(phi);
		
		//d is the modular inverse of e (with mod phi)
		BigInteger d = e.modInverse(phi);
		
		this.privateKey = d;
		this.publicKey = e;
	}
	
	//this is how we calculate the e parameter
	private BigInteger generatePublicFactor(BigInteger phi)
	{
		BigInteger e = new BigInteger(phi.bitLength(), this.random);
		
		//we, after a coprime where gcd(e, phi) = 1, are iterating
		while(!e.gcd(phi).equals(BigInteger.ONE))
			e = new BigInteger(phi.bitLength(), this.random);
		
		return e;
	}
}

public class RSA
{
	public static void main(String args[])
	{
		RSA_algorithm rsa = new RSA_algorithm();
		rsa.generateKeys(1024);
		
		//we are generating a random big integer in range [25000000000, 5000000000000]
        BigInteger maxLimit = new BigInteger("5000000000000");
        BigInteger minLimit = new BigInteger("25000000000");
        BigInteger bigInteger = maxLimit.subtract(minLimit);
        Random randNum = new Random();
        int len = maxLimit.bitLength();
		
        BigInteger originalMessage = new BigInteger(len, randNum);
        if (originalMessage.compareTo(minLimit) < 0)
            originalMessage = originalMessage.add(minLimit);
        if (originalMessage.compareTo(bigInteger) >= 0)
            originalMessage = originalMessage.mod(bigInteger).add(minLimit);
        
		System.out.println("\nEncrypted message by Alice: " + originalMessage);
		BigInteger cipher = rsa.encryptMessage(originalMessage);
		System.out.println("\nCipher text: " + cipher);
		System.out.println("\nDecrypted message by Bob: " + rsa.decryptMessage(cipher));
	}
}