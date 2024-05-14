import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P_IMC_Plantilla.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)
        self.txt_imc.setEnabled(False)
        self.dicc_imc = {
            1:[":/imc/images.jfif"],
            2:[":/imc/images (1).jfif"],
            3:[":/imc/png-transparent-obesity-adipose-tissue-health-overweight-fat-health-weight-loss-silhouette-black.png"],
            4:[":/imc/descarga.jfif"],
            5:[":/imc/descarga (1).png"],
            6:[":/imc/Daniel_Lambert_Benjamin_Marshall.jpg"]
        }

    # Área de los Slots
    def calcular(self):
        try:
            peso = float(self.txt_peso.text())
            estatura = float(self.txt_estatura.text())
            imc = peso / (estatura ** 2)
            if imc < 18.5:
                imagen = self.dicc_imc[1][0]
                self.lbl_imc.setPixmap(QtGui.QPixmap(imagen))
                QtWidgets.QMessageBox.warning(self, "IMC", "Peso bajo, necesita alimentarse mejor")

            elif 18.5 <= imc <= 24.9:
                imagen = self.dicc_imc[2][0]
                self.lbl_imc.setPixmap(QtGui.QPixmap(imagen))
                QtWidgets.QMessageBox.information(self, "IMC ",
                                                  "IMC de " + str(imc) + ",Peso normal, siga alimentandose bien ")

            elif 24.97 <= imc <= 29.9:
                imagen = self.dicc_imc[3][0]
                self.lbl_imc.setPixmap(QtGui.QPixmap(imagen))
                QtWidgets.QMessageBox.information(self, "IMC", "Sobrepeso, procurar el ejercicio y una dieta sana :)")
            elif 29.999 <= imc <= 34.9:
                imagen = self.dicc_imc[4][0]
                self.lbl_imc.setPixmap(QtGui.QPixmap(imagen))
                QtWidgets.QMessageBox.warning(self, "IMC", "Obesidad grado 1, hacer ejercicio y dieta rigurosa")
            elif 34.999 <= imc <= 39.9:
                imagen = self.dicc_imc[5][0]
                self.lbl_imc.setPixmap(QtGui.QPixmap(imagen))
                QtWidgets.QMessageBox.warning(self, "IMC", "Obesidad grado 2, necesita hacer mucho ejercicio y dieta estricta")
            elif imc >= 40.0:
                imagen = self.dicc_imc[6][0]
                self.lbl_imc.setPixmap(QtGui.QPixmap(imagen))
                QtWidgets.QMessageBox.warning(self, "IMC", "Obesidad grado 3,deje todo y vaya al gimnasio")
            self.txt_imc.setText(str(imc))
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error en la magnitud del IMC", str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
