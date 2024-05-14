import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E01_SistemaDeUnidad.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_transformar.clicked.connect(self.transformar)
        self.txt_kilo.setEnabled(False)
        self.txt_km.setEnabled(False)
        self.txt_celsius.setEnabled(False)

    # Área de los Slots
    def transformar(self):
        try:
            var = float(self.txt_libra.text())
            kilo = var * 0.45359
            self.txt_kilo.setText(str(kilo))
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error en la magnitud de masa", str(e))

        try:
            var = int(self.txt_farhen.text())
            celsius = (5 / 9) * (var - 32)
            self.txt_celsius.setText(str(int(celsius)))
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error en la magnitud de temperatura ", str(e))

        try:
            var = float(self.txt_milla.text())
            km = var / 0.62137
            self.txt_km.setText(str(km))
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error en la magnitud de longitud ", str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
