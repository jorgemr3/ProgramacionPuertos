import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile="P13_SeleccionMascota.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.lbl_yisus.setPixmap(QtGui.QPixmap("C:\PIP_2024_1\IMG-20240216-WA0028.jpg" ))
        self.lbl_jorge.setPixmap(QtGui.QPixmap("C:\PIP_2024_1\IMG-20240216-WA0027.jpg" ))
        self.lbl_ana.setPixmap(QtGui.QPixmap("C:\PIP_2024_1\IMG-20240216-WA0025.jpg" ))
        self.lbl_axel.setPixmap(QtGui.QPixmap("C:\PIP_2024_1\IMG-20240216-WA0026.jpg" ))

        # Área de los Signals
        self.rb_yisus.toggled.connect(self.tog_yisus)
        self.rb_yisus.clicked.connect(self.cl_yisus)

        self.rb_jorge.toggled.connect(self.tog_Jorge)
        self.rb_jorge.clicked.connect(self.cl_Jorge)

        self.rb_ana.toggled.connect(self.tog_Ana)
        self.rb_ana.clicked.connect(self.cl_ana)

        self.rb_axel.toggled.connect(self.tog_axel)
        self.rb_axel.clicked.connect(self.cl_axel)

    # Área de los Slots
    def tog_axel(self):
        estado = self.rb_axel.isChecked()
        print(f"el axel ha cambiado de estado (toggle), Nuevo estado: {estado}")

    def cl_axel(self):
        print("hiciste click en axel")
        self.txt_equipo.setText("Axel")


    def tog_Ana(self):
        estado = self.rb_ana.isChecked()
        print(f"Ana ha cambiado de estado (toggle), Nuevo Estado: {estado} ")

    def cl_ana(self):
        print("Hiciste click en ana patto ")
        self.txt_equipo.setText("Ana")

    def tog_Jorge(self):
        estado = self.rb_Jorge.isChecked()
        print(f"Jorge ha cambiado de estado (toggle), Nuevo Estado: {estado} ")

    def cl_Jorge(self):
        print("hiciste click en jorge")
        self.txt_equipo.setText("Jorge")

    def tog_yisus(self):
        estado = self.rb_yisus.isChecked()
        print(f"Yisus ha cambiado de estado (toggle), Nuevo Estado: {estado} ")

    def cl_yisus(self):
        print("hiciste click en yisus")
        self.txt_equipo.setText("Yisus")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

