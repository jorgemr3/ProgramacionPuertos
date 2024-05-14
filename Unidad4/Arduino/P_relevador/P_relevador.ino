int relevador = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(relevador,OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if serial.available()>0{
    int v = serial.readString().toInt();
    digitalWrite(relevador,v);
    Serial.println("Estado Aplicado: "+ String(v));
  }
  delay(100);

}
