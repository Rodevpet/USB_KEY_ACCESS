import RPi.GPIO as GPIO
import usb.core
import usb.util
import csv

# Pin GPIO sur lequel est branché la carte arduino
Pin = 4

# On initialise le Pin est le fichier contenant les clé valides pour ouvrir
def initialisation (Pin,Base_Donne):
    # On defini le mode de la carte, ici se sera BCM
    GPIO.setmode(GPIO.BCM)
    # On met le pin en mode ecriture
    GPIO.setup(Pin, GPIO.OUT)
    # Ouverture du fichier csv appele "Liste_Blanche.csv"
    with open(Base_Donne, encoding='utf8') as fichier:
        lecteur = csv.DictReader(fichier, delimiter=";")
        # Le dictionnaire Liste_Blanche contiendra les numeros de series des clés valides que contient le fichier "Liste_Blanche.csv"
        Liste_Blanche = [dict(ligne) for ligne in lecteur]
    return Liste_Blanche

# On vérifie si la clé est valide et si c'est le cas alors on ouvre
def validation_acces (Liste_USB):
    # On crée une itération des numéro de serie contenu dans la liste Liste_USB
    for USB_ID in Liste_USB :
        #On creée une itération des numéro de serie contenu dans le dictionnaire Liste_Blanche
        for ID in Liste_Blanche :
            #Si il y a une correspondance entre les deux itérations alors l'accès est valide
            if (USB_ID==ID["ID"]):
                print ("Grant Access")
                # fonction d'ouverture
                ouverture()

# On met fin a la validation de la clé
def fin_acces (liste_temoin,liste_actuelle):
    # On tri les deux listes, la cle retirée sera le dernier élément de la liste "liste_temoin"
    liste_temoin.sort()
    liste_actuelle.sort()
    # On récupère la clé qui a été deconnecté
    cle_deconnecte = liste_temoin [-1]
    print (cle_deconnecte)
    # On vérifie si cet clé a une correspondance avec un numéro de Serie valide
    for ID in Liste_Blanche:
        # Si c'est le cas alors on déclenche le processus de fermeture
        if (cle_deconnecte==ID["ID"]):
            fermeture ()
# permet d'ouvrir
def ouverture ():
    # Envoie un signal HAUT donc 1 a l'arduino qui va interprété ce signal comme une ouverture
    GPIO.output(Pin, GPIO.HIGH)

# pert de ferme
def fermeture ():
    # Envoie un signal BAS donc 0 a l'arduino qui va interprété ce signal comme une fermeture
    GPIO.output(Pin, GPIO.LOW)

# Fonction d'écoute des ports usb
def Port_Listen ():
    # On initialise une liste qui nous permettra de savoir quel changement il y a eu entre l'instant t=0 et t=1
    liste_temoin = []
    # On crée une itération de tout les éléments usb trouvés
    for dev in usb.core.find(find_all=True) :
        # On verifie que l'element usb est valide, donc qu'il existe
        if(usb.util.get_langids(dev)==None):
            pass
        else :
            #On verifie aussi que l'on va pouvoir récupérer son numéro de Serie
            if (usb.util.get_string(dev,dev.iSerialNumber) is None):
                pass
            else :
                # Si les deux conditions sont passé alors on rajoute le numéro de série de l'élémentusb à la liste témoin
                liste_temoin.append(usb.util.get_string(dev,dev.iSerialNumber))
    # On crée une boucle infinie pour que les ports usb soient constatment sur écoute
    while True :
        # On initialise la liste qui va contenir tout les éléments usb trouvés lors de l'écoute (à l'instant t=1)
        liste_actuelle = []
        # Une erreur dû à la déconnection du périphérique peut entrainer une erreur, on évite cela en la capturant
        try :
            # Comme pour la liste "liste_temoin" on vérifie que les éléments usb sont valides
            for dev in usb.core.find(find_all=True) :
                if(dev is None or usb.util.get_langids(dev)==None):
                   pass
                else :
                    if (usb.util.get_string(dev,dev.iSerialNumber) is None):
                        pass
                    else:
                        # Si l'élément est valide alors on l'ajoute à la liste des éléments usb
                        liste_actuelle.append(usb.util.get_string(dev,dev.iSerialNumber))
        except :
            pass
        # Si on détecte un changement entre la liste défini avant l'itération donc à t=0 et la liste défini après l'itération donc à t=1
        # Soit un nouvel élément usb à été ajouté soit il y en a qui à été retiré
        if (liste_temoin!=liste_actuelle):
            print (liste_temoin)
            print (liste_actuelle)
            # Si la liste à l'instant t=0 est plus petite que la liste à l'instant t=1 alors un nouvel élément usb a été ajouté
            if (len(liste_temoin)<len(liste_actuelle)):
                print ("Connected")
                # On déclenche donc la procédure de validation et d'accès
                validation_acces(liste_actuelle)
            # Si la liste à l'instant t=0 est plus grande que la liste à l'instant t=1 alors un élément usb a été retiré
            if (len(liste_temoin)>len(liste_actuelle)):
                print ("Disconnected")
                print(liste_actuelle)
                print (liste_temoin)
                # ON déclenche donc la procédure de fermture
                fin_acces(liste_temoin,liste_actuelle)
            # A la fin de l'itération pour recommencé l'écoute et trouvé les changments, la liste à l'instant t=0 devient la liste à l'instant t=1
            liste_temoin = liste_actuelle
Liste_Blanche = initialisation(Pin,"Liste_Blanche.csv")
Port_Listen()
