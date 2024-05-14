import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="P7_CambiarColor.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals

        self.hs_R.setMinimum(0)
        self.hs_R.setMaximum(255)
        self.hs_R.setSingleStep(1)
        self.hs_R.setValue(0)
        self.hs_R.valueChanged.connect(self.cambiaR)

        self.hs_G.setMinimum(0)
        self.hs_G.setMaximum(255)
        self.hs_G.setSingleStep(1)
        self.hs_G.setValue(0)
        self.hs_G.valueChanged.connect(self.cambiaG)

        self.hs_B.setMinimum(0)
        self.hs_B.setMaximum(255)
        self.hs_B.setSingleStep(1)
        self.hs_B.setValue(0)
        self.hs_B.valueChanged.connect(self.cambiaB)

        self.R=0
        self.G=0
        self.B=0

    def cambiaR(self):
        self.R=self.hs_R.value()
        estilo = ("background-color: rgb(" + str(self.R) + "," + str(self.G) + "," + str(self.B) + ");")
        self.lbl_color.setStyleSheet(estilo)

    def cambiaG(self):
        self.G=self.hs_G.value()
        estilo = ("background-color: rgb(" + str(self.R) + "," + str(self.G) + "," + str(self.B) + ");")
        self.lbl_color.setStyleSheet(estilo)


    def cambiaB(self):
        self.B=self.hs_B.value()
        estilo = ("background-color: rgb(" + str(self.R) + "," + str(self.G) + "," + str(self.B) + ");")
        self.lbl_color.setStyleSheet(estilo)

    # Área de los Slots





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

