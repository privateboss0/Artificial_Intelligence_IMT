import time
import pyotp

secretkey = "4Private6Public7" 

counter = 0
max_attempt = 10

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
        counter = 0
        print("You have sucessfully logged in with Recovery Codes!")

        # Make the API call.
        # TODOLIST: Implement your API call here into your application.

        break

    else:
        counter += 1
        print("Invalid recovery code. Please try again.")

        if counter == max_attempt:
            print("Invalid recovery code. We advise to contact Support after 10 trials")
            break
