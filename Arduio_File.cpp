// C++ code
//
#include <Servo.h>

Servo servo;

int Pin_Servo = 9;
int Pin_State = 2;
void setup (){
  //on définie le pin utilisé pour envoyer le signal au servo moteur
  servo.attach(Pin_Servo);
  //on définie le pin utilisé par le raspberry pi pour envoyer le signal (en mode lecture)
  pinMode(Pin_State,INPUT);
  Serial.begin(9600);
}

void open(){
  //On tourne de 90°
  servo.write(90);
}

void close(){
  //On tournede de -90°
  servo.write(0);
}
void loop(){
  //on récupère le signal envoyer par le raspberry pi
  int state = digitalRead(Pin_State);
  //il y a un signal, ou le courant est haut, alors on ouvre
  if (state == HIGH){
    open();
    }
    //il n'y a pas de signal, ou le courant est bas, alors on ferme
   if (state == LOW){
      close();
    }
}