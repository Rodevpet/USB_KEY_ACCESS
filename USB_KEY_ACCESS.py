#import RPi.GPIO as GPIO
import usb.core
import usb.util
import csv

Pin = 4
def initialisation (Pin,Base_Donne):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Pin, GPIO.OUT)
    with open(Base_Donne, encoding='utf8') as fichier:
        lecteur = csv.DictReader(fichier, delimiter=";")
        Liste_Blanche = [dict(ligne) for ligne in lecteur]
    return Liste_Blanche
def validation_acces ():
    Liste_USB = usb.core.find(find_all=True)
    if (Liste_USB!=None):
        for USB in Liste_USB :
            print (USB)
            for ID in Liste_Blanche :
                IDE = usb.util.get_string(USB,USB.iSerialNumber)
                print(IDE)
                if (IDE==ID["ID"]):
                    ID["ETAT"] = True
                    print ("Grant Access")

def fin_acces (liste_temoin,liste_actuelle):
    sorted(liste_temoin,key=tri_usb)
    sorted(liste_actuelle, key=tri_usb)
    cle_deconnecte = liste_temoin[:-1]
    ID_wrong = usb.util.get_string(cle_deconnecte, cle_deconnecte.iSerialNumber)
    for ID in Liste_Blanche ():
        if (ID_wrong==ID["ID"]):
            fermeture ()
def tri_usb (USB):
    return usb.util.get_string(USB,USB.iSerialNumber);
def ouverture ():
    GPIO.output(Pin, GPIO.HIGH)
def fermeture ():
    GPIO.output(Pin, GPIO.LOW)
def Port_Listen ():
    liste_temoin = usb.core.find(find_all=True)
    while True :
        liste_actuelle = usb.core.find(find_all=True)
        if (liste_temoin!=liste_actuelle):
            if (len(liste_temoin)<len(liste_actuelle)):
                print ("Connected")
                validation_acces()
                Etat = True
            if (len(liste_temoin)>len(liste_actuelle)):
                print ("Disconnected")
                fin_acces(liste_temoin,liste_actuelle)
            liste_temoin=usb.core.find()

Liste_Blanche = initialisation(Pin,"Liste_Blanche.csv")
Port_Listen()
