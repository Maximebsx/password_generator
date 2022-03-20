import string
import random

majuscules = string.ascii_uppercase
lettres = string.ascii_lowercase
chiffres = string.digits
caracterespeciaux = string.punctuation

print("Si vous voulez répondre positivement à la quetion écrivez True, sinon False")
while True:
    try:
        umaj = eval(input("Voulez-vous des majuscules ? (True ou False): "))
        ulettres = eval(input("Voulez-vous des minuscules ? (True ou False): "))
        uchiffres = eval(input("Voulez-vous des chiffres ? (True ou False): "))
        uponc = eval(input("Voulez-vous des caractères spéciaux ?(True ou False): "))
        l = int(input("Longueur du mot de passe: "))

        # Ajouter des composantes possibles
        char = ""
        char += majuscules if umaj else ""
        char += lettres if ulettres else ""
        char += chiffres if uchiffres else ""
        char += caracterespeciaux if uponc else ""

        # Générer le mot de passe
        MDP = "".join(random.choices(char, k=l))

        # Imprimer le nouveau mot de passe
        print("Votre mot de passe est : ", MDP)
    except:
        print("Veuillez suivre les instructions")
    break

import qrcode
import numpy as np

# data to encode
data = MDP

# instantiate QRCode object
qr = qrcode.QRCode(version=10, box_size=20, border=1)

# add data to the QR code
qr.add_data(data)

# compile the data into a QR code array
qr.make()

# print the image shape
print("La résolution de l'image QRcode :", np.array(qr.get_matrix()).shape)

# transfer the array into an actual image
img = qr.make_image(fill_color="black", back_color="white")

# save it to a file
img.save("MDP.png")

# we show the QR code on the screen
from PIL import Image

image = Image.open('MDP.png')
image.show()

# we send it by E-mail

import smtplib

SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
SMTP_USERNAME = "j.laharrague@tbs-education.org"
SMTP_PASSWORD = "wsnv71fu"
EMAIL_FROM = "j.laharrague@tbs-education.org"
EMAIL_TO = "celine.bergougnan8@gmail.com"
EMAIL_SUBJECT = "Mot de passe d'instagram"
EMAIL_MESSAGE = "Yo, ton mot de passe est :"+  MDP

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.starttls()
s.login(SMTP_USERNAME, SMTP_PASSWORD)
message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)
s.sendmail(EMAIL_FROM, EMAIL_TO, message)
s.quit()