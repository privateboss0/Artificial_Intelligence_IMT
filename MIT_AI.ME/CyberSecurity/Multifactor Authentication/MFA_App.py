import time
import pyotp
import qrcode

secretkey = "3Private6Public7" 
#secretkey = pyotp.random_base32() Either use a static key or random key, both kept by the service provider.
#but the program works inversely with the recovery code app set to static, while MFA na d Integration app in random.

counter = 0

dotp = pyotp.TOTP(secretkey)

while True:
  
  dotp_code = input("Enter the OTP from your Google/Microsoft Authenticator App: ")

  if dotp.verify(dotp_code):

    counter = 0

  
    print("Authentication successful!")

     # Make the API call.
    #Implement the API call here.

    break
  else:
   
    counter += 1
    
    print("Authentication failed, Please try again!")

    if counter == 5:
      
      # Prompt the user to enter a recovery code after 5 failed OTP attempt by importing Recovery_Code_App
      import Recovery_Code_App
      
      recovery_code = input("Enter your recovery code: ")

      # Verify the recovery code.
      R_codes = pyotp.HOTP(secretkey)
      if R_codes.verify(recovery_code):
    
        counter = 0

        print("Authentication successful!")
        break
      else:

        print("Invalid recovery code. We advise to contact Support after 10 trials")
