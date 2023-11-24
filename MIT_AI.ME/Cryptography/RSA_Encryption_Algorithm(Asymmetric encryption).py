# This program encrypts and decrypts messages using RSA encryption or (Asymmetric encryption).
# To use the program, simply run it and enter your message when prompted.
# The program will then generate a public and private key pair. The public
# key will be used to encrypt the message, and the private key will be used
# to decrypt it. Once the message is encrypted, you can share it with anyone.
# To decrypt the message, the receiver will need to have the private key...

import math
from math import gcd
import secrets
import sys

def encodeMessage(msg):
    encodedMsg = 0

    for char in msg:
        encodedMsg = encodedMsg << 8
        encodedMsg = encodedMsg ^ ord(char)
    return encodedMsg

def getSecretsPrime(primeSize):
    x = secrets.randbelow((1 << primeSize) - 1)
    while not (isPrime(x)):
        x = secrets.randbelow((1 << primeSize) - 1) 
    return x
    
def isPrime(n):
    if n % 2 == 0:
        return False

    for i in range(1, 40):
        a = secrets.randbelow(n - 1)
        if isComposite(a, n):
            return False
    return True

def isComposite(a, n):
    
    t,d = decompose(n - 1)
    x = pow(a, d, n)
    
    if x == 1 or x == n - 1:
        return False

    for i in range(1, t):
        x0 = x;
        x = pow(x0, 2, n)
        if x == 1 and x0 != 1 and x0 != n - 1:
            return True
    if x != 1:
        return True
        
    return False

def decompose(n):
    i = 0
    while n & (1 << i) == 0:
        i += 1
    return i, n >> i

def getKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    for i in range(2, phi):
        if gcd(phi, i) == 1:
            e = i
            break
         
    d = multiplicativeInverse(e, phi)
    
    return n, e, d
def multiplicativeInverse(e, phi):
    return extendedEuclid(e, phi)[1] % phi

def extendedEuclid(a, b):
    if b == 0:
        return a, 1, 0
    else: 
        d2, x2, y2 = extendedEuclid(b, a % b)
        d, x, y = d2, y2, x2 - (a // b) * y2
        return d, x, y
try:
    modulusSize = int(sys.argv[1])
        
except:
    modulusSize = 2048  #4096 modulus size was used too but message encryption and decryption was about 9minutes due to local computational resources

msg = (input('Type your secure message and press Enter: '))

primeSize = modulusSize // 2
p = getSecretsPrime(primeSize)
q = getSecretsPrime(primeSize)
while p == q:
    q = getSecretsPrime(primeSize)

n, e, d = getKeys(p, q)

encodedMsg = encodeMessage(msg)
encryptedMsg = pow(encodedMsg, e, n)
decryptedMsg = pow(encryptedMsg, d, n)

print("Public key (e, n):")
print("\te = ", e)
print("\tn = ", n)
print("\nPrivate key (d, n):")
print("\td = ", d)
print("\tn = ", n)
print("\nOriginal message string:\n\t", msg)
print("\nInteger encoded message:\n\t", encodedMsg)
print("\nEncrypted message( C(M) = M^e % n ):\n\t", encryptedMsg)
print("\nDecrypted message( M(C) = C^d % n ):\n\t", decryptedMsg)
if encodedMsg == decryptedMsg:
    print("Secured message from sender: ", msg)
    #print("Secured message from sender: ", decryptedMsg)
    #print("\nSecure message transmitted!. Decrypted message and original Encoded message is a match")
