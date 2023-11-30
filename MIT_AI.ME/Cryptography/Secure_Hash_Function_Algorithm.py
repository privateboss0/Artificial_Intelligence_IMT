""" This program takes an input and performs a one way hash function to ensure integrity using the 
latest standard of the algorithm which are SHA512, SHA3-384, SHA3-512 and Blake3. you only need to run the program"""

import hashlib
import blake3

def encodeMessage(msg):
    encodedMsg = 0

    for char in msg:
        encodedMsg = encodedMsg << 8
        encodedMsg = encodedMsg ^ ord(char)
    return encodedMsg

def sha512(data):
  h = hashlib.sha512()
  h.update(data)
  return h.hexdigest()

def sha3_384(data):
  h = hashlib.sha3_384()
  h.update(data)
  return h.hexdigest()

def sha3_512(data):
  h = hashlib.sha3_512()
  h.update(data)
  return h.hexdigest()

def blake3_hash(message):
  try:
    encoded_message = message.encode()
    hash_digest09 = blake3.blake3(encoded_message).hexdigest()

    print(f'\nThe BLAKE3 hash of your message is:\n{hash_digest09}')

  except Exception as e:
    print(f'Error hashing message: {e}')

message = input('Type your message to be digested: ')

encoded_message = message.encode()
hash_digest01 = sha512(encoded_message)
hash_digest06 = sha3_384(encoded_message)
hash_digest07 = sha3_512(encoded_message)

print(f'The SHA512 hash of your message is:\n{hash_digest01}')
print(f'\nThe SHA3-384 hash of your message is:\n{hash_digest06}')
print(f'\nThe SHA3-512 hash of your message is:\n{hash_digest07}')
blake3_hash(message)