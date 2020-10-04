"""Simple implementation of RSA algorithm."""


def egcd(a: int, b: int) -> int:
    """Euclidian algorithm to compute GCD."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def mod_inv(a: int, m: int) -> int:
    """Compute modulo inverse of a under m."""
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f'No modular inverse for {a} under {m}.')
    else:
        return x % m


class RSA:
    """Simple implementation of RSA."""

    def __init__(self, p: int, q: int, e: int):
        """Generate keys.

        p and q must be prime, e must be prime with and less than (p - 1)(q - 1).
        """
        self.n = p * q
        self.e = e
        phi = (p - 1) * (q - 1)
        self.d = mod_inv(e, phi)

    def encrypt(self, message: int) -> int:
        """Encrypt a message.

        The message must be less than n.
        """
        return (message ** self.e) % self.n

    def decrypt(self, encrypted: int) -> int:
        """Decrypt an encrypted message."""
        return (encrypted ** self.d) % self.n


# EXAMPLE

p, q = 61, 53  # p and q are primes.
e = 17  # e is prime with (p - 1)(q - 1).
rsa = RSA(p, q, e)

message = 65  # Message is less than p * q.
print(f'Message: {message}')

encrypted = rsa.encrypt(message)
print(f'Encrypted: {encrypted}')

decrypted = rsa.decrypt(encrypted)
print(f'Decrypted: {decrypted}')

print(f'Message == Decrypted: {message == decrypted}')
