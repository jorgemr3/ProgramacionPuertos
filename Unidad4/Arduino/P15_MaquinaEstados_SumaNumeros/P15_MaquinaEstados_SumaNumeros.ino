void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int valorA;
int valorB;
int  estado=0;
void loop() {
  // put your main code here, to run repeatedly:
  if (estado==0 || estado == 1){
     if(Serial.available()>0){
          int v = Serial.readString().toInt();
          if(estado==0){ valorA=v;} else { valorB=v;}
          estado++;
        }
  }
  if (estado==2){
    int r = valorA + valorB;
    Serial.println("Suma de A y B: "+ String(r));
    estado++;
  }
  if (estado==3){
    Serial.println("Desea repetir?... (1=SI, 0=NO");
    estado++;
  }
  if(estado==4){
    if(Serial.available()>0){
        int v = Serial.readString().toInt();
        if (v==1){estado=0;} else  {estado==3;}
      }
  }
  delay(100);
}

