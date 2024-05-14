import serial
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="P21_InterfazConexionArduino.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        # Área de los Signals
        self.btn_conectar.connect.clicked(self.accion)
        self.arduino = None
    # Área de los Slots
    def accion(self):
        texto_boton = self.btn_conectar.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            self.arduino=serial.Serial(port=com, baudrate=9600, timeout=1)
            self.btn_conectar.setText("DESCONECTAR")
        elif texto_boton == "DESCONECTAR" and self.arduino.isOpen():
            self.arduino.close()
            self.btn_conectar.setText("RECONECTAR")
        else:
            self.arduino.open()
            self.btn_conectar.setText("DESCONECTAR")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

