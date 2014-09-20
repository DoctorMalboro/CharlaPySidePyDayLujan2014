# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from PySide import QtGui

class Ejemplo4(QtGui.QWidget):

    def __init__(self):
        super(Ejemplo4, self).__init__()

        self.GUILayout()

    def GUILayout(self):

        etiqueta = QtGui.QLabel('Layout', self)
        etiqueta.move(15, 10)

        explicando = QtGui.QLabel('sin', self)
        explicando.move(35, 40)

        layouts = QtGui.QLabel('orden', self)
        layouts.move(55, 70)

        botonOK = QtGui.QPushButton('Ok')
        botonCancelar = QtGui.QPushButton('Cancelar')

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(botonOK)
        hbox.addWidget(botonCancelar)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Interfaz con Layout')
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ej4 = Ejemplo4()
    sys.exit(app.exec_())