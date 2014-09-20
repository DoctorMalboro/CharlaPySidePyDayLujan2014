# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from PySide import QtGui
from PySide import QtCore

class Ejemplo7(QtGui.QWidget):

    def __init__(self):
        super(Ejemplo7, self).__init__()
        self.GUIConEventos3()

    def GUIConEventos3(self):

        self.muestra = QtGui.QLabel('0 clicks')
        fuente = QtGui.QFont('Terminal', 48)
        self.muestra.setFont(fuente)
        self.muestra.setAlignment(QtCore.Qt.AlignCenter)
        contador = QtGui.QPushButton('Contar')
        self.contador = 0

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.muestra)
        vbox.addWidget(contador)

        self.setLayout(vbox)
        contador.clicked.connect(self.contar)

        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Ejemplo de señal N°3')
        self.show()

    def contar(self):
        self.contador += 1
        self.muestra.setText('%d clicks' % self.contador)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ej7 = Ejemplo7()
    sys.exit(app.exec_())
