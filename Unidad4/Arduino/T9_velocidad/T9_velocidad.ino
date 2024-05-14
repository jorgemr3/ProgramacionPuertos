void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("dame la unidad de distancia en metros");
  while(!Serial.available());
  int d = Serial.readStringUntil("\n").toInt();
  Serial.println("dame la unidad de tiempo en segundos ");
    while(!Serial.available());
  int t = Serial.readStringUntil("\n").toInt();
  Serial.println("la velocidad es de: ");
  Serial.println(d/t);
}
