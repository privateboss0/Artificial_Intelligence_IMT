import time
import pyotp
import qrcode

secretkey = "3Private6Public7" 
#secretkey = pyotp.random_base32() Either use a static key or random key, both kept by the service provider.
#but the program works inversely with the recovery code app secretkey set to static, while MFA and Integration app secretkey in random.

Uniform_Resource_Identifier = pyotp.totp.TOTP(secretkey).provisioning_uri(name="Aola", issuer_name= "Privateboss_App")

print(Uniform_Resource_Identifier)

#Make and download the QRcode for Privateboss_App to use with Google/Microsoft Authenticator app
qrcode.make(Uniform_Resource_Identifier).save("QRCode.png")
