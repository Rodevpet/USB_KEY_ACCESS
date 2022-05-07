// C++ code
//
#include <Servo.h>

Servo servo;
int Pin_Servo = 9;
int Pin_Open_State = 2;
int Pin_Close_State = 4;
void setup (){
  servo.attach(Pin_Servo);
  pinMode(Pin_Open_State,INPUT);
  pinMode(Pin_Close_State,INPUT);
  Serial.begin(9600);
}

void open(){
  servo.write(90);
}

void close(){
  servo.write(0);
}
void loop(){
  int open_state = digitalRead(Pin_Open_State);
  int close_state = digitalRead(Pin_Close_State);
  if (open_state == HIGH){
    open();
  }
  if (close_state == HIGH){
    close();
  }
}