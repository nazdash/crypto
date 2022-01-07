# Simple RSA algorythm
#import fractions  #gcd
import math
import numpy as np
 

p1 = int(input("Choose prime number 1: ")) 
p2 = int(input("Choose prime number 2: "))
print()

#k = 2 # just defined by me
p = p1
q = p2
n = p*q
fi = (p-1)*(q-1)

# e has some requirements
i = 0
while i < 1:
  print("Choose e between 1 and", fi,"AND coprime to", fi)
  e = int(input("Enter e:"))
  print()
  if math.gcd(e,fi) != 1 or e > fi:
    print("Wrong e")
  else:
    i += 1

# it's hard to understand how to calculate this fookin "d"
#d = ((k * fi) + 1) / e
#d = e**(fi-2) % fi
d = pow(e, -1, fi)
#d = 11

print("Your public key is:", e, n)
print("Your private key is:", d, n)
print()

def encrypt(me):
    c = me**e % n
    #print(e, en, n)
    print("Encrypted Message is: ", c)
    return c

def decrypt(me):
    c = me**d % n
    #print(d, en, n)
    print("Decrypted Message is: ", c)
    return c

while 1:
  a1 = input("Do you want to encrypt or decrypt a message? (e/d): ")
  if a1.lower() == 'e':
    message = int(input("Enter the message to be encrypted: ")) 
    # print("Original Message is: ", message)
    c = encrypt(message)
    print()
  elif a1.lower() == 'd':
    message = int(input("Enter the message to be decrypted: ")) 
    # print("Original Message is: ", message)
    c = decrypt(message)
    print()
  else:
    print("Unknown command")