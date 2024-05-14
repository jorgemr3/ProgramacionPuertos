import serial as conn
from matplotlib import pyplot as plt

arduino=conn.Serial(port="COM4", baudrate=9600, timeout=1)
print("conexion con arduino exitosa")

archivo = open("../Archivos/dato_potenciometro.csv")

x=[i for i in range(100)]
y=[0 for i in range(100)]

while True:
    a = arduino.readLine().decode().strip()
    y.pop(0)
    y.append(int(a))
    print(y)
    plt.plot(x,y)
    plt.grid = True
    plt.show()
