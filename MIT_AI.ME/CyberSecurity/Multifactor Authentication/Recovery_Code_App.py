import time
import pyotp

secretkey = "4Private6Public7" 

counter = 0
max_attempt = 10
used_codes = []

file_path = "used_codes.txt"  # Path to the file storing used codes

# Load used codes from file if it exists but no database currently
try:
    with open(file_path, "r") as f:
        used_codes = f.read().splitlines()
except FileNotFoundError:
    pass

#Recovery codes are typically emailed to the end user OOB(Out of Band)
recovery_codes = pyotp.HOTP(secretkey)

# This is the secret key for counter value of recovery codes
(recovery_codes.at(0))
(recovery_codes.at(1))
(recovery_codes.at(2))
(recovery_codes.at(3))
(recovery_codes.at(4))
(recovery_codes.at(5))
(recovery_codes.at(6))
(recovery_codes.at(7))
(recovery_codes.at(8))
(recovery_codes.at(9))
(recovery_codes.at(10))

while True:
    code = input("Enter your Recovery Code please: ")

    if recovery_codes.verify(code, counter):
        if code in used_codes:
            print("Recovery code has already been used. Please enter a different code.")
        else:
            counter = 0
            print("You have sucessfully logged in with Recovery Codes!")

            # Make the API call.
            # TODOLIST: Implement your API call here into your application.

            used_codes.append(code)  # Mark the code as used
            break

    else:
        counter += 1
        print("Invalid recovery code. Please try again.")

        if counter == max_attempt:
            print("Invalid recovery code. We advise to contact Support after 10 trials")
            break
