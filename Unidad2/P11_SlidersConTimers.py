import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile="P11_SlidersConTimers.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.segundoplano = QtCore.QTimer()
        self.segundoplano.timeout.connect(self.carrusel)
        self.lista_img =[
            "C:\PIP_2024_1\IMG-20240216-WA0028.jpg",
            "C:\PIP_2024_1\IMG-20240216-WA0027.jpg",
            "C:\PIP_2024_1\IMG-20240216-WA0025.jpg",
            "C:\PIP_2024_1\IMG-20240216-WA0026.jpg"
        ]
    # Área de los Slots
    def iniciar(self):
        t = self.btn_iniciar.text()
        if t == "INICIAR":
            self.btn_iniciar.setText("DETENER")
            self.idx=0
            self.segundoplano.start(110)
        else:
            self.btn_iniciar.setText("INICIAR")
            self.segundoplano.stop()

    def carrusel(self):
        self.txt_image.setPixmap(QtGui.QPixmap(self.lista_img[self.idx]))
        self.idx = (self.idx+1)%len(self.lista_img)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

