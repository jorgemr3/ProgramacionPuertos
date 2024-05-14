import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile="P2_CheckBox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.txt_equipo.setText("hola")
        # Área de los Signals
        self.cb_yisus.toggled.connect(self.sel_yisus)
        self.cb_Jorge.toggled.connect(self.sel_Jorge)
        self.cb_Ana.toggled.connect(self.sel_Ana)
        self.cb_axel.toggled.connect(self.sel_axel)

        self.lbl_yisus.setPixmap(QtGui.QPixmap("C:\PIP_2024_1\IMG-20240216-WA0028.jpg"))
        self.lbl_jorge.setPixmap(QtGui.QPixmap("C:\PIP_2024_1\IMG-20240216-WA0027.jpg"))
        self.lbl_ana.setPixmap(QtGui.QPixmap("C:\PIP_2024_1\IMG-20240216-WA0025.jpg"))
        self.lbl_axel.setPixmap(QtGui.QPixmap("C:\PIP_2024_1\IMG-20240216-WA0026.jpg"))


        self.yisus=""
        self.Jorge = ""
        self.Ana = ""
        self.axel=""

    # Área de los Slots
    def sel_yisus(self):
        if self.cb_yisus.isChecked():
            print("Yisus True")
            self.yisus="Yisus\n"

        else:
            print("Yisus False")
            self.yisus = ""
        self.txt_equipo.setText(self.yisus+self.Jorge+self.Ana+self.axel)

    def sel_Jorge(self):
        if self.cb_Jorge.isChecked():
            print("Jorge True")
            self.Jorge = "JORGE\n"
        else:
            print("Jorge False")
            self.Jorge = ""
        self.txt_equipo.setText(self.yisus + self.Jorge + self.Ana + self.axel)

    def sel_Ana(self):
        if self.cb_Ana.isChecked():
            print("Ana True")
            self.Ana = "ANA\n"
        else:
            print("ANA False")
            self.Ana = ""
        self.txt_equipo.setText(self.yisus + self.Jorge + self.Ana + self.axel)

    def sel_axel(self):
        if self.cb_axel.isChecked():
            print("Axel True")
            self.axel = "AXEL\n"
        else:
            print("axel False")
            self.axel = ""
        self.txt_equipo.setText(self.yisus + self.Jorge + self.Ana + self.axel)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

