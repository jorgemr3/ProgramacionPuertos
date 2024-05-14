import sys
from PyQt5 import QtWidgets
from Unidad_3.Graficacion import Grafica_plantilla as interfaz
import matplotlib.pyplot as plt

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_graficar.clicked.connect(self.graficar)
        self.btn_titulo.clicked.connect(self.titulo)
        self.btn_grilla.clicked.connect(self.grilla)
        self.btn_limpiar.clicked.connect(self.limpiar)

        self.cb_estiloLinea.addItem("Estilo: ",":")
        self.cb_estiloLinea.addItem("Estilo: ", "-")
        self.cb_estiloLinea.addItem("Estilo: ", "--")
        self.cb_estiloLinea.addItem("Estilo: ", "-.")
        self.cb_estiloLinea.currentIndexChanged.connect(self.estiloLinea)

        self.cb_Colorlinea.addItem("Negro", "black")
        self.cb_Colorlinea.addItem("Rojo", "red")
        self.cb_Colorlinea.addItem("Azul", "blue")
        self.cb_Colorlinea.addItem("Verde", "green")
        self.cb_ColorLinea.currentIndexChanged.connect(self.colorLinea)



    # Área de los Slots
    def graficar(self):
        polinomio = self.txt_polinom.text()
        polinomio = polinomio.replace("^","**")
        x = [i for i in range(self.spinBox_5,self.spinBox_4+1)]
        print("Valores para x")
        print(x)

        y =[eval(polinomio.replace("x","*("))]


    def titulo(self):
        pass
    def grilla(self):
        pass
    def limpiar(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

