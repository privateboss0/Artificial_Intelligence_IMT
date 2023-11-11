import secrets
def prime_checker(p):
    # Checks If the number entered is a Prime Number or not
    if p < 1:
        return -1
    elif p > 1:
        if p == 2:
            return 1
        for i in range(2, p):
            if p % i == 0:
                return -1
        return 1
def primitive_check(g, p):
    # Checks If The Entered Number Is A Primitive Root Or Not
    L = []
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return -1
        return 1

#Generate a secure random prime number, I Limited this to 7000(13 prime number bits) due to local computing power. larger prime
#number bit also require more computational power to generate and use, so there is a trade-off between security and performance.
#1024 prime bits is good, 2048 is better, 4096 is best excluding quantum computational power maturity."""

while True:
    P = secrets.randbelow(7000)  
    if prime_checker(P) == -1:
        continue
    break

while True:
    G = secrets.randbelow(P - 1)  # Generate a secure random primitive root of the prime number
    if primitive_check(G, P) == -1:
        continue
    break
L = []  # Initialize the L list

x1 = secrets.randbelow(P - 1)  # Generate secure and random private keys
x2 = secrets.randbelow(P - 1)  # Generate secure and random private keys

y1, y2 = pow(G, x1) % P, pow(G, x2) % P    # Calculate Public Keys
k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P  # Generate Secret Keys

print(f"\nSecret Key For Bob Is {k1}\nSecret Key For Alice Is {k2}\n")

if k1 == k2:
    print("Keys Have Been Exchanged Successfully")
else:
    print("Keys Have Not Been Exchanged Successfully")
