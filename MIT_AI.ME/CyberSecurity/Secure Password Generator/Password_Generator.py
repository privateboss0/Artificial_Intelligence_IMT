#While I strongly advocate for SSO(Single Sign On) with 2FA/MFA as part of a strong identity solution,
#I thought creating a secure random password generator would be great, which is a better alternative to
#reusing passwords on multiple platforms. Just run the code and sea or don't and space..lool
#CS-MENT-W (Chemistry/Cybersecurity-Satellite-Magnetic-Electricity-Network-Transport-Wave) #killchain 7
#shorts (CS-TL (Chemistry/Cybersecurity-Satellite-Transport-Light)) 4

import secrets
import string

MAX_PASSWORD_LENGTH = 2147483647

def generate_password(length):
  """Given the password length, generates a secure password using this combination of strings"""
  chars = string.ascii_letters + string.digits + string.punctuation

  password = ''.join(secrets.choice(chars) for i in range(length))
  return password

while True:
  try:
    length = int(input('Enter the length of your password in numbers: '))

    if length <= 15:
      raise ValueError('Password length must be greater than fifteen')

    if length > MAX_PASSWORD_LENGTH:
      raise ValueError('Password length must be less than {}'.format(MAX_PASSWORD_LENGTH))

    password = generate_password(length)
    print("Generated password:", password)
    break
  except ValueError as e:
    print('\n{}'.format(e))
