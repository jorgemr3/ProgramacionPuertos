//voltaje de de referencia : 5v
// bits de resolucion: 10 bits de resolucion... 1024 valores posibles...

//cada valor que les da el arduino se distancia uno del otro en 4.8mv
// la señal analogica del arduino funciona con los pines analogicos ( A# ...)

int potenciometro = A0; //pin analogico A0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //pinMode no se usa en pines analogicos 
  //un pin analogico solo es de entrada, no se puede usar en salida 

}

// P1     P2     P3
// GND    A#     5V
//        A0

int valor;
void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(potenciometro);
  Serial.println(valor);
  delay(100);
}
