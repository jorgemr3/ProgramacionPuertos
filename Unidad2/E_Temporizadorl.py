import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "E_temporizador.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.dicc_temp = {
            1: [":/temp/7koo.gif"],
            2: [":/temp/RELOJ.JPG"]
        }
        self.lcd_temp.setNumDigits(8)
        self.lcd_temp.display(0)
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_detener.clicked.connect(self.detener)
        self.btn_redo.clicked.connect(self.reiniciar)
        self.btn_reanudar.clicked.connect(self.reanudar)
        self.detenido = self.dicc_temp[2][0]
        self.andando = self.dicc_temp[1][0]
        self.lbl_tiempo.setPixmap(QtGui.QPixmap(self.detenido))

    # Área de los Slots
    def iniciar(self):
        tiempo = self.txt_Seg.text()
        if tiempo == '':
            QtWidgets.QMessageBox.warning(self, "Campo vacío", "Por favor, ingrese un valor en el campo de tiempo.")
        else:
            try:
                seg = int(tiempo)
                if seg <= 0:
                    QtWidgets.QMessageBox.warning(self, "Error en el tiempo", "El tiempo debe ser mayor que 0")
                else:
                    self.btn_iniciar.setEnabled(False)
                    self.lcd_temp.display(seg)
                    self.temporizador = QtCore.QTimer(self)
                    self.tiempo_restante = seg
                    self.temporizador.timeout.connect(self.actualizar_temporizador)
                    self.temporizador.start(1000)
                    self.lbl_tiempo.setMovie(QtGui.QMovie(self.andando))
                    self.lbl_tiempo.movie().start()
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Error en el tiempo", str(e))

    def actualizar_temporizador(self):
        self.tiempo_restante -= 1
        self.lcd_temp.display(self.tiempo_restante)
        if self.tiempo_restante == 0:
            self.temporizador.stop()
            self.btn_iniciar.setEnabled(True)
            self.btn_reanudar.setEnabled(False)
            self.lbl_tiempo.setPixmap(QtGui.QPixmap(self.detenido))
            QtWidgets.QMessageBox.information(self, "Fin del tiempo", "El tiempo ha terminado")

    def detener(self):
        if self.lcd_temp.value() != 0:
            self.temporizador.stop()
            self.btn_reanudar.setEnabled(True)
            self.lbl_tiempo.setPixmap(QtGui.QPixmap(self.detenido))
            QtWidgets.QMessageBox.information(self, "Informacion", "El temporizador ha sido detenido.")
        else:
            QtWidgets.QMessageBox.information(self, "Informacion", "El temporizador no ha sido iniciado.")

    def reiniciar(self):
        if self.lcd_temp.value() != 0:
            self.lcd_temp.display(0)
            self.txt_Seg.setText("0")
            self.tiempo_restante = 0
            self.temporizador.stop()
            self.btn_iniciar.setEnabled(True)
            self.btn_reanudar.setEnabled(False)
            self.lbl_tiempo.setPixmap(QtGui.QPixmap(self.detenido))
            QtWidgets.QMessageBox.information(self, "Informacion", "El temporizador ha sido reiniciado.")
        else:
            QtWidgets.QMessageBox.information(self, "Informacion", "El temporizador no ha sido iniciado.")

    def reanudar(self):
        self.lbl_tiempo.setMovie(QtGui.QMovie(self.andando))
        self.lbl_tiempo.movie().start()
        self.temporizador.start(1000)
        self.btn_reanudar.setEnabled(False)
        QtWidgets.QMessageBox.information(self, "Informacion", "El temporizador ha sido reanudado.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
