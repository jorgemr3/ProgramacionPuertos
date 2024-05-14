import sys
from PyQt5 import uic, QtWidgets
import math
qtCreatorFile="P_09_Plantilla.ui"  # Nombre del archivo aquí.
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
        c1=float(self.txt_calif1.text())
        c2 =float (self.txt_calif2.text())
        c3 = float(self.txt_calif3.text())
        prom=(c1+c2+c3)/3
        if prom==10:
            cadena = "Tu promedio es de calificacion A !!!"
        elif prom >= 9:
            cadena = "Tu promedio es de calificacion B !!"
        elif prom >= 8:
            cadena = "Tu promedio es de calificacion C !"
        elif prom >= 7:
            cadena = "Tu promedio es de calificacion D+"
        elif prom >= 6:
            cadena = "Tu promedio es de calificacion D..."
        else:
            cadena = ("Tu promedio es de calificacion F :("
                      "\n estas reprobadote!")

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

