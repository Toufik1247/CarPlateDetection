import pytesseract
import os
from PIL import Image
import cv2
import torch
from utils.general import xyxy2xywh
import re
import time
# import serial
from fuzzywuzzy import fuzz

platereaded = ""


def readplatebox(xyxy, im, gain=1.02, pad=10, square=False, BGR=False):
    global platereaded
    xyxy = torch.tensor(xyxy).view(-1, 4)
    b = xyxy2xywh(xyxy)
    b[:, 2:] = b[:, 2:] * gain + pad

    x1 = max(0, int(xyxy[0, 0]) - 25)
    x2 = min(im.shape[1], int(xyxy[0, 2]) - 25)
    y1 = max(0, int(xyxy[0, 1]))
    y2 = min(im.shape[0], int(xyxy[0, 3]))

    crop = im[y1:y2, x1:x2, :: (1 if BGR else -1)]   
    if crop.size > 0:
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(str(filename), crop)
        platereaded = pytesseract.image_to_string(
            Image.open(filename),
            lang="eng",
            config="--psm 7 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- --user-patterns my.patterns",
            timeout=10,
        )
        # time.sleep(2)
        os.remove(filename)
        return platereaded
    else:
        return None


def fuzzratio():
    pattern = "[A-Z][A-Z][-][0-9][0-9][0-9][-][A-Z][A-Z]"
    authorizedPlates = [
        "1924 YX 25",
        "DR-819-YV",
        "EL-979-JZ",
    ]
    if re.match(pattern, str(platereaded.strip())) is not None:
        print("LECTURE DE PLAQUE EN COURS...")
        print("PLAQUE D'IMMATRICULATION LUE : ", platereaded.strip())
        for i in authorizedPlates:
            if fuzz.ratio(str(platereaded.strip()), i) > 95:
                print("PLAQUE D'IMMATRICULATION LUE : ", platereaded.strip())
                print(
                    "CORRESPONDANCE DE LA PLAQUE AVEC LA BASE DE DONNEES: ",
                    fuzz.ratio(
                        platereaded.strip(),
                        i,
                    ),
                    "%",
                )
                print("VOTRE VEHICULE EST AUTORISE\n \n \n \n \n \n \n \n \n \n")
            else:
                print("VOTRE VEHICULE N'EST PAS AUTORISE")
                print(
                    "ASSUREZ-VOUS QUE VOTRE VEHICULE EST ENREGISTRE DANS LA BASE DE DONNEES"
                )
                print(
                    "ET QUE VOTRE PLAQUE D'IMMATRICULATION EST PROPRE ET LISIBLE \n \n \n \n \n \n \n \n \n \n"
                )


def closingAccess():
    t_end = time.time() + 2
    while True:
        if time.time() > t_end:
            print("FERMETURE DE LA BARRIERE \n \n \n \n \n \n \n \n \n \n")
            break
