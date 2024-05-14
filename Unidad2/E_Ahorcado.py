import random
import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "E_Ahorcado.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_inicia.clicked.connect(self.iniciarjuego)
        self.btn_checa.clicked.connect(self.adivina)
        self.btn_reinicia.clicked.connect(self.reiniciar)
        self.palabras = ["avion", "azul", "bicho", "bueno", "cajas", "calle", "datos", "denso", "ellos", "error",
                         "fuego", "feria", "gases", "gorro", "hielo", "halos", "india", "islas", "joven", "jugar",
                         "karma", "largo", "luzon", "mango", "nubes", "norte", "oruga", "opera", "papel", "pista",
                         "quedo", "quien", "ruido", "rocas", "salsa", "tacos", "tarta", "uvas", "unica", "virus",
                         "vista", "wally", "wimax", "xenon", "xerox", "yogur", "zorro"]
        self.palabra = random.choice(self.palabras)
        self.intentos = 6
        self.dicc_img = {
            1: ":/ahorcado/ahorcado_cabeza.JPG",
            2: ":/ahorcado/ahorcado_cuerpo.JPG",
            3: ":/ahorcado/ahorcado_brazo1.JPG",
            4: ":/ahorcado/ahorcado_brazo2.JPG",
            5: ":/ahorcado/ahorcado_pie1.JPG",
            6: ":/ahorcado/ahorcado_pie2.JPG"
        }
        self.txt_letra.setEnabled(False)
        self.txt_letra1.setEnabled(False)
        self.txt_letra2.setEnabled(False)
        self.txt_letra3.setEnabled(False)
        self.txt_letra4.setEnabled(False)
        self.txt_letra5.setEnabled(False)
        self.btn_checa.setEnabled(False)
        self.btn_reinicia.setEnabled(False)

    # Área de los Slots

    def iniciarjuego(self):
        self.btn_checa.setEnabled(True)
        self.btn_reinicia.setEnabled(True)
        self.btn_inicia.setEnabled(False)
        self.txt_letra.setEnabled(True)
        #print(self.palabra)
        QtWidgets.QMessageBox.information(self, "Atencion!",
                                          "El juego ha comenzado, se generó una palabra nueva, buena suerte! :)")

    def adivina(self):
        if self.txt_letra.text() == '':
            QtWidgets.QMessageBox.warning(self, "Campo vacío", "Por favor, ingrese una letra.")
        elif self.txt_letra.text() in self.palabra:
            if self.txt_letra.text() == self.palabra[0]:
                self.txt_letra1.setText(self.txt_letra.text())
            elif self.txt_letra.text() == self.palabra[1]:
                self.txt_letra2.setText(self.txt_letra.text())
            elif self.txt_letra.text() == self.palabra[2]:
                self.txt_letra3.setText(self.txt_letra.text())
            elif self.txt_letra.text() == self.palabra[3]:
                self.txt_letra4.setText(self.txt_letra.text())
            elif self.txt_letra.text() == self.palabra[4]:
                self.txt_letra5.setText(self.txt_letra.text())
            if self.txt_letra1.text() != '' and self.txt_letra2.text() != '' and self.txt_letra3.text() != '' and self.txt_letra4.text() != '' and self.txt_letra5.text() != '':
                QtWidgets.QMessageBox.information(self, "Felicidades!", "Has ganado el juego")
                self.txt_letra.setEnabled(False)
        else:
            self.intentos -= 1
            # cuando no adivina nada
            if self.intentos == 5:
                self.lbl_ahorcado.setPixmap(QtGui.QPixmap(self.dicc_img[1]))
            elif self.intentos == 4:
                self.lbl_ahorcado.setPixmap(QtGui.QPixmap(self.dicc_img[2]))
            elif self.intentos == 3:
                self.lbl_ahorcado.setPixmap(QtGui.QPixmap(self.dicc_img[3]))
            elif self.intentos == 2:
                self.lbl_ahorcado.setPixmap(QtGui.QPixmap(self.dicc_img[4]))
            elif self.intentos == 1:
                self.lbl_ahorcado.setPixmap(QtGui.QPixmap(self.dicc_img[5]))
            else:
                self.lbl_ahorcado.setPixmap(QtGui.QPixmap(self.dicc_img[6]))
                QtWidgets.QMessageBox.information(self, "Perdiste!", "Has perdido el juego :(")
                self.txt_letra.setEnabled(False)
                self.btn_checa.setEnabled(False)
                self.btn_reinicia.setEnabled(True)

    def reiniciar(self):
        self.txt_letra.clear()
        self.txt_letra1.clear()
        self.txt_letra2.clear()
        self.txt_letra3.clear()
        self.txt_letra4.clear()
        self.txt_letra5.clear()
        QtWidgets.QMessageBox.information(self, "Atencion!",
                                          "El juego se ha reiniciado")
        self.lbl_ahorcado.setPixmap(QtGui.QPixmap(":/ahorcado/descargaaaa.jfif"))
        self.txt_letra.setEnabled(False)
        self.palabra = random.choice(self.palabras)
        self.btn_inicia.setEnabled(True)
        self.btn_checa.setEnabled(False)
        self.btn_reinicia.setEnabled(False)
        self.intentos = 6


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
