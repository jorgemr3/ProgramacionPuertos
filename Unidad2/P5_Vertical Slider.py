import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile="P5_VerticalSlider.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.datos_imagenes = {
            1: ["Hamster", "Roer", 5, "o-", "C:\PIP_2024_1\IMG-20240216-WA0028.jpg"],
            2: ["Gato", "Gatar", 5, "o-", "C:\PIP_2024_1\IMG-20240216-WA0027.jpg"],
            3: ["Cuyo", "Cuyar", 5, "o-", "C:\PIP_2024_1\IMG-20240216-WA0025.jpg"],
            4: ["Perro", "PERRAR", 5, "o-", "C:\PIP_2024_1\IMG-20240216-WA0026.jpg"]
        }
        # Área de los Signals
        self.vs_integrantes.setMinimum(1)
        self.vs_integrantes.setMaximum(5)
        self.vs_integrantes.setSingleStep(1)
        self.vs_integrantes.setValue(1)
        self.vs_integrantes.valueChanged.connect(self.cambia)


    # Área de los Slots
    def cambia(self):
        dataClave = self.vs_integrantes.value()
        print(dataClave)
        imagen = self.datos_imagenes[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())




