import serial
import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P23_InterfazConexionArduino3.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_conectar.clicked.connect(self.accion)
        self.arduino = None
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturaArduino)
        self.btn_led.clicked.connect(self.control_led)
        self.estado_led = 1

    # Área de los Slots
    def accion(self):
        texto_boton = self.btn_conectar.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.segundoPlano.start(100)
            self.btn_conectar.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")
        elif texto_boton == "DESCONECTAR" and self.arduino.isOpen():
            self.segundoPlano.stop()
            self.arduino.close()
            self.btn_conectar.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
        else:
            self.arduino.open()
            self.segundoPlano.start(100)
            self.btn_conectar.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")

    def lecturaArduino(self):
        try:
            if not self.arduino is None and self.arduino.isOpen():
                if self.arduino.inWaiting():
                    cadena = self.arduino.readline().decode().strip()
                    if cadena != "":
                        self.datos.addItem(cadena)
                        self.datos.setCurrentRow(self.datos.count() - 1)
        except Exception as e:
            print(e)

    def control_led(self):
        if not self.arduino is None and self.arduino.isOpen():
            if self.estado_led == 0:
                self.btn_led.setText("PRENDER")
            else:
                self.btn_led.setText("APAGAR")
            val = "1" if self.estado_led == 1 else "0" + "\n"
            self.arduino.write(val.encode())
            self.estado_led = self.estado_led * -1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
