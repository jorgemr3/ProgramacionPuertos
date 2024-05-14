void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Dame el cateto opuesto");
  while (!Serial.available()); 
  double a = Serial.readStringUntil('\n').toDouble(); 
  Serial.println("Dame el cateto adyacente");
  while (!Serial.available()); 
  double b = Serial.readStringUntil('\n').toDouble();

  if (isnan(a) || isnan(b)) {
    Serial.println("Solo se puede ingresar numeros");
    return;
  }
  double hypotenuse = sqrt(pow(a, 2) + pow(b, 2));
  Serial.print("La hipotenusa es\n");
  Serial.println(hypotenuse);
}

