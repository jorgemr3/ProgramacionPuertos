import sys
from PyQt5 import uic, QtWidgets
import numpy as np
import statistics as stat
qtCreatorFile="Proyecto_Final.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_suma.clicked.connect(self.calcular)
        self.btn_prom.clicked.connect(self.calcular)
        self.btn_mediana.clicked.connect(self.calcular)
        self.btn_moda.clicked.connect(self.calcular)
        self.btn_Destandar.clicked.connect(self.calcular)
        self.btn_max.clicked.connect(self.calcular)
        self.btn_min.clicked.connect(self.calcular)
        self.btn_limpiar.clicked.connect(self.calcular)
        self.btn_varianza.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        try:
            # print(liste)
            # print(liste_num)
            obj=self.sender()
            boton=obj.objectName()
            num = self.txt_num1.text()
            liste = num.split(" ")
            liste_num=[int(i) for i in liste]
            if boton == "btn_suma":
                operacion = sum(liste_num)
            elif boton == "btn_prom":
                operacion = np.average(liste_num)
            elif boton == "btn_mediana":
                operacion = np.median(liste_num)
            elif boton == "btn_moda":
                operacion = stat.mode(liste_num)
            elif boton == "btn_Destandar":
                operacion = stat.stdev(liste_num)
            elif boton == "btn_max":
                operacion = np.max(liste_num)
            elif boton == "btn_min":
                operacion = np.min(liste_num)
            elif boton == "btn_varianza":
                operacion = np.var(liste_num)
            else:
                operacion = ""
                self.txt_num1.setText("")
            self.txt_res.setText(str(operacion))
        except Exception as err:
            print(err)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


# en el proyecto final hay que manipular la lista con las
# funciones min, max, y hacer promedio, moda, mediana y desviacion estandar
