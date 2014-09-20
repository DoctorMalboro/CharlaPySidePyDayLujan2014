# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from PySide import QtGui
from PySide import QtCore

class Ejemplo5(QtGui.QWidget):

    def __init__(self):
        super(Ejemplo5, self).__init__()

        self.GUIConEventos()

    def GUIConEventos(self):

        fuente = QtGui.QFont()
        fuente.setPixelSize(36)

        self.nombre = QtGui.QLineEdit()
        self.nombre.returnPressed.connect(self.saludar)
        self.etiqueta = QtGui.QLabel('Hola!', self)
        self.etiqueta.setFont(fuente)
        self.etiqueta.setAlignment(QtCore.Qt.AlignCenter)        

        grilla = QtGui.QGridLayout()
        grilla.setSpacing(5)
        grilla.addWidget(self.nombre)
        grilla.addWidget(self.etiqueta)

        self.setLayout(grilla)

        self.setGeometry(200, 200, 350, 250)
        self.setWindowTitle('Interfaz con Interacción')
        self.show()

    def saludar(self):

        if self.nombre.text():
            self.etiqueta.setText('Hola <b>%s</b>!' % self.nombre.text())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ej5 = Ejemplo5()
    sys.exit(app.exec_())