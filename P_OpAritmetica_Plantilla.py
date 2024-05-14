import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="P_OpAritmetica_Plantilla.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_suma.clicked.connect(self.calcular)
        self.btn_resta.clicked.connect(self.calcular)
        self.btn_multi.clicked.connect(self.calcular)
        self.btn_div.clicked.connect(self.calcular)
    # Área de los Slots
    def calcular(self):
        try:
            objeto = self.sender()
            nombre = objeto.objectName()
            num1 = int(self.txt_num1.text())
            num2= int(self.txt_num2.text())
            if nombre == "btn_suma":
                resultado = num1 + num2
            elif nombre == "btn_resta":
                resultado = num1 - num2
            elif nombre == "btn_multi":
                resultado = num1 * num2
            else:
                resultado = num1 / num2
            self.txt_res.setText(str(resultado))
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

