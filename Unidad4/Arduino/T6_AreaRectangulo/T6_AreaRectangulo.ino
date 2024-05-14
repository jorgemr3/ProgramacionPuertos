void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}



void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Ingresa la base del rectangulo");
  while(!Serial.available());
  int base = Serial.readStringUntil("\n").toInt();
  Serial.println("Ingresa la altura del rectangulo");
  while(!Serial.available());
  int altura = Serial.readStringUntil("\n").toInt();
  Serial.println("El area del rectangulo es: ");
  Serial.println(base * altura);
}
