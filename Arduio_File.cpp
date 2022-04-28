// C++ code
//
int Pin_Servo = 9;
int Pin_Open_State = 2;
int Pin_Close_State = 4;
void setup (){
  pinMode(Pin_Servo,OUTPUT);
  pinMode(Pin_Open_State,INPUT);
  pinMode(Pin_Close_State,INPUT);
  Serial.begin(9600);
}

void open(){
  digitalWrite(Pin_Servo,HIGH);
  delay(100);
  digitalWrite(Pin_Servo,LOW);
}

void close(){
  digitalWrite(Pin_Servo,LOW);
  delay(100);
  digitalWrite(Pin_Servo,HIGH);
}
void loop(){
  int open_state = digitalRead(Pin_Open_State);
  int close_state = digitalRead(Pin_Close_State);
  if (open_state==HIGH){
    open();
  }
  if (close_state==HIGH){
    close();
  }
}