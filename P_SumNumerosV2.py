import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="P_SumNumerosV2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_suma.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        try:
            num = self.txt_num1.text()
            liste = num.split(" ")
            print(liste)
            liste_num=[int(i) for i in liste]
            print(liste_num)
            suma = sum(liste_num)
            self.txt_res.setText(str(suma))
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


# en el proyecto final hay que manipular la lista con las
# funciones min, max, y hacer promedio, moda, mediana y desviacion estandar
