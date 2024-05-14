import serial as conn

arduino=conn.Serial(port="", baudrate=9600, timeout=1)
print("conexion con arduino exitosa")

archivo = open("../Archivos/dato_potenciometro.csv")

i=0
while i<10:
    a = arduino.readLine()
    a = a.decode()
    a = a.strip()
    print(a)
    archivo.write(a + "\n")
    i+=1
archivo.flush()
archivo.close()
