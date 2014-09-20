# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from PySide import QtGui
from PySide import QtCore

class Ejemplo8(QtGui.QWidget):

    def __init__(self):
        super(Ejemplo8, self).__init__()
        self.WidgetsParte2_1()

    def WidgetsParte2_1(self):

        texto_1 = QtGui.QLabel('Tamaño')
        fuente_texto_1 = QtGui.QFont('Arial', 72)
        texto_1.setFont(fuente_texto_1)
        texto_2 = QtGui.QLabel('Fuente')
        fuente_texto_2 = QtGui.QFont('Comic Sans MS', 18)
        texto_2.setFont(fuente_texto_2)
        texto_3 = QtGui.QLabel('Atributos')
        fuente_texto_3 = QtGui.QFont('Arial', 18,
            QtGui.QFont.Bold,
            italic=True)
        texto_3.setFont(fuente_texto_3)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(texto_1)
        vbox.addWidget(texto_2)
        vbox.addWidget(texto_3)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Ejemplo de widget N°1')
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ej8 = Ejemplo8()
    sys.exit(app.exec_())
