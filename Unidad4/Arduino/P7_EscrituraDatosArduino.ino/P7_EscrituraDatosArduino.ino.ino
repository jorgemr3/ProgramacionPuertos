int v;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:

  if(Serial.available()>0){  //comprobar el buffer del arduino
  //leera todos los bytes que le sea posible antes de 
  //que se acabe el tiempo de espera (timeout)
  //timeout por defecto 1 segundo 
      v = Serial.readString().toInt();
      Serial.println(v);
  }

}
