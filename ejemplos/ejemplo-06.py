# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from PySide import QtGui
from PySide import QtCore

class Ejemplo6(QtGui.QWidget):

    def __init__(self):
        super(Ejemplo6, self).__init__()

        self.GUIConEventos2()

    def GUIConEventos2(self):

        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 550, 350)
        self.setWindowTitle('Ejemplo de señal N°2')
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ej6= Ejemplo6()
    sys.exit(app.exec_())
