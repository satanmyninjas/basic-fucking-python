"""
==================================================
BASIC/BARE-BONES IMPLEMENTATION OF RSA ENCRYPTION:
==================================================

1. n = pq, p =! q are primes.
2. Compute the phi(n).
3. Choose an integer 1 < e < phi(n), where e is relatively prime to totient(n).
4. Compute d = e^-1 modulo phi(n)

n and e represent your public key, and d is your private key.
x is your message that you want to send.
b is your encrypted text.

Your plaintext should be an integer 0 <= x < n.
The cipher-text can be computed as b = x^e modulo n.
Recover the plaintext: x = b^d = (x^e)^d = x^ed modulo n.

Exponentiation / logarithms are used to recover the plaintext.
"""


from math import gcd, log


def prime_finder(p):
    pass


def phi(x):
    amount = 0
    for k in range(1, x + 1):
        if gcd(x, k) == 1:
            amount += 1
    return amount


def encrypt(message):
    pass


def decrypt(cipher):
    pass
