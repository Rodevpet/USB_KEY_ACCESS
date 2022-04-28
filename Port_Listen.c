#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "./macos_11.6/include/libusb-1.0/libusb.h"


int main (void){
    int e = libusb_init(NULL);
    libusb_device ** Device_List = NULL;
    ssize_t u = libusb_get_device_list(NULL,&Device_List);
    libusb_device *devi = Device_List[0];
    struct libusb_device_descriptor desc;
    libusb_device_handle *HAND = NULL;
    libusb_open(devi,&HAND);
    int rc = libusb_get_device_descriptor(devi, &desc);
    char pesg [200];
    libusb_get_string_descriptor_ascii (HAND,desc.iProduct,pesg,200);
    printf ("SerialNumber %s \n",pesg);
    libusb_free_device_list(Device_List, 1);
    libusb_close(HAND);
    libusb_exit(NULL);
    return 0;
}