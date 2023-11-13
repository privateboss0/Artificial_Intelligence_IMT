import time
import pyotp

secretkey = "3Private6Public7" 
#secretkey = pyotp.random_base32() Either use a static key or random key, both kept by the service provider.
#but the program works inversely with the recovery code app secretkey set to static, while MFA and Integration app secretkey in random.

counter = 0

recovery_codes = pyotp.HOTP(secretkey)

# This is the secret key for counter value of recovery codes
print(recovery_codes.at(0))
print(recovery_codes.at(1))
print(recovery_codes.at(2))
print(recovery_codes.at(3))
print(recovery_codes.at(4))
print(recovery_codes.at(5))
print(recovery_codes.at(6))
print(recovery_codes.at(7))
print(recovery_codes.at(8))
print(recovery_codes.at(9))

while True:
  code = input("Enter your Recovery Code please: ")
  if recovery_codes.verify(code, counter):
    counter = 0
    print("You have sucessfully logged in with Recovery Codes!")

# Make the API call.
# TODOLIST: Implement your API call here into your application.
  break

else:
    print("Invalid recovery code. We advise to contact Support after 10 trials")
