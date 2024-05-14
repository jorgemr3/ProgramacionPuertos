void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Ingresa un numero");
  while(!Serial.available());
  int n = Serial.readStringUntil("\n").toInt();
  if(n % 2 == 0){ Serial.println("es par "); } else {Serial.print("es impar"); }
}
