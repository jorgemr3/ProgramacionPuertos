import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile="P1_DescripcionImagenes.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        # Área de los Signals
        self.datos_imagenes = {
        1: ["Hamster", "Roer", 5, "o-","C:\PIP_2024_1\IMG-20240216-WA0028.jpg"],
        2: ["Gato", "Gatar", 5, "o-","C:\PIP_2024_1\IMG-20240216-WA0027.jpg"],
        3: ["Cuyo", "Cuyar", 5, "o-","C:\PIP_2024_1\IMG-20240216-WA0025.jpg"],
        4: ["Perro","PERRAR", 5, "o-","C:\PIP_2024_1\IMG-20240216-WA0026.jpg"]
    }
        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)
        self.index_control=0
        self.btn_atras.setEnabled(False)
    # Área de los Slots
    def atras(self):
        if self.index_control<=1:
            self.index_control -= 1
            datos = self.datos_imagenes[self.index_control]
            print(datos)
            self.btn_atras.setEnabled(True)
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))

        if self.index_control ==1:
            self.btn_atras.setEnabled(False)

    def adelante(self):
        if self.index_control<=4:
            self.index_control += 1
            datos = self.datos_imagenes[self.index_control]
            print(datos)
            self.btn_adelante.setEnabled(True)
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))

        if self.index_control == 4:
            self.btn_adelante.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

# FALTA PONER RUTA DE IAGENES DE PERRO GATO HAMSTER Y
# CUYO, TAMBI
#

