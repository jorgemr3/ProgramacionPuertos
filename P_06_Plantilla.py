import sys
import math
from PyQt5 import uic, QtWidgets
qtCreatorFile="P_06_Plantilla.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        x1=int(self.txt_x1.text())
        y1=int(self.txt_y1.text())
        x2 = int(self.txt_x2.text())
        y2 = int(self.txt_y2.text())
        distancia = math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
        cadena = "Distancia entre punto uno y punto dos es de: " + str(distancia)

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

