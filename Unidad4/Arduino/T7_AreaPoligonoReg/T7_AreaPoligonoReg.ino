void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Dame la longitud el apotema");
  double a = Serial.readString().toDouble();
  Serial.println("Dame el perimetro del area");
  double p = Serial.readString().toDouble();
  double area = (a*p)/2;
  Serial.println("el area del poligono regular es: ");
  Serial.print(area);
} 
