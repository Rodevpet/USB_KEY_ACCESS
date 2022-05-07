#include <stdio.h>
#include <stdlib.h>
//Module/Librairie pour l'accès usb
#define MACOS
#define ERREUR 1
#define OK 0
#ifdef MACOS
#include "./macos_11.6/include/libusb-1.0/libusb.h"
#endif
struct Etat
{
    int Etat_Initialisation;
    int Etat_Ouverture;
    struct libusb_device_descriptor Description;
};
void Initialisation (struct Etat etat);
void Ouverture (struct Etat etat, libusb_device *peripherique_usb, libusb_device_handle *interface);
void Obtention_Liste_Peripheriques_USB (struct Etat etat, libusb_device ** Liste_peripherique_usb);