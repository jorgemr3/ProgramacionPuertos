import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile="P3_ComboBox.ui"  # Nombre del archivo aquí.
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
        self.comboBox.addItem("Selecciona",0)
        self.comboBox.addItem("Soltera numero 1",1)
        self.comboBox.addItem("Soltera numero 2", 2)
        self.comboBox.addItem("Soltera numero 3", 3)
        self.comboBox.addItem("Conejo", 4)
        self.comboBox.currentIndexChanged.connect(self.cambia)
    # Área de los Slots
    def cambia(self):
        print("Text: "+ self.comboBox.currentText())
        print("Index: " + str(self.comboBox.currentIndex()))
        print("Data: "+ str(self.comboBox.currentData()))

        dataClave=self.comboBox.currentData()
        imagen= self.datos_imagenes[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

