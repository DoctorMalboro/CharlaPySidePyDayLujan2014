# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from PySide import QtGui

class Ejemplo3(QtGui.QWidget):

    def __init__(self):
        super(Ejemplo3, self).__init__()

        self.iniciarGUI()

    def iniciarGUI(self):

        self.setToolTip('Esta interfaz tiene un botón.')

        boton = QtGui.QPushButton('Ejemplo', self)
        boton.setToolTip('Este botón se puede presionar.')
        boton.resize(boton.sizeHint())
        boton.move(50,50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Interfaz con botón')
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ej3 = Ejemplo3()
    sys.exit(app.exec_())
