//l298d modulo
//--- 2 puentes h 
//enA  --VELOCIDAD DE GIRO
//in1   ----SENTIDO
//in2
//out1
//out2

//enb
//in3
//in4
//out3
//out4

int ENA = 3;
int In1=5;
int In2=6;

//conectados al motor
//out 1 y 2 se conectan directamente del puente h al motor


void setup() {
  // put your setup code here, to run once:
  pinMode(In1,OUTPUT);
  pinMode(In2,OUTPUT);
// ena no lleva porque es de pwm
Serial.begin(9600);
Serial.setTimeout(10);
}

void loop() {
  if(Serial.available()>0){
    int v = Serial.readString().toInt();
    digitalWrite(In1,1);   //el out1 esta conectado a un led
    analogWrite(ENA,v);     //va de 0 a 255
    
  }
  // put your main code here, to run repeatedly:

}
