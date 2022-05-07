#include "Port_Listen.h"
void Initialisation (struct Etat etat){
    if (etat.Etat_Initialisation != OK){
        int Intialisation = libusb_init(NULL);
        if (Initialisation != 0){
            etat.Etat_Initialisation = OK;
        }else{
            etat.Etat_Initialisation = ERREUR;
        }
    }
}

void Ouverture (struct Etat etat, libusb_device *peripherique_usb, libusb_device_handle *interface){
    if (etat.Etat_Initialisation == OK){
        int Etat_Ouverture =  libusb_open(peripherique_usb,&interface);
        if (Etat_Ouverture != 0){
            etat.Etat_Ouverture = OK;
        }else{
            etat.Etat_Ouverture = ERREUR;
        }
    }
}

void Obtention_Liste_Peripheriques_USB (struct Etat etat, libusb_device ** Liste_peripherique_usb){
    ssize_t nombre_peripherique_usb = libusb_get_device_list(NULL,&Liste_peripherique_usb);
    libusb_device* Adresses_Memoire_USB [nombre_peripherique_usb];
    for (int index=0; index<nombre_peripherique_usb; index++){
        libusb_device_handle *interface = NULL;
        Ouverture (etat,Liste_peripherique_usb[index],interface);
        struct libusb_device_descriptor description_peripherique;
        libusb_get_device_descriptor(Liste_peripherique_usb[index], &description_peripherique);
        char fiche_description [200];
        libusb_get_string_descriptor_ascii (interface,description_peripherique.iProduct,fiche_description,200);
        printf ("SerialNumber %s \n",fiche_description);
        libusb_close(interface);
        
    }
    libusb_free_device_list(Liste_peripherique_usb, 1);
}
int main (void){
    //Initialisation
    struct Etat etat;
    Initialisation(etat);

    //Obtention de la liste des peripheriques usb
    libusb_device ** Liste_peripherique_usb = NULL;
    Obtention_Liste_Peripheriques_USB(etat,Liste_peripherique_usb);
    /*
    struct libusb_device_descriptor desc;

    Ouverture(etat,devi,interface);
    int rc = libusb_get_device_descriptor(devi, &desc);
    char pesg [200];
    libusb_get_string_descriptor_ascii (interface,desc.iProduct,pesg,200);
    printf ("SerialNumber %s \n",pesg);
    libusb_free_device_list(Device_List, 1);
    libusb_close(interface);
    libusb_exit(NULL);
    */
   libusb_exit(NULL);
    return 0;
}