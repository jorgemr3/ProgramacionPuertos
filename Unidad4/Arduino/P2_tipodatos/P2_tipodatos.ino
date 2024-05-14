
void setup() {
  // put your setup code here, to run once:
  //modulo uart... modulo asincrono universal de transmision y recepcion de datos
  Serial.begin(9600); //inicializa comunicacion serial
}

void loop() {
  // put your main code here, to run repeatedly:
    Serial.println("hola >:3");
    delay(500); // en milisegundos
}
