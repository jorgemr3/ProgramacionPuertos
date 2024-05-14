import sys

from PyQt5 import uic, QtWidgets
qtCreatorFile="P_07_Plantilla.ui"  # Nombre del archivo aquí.
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
        c1 = float(self.calf_1.text())
        c2 = float(self.calf_2.text())
        c3 = float(self.calf_3.text())
        c4 = float(self.calf_4.text())
        c5 = float(self.calf_5.text())
        prom=(c1+c2+c3+c4+c5)/5
        nombre = self.txt_nombre.text()
        cadena = "Promedio del alumno " + str(nombre) + " es de " + str(prom)

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

