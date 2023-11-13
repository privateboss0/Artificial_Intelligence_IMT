import time
import pyotp
import qrcode

secretkey = "PublicPrivate"

Uniform_Resource_Identifier = pyotp.totp.TOTP(secretkey).provisioning_uri(name="Aola", issuer_name= "Privateboss_App")

print(Uniform_Resource_Identifier)

#Make and download the QRcode for Privateboss_App to use with Google/Microsoft Authenticator app
qrcode.make(Uniform_Resource_Identifier).save("QRCode.png")
