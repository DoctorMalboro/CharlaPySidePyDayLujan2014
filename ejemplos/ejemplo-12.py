# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from PySide import QtGui
from PySide import QtCore
from PySide import QtWebKit

class Ejemplo12(QtGui.QWidget):

    def __init__(self):
        super(Ejemplo12, self).__init__()
        self.WidgetsParte2_5()

    def WidgetsParte2_5(self):

        self.barra_de_navegacion = QtGui.QLineEdit()
        self.navegador = QtWebKit.QWebView()
        self.barra_de_navegacion.returnPressed.connect(self.ir_a_pagina)

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.barra_de_navegacion)
        self.vbox.addWidget(self.navegador)
        self.setLayout(self.vbox)

        self.setGeometry(300, 50, 900, 650)
        self.setWindowTitle('Ejemplo de widget N°5')
        self.show()

    def ir_a_pagina(self):
        self.navegador.load(QtCore.QUrl(self.barra_de_navegacion.text()))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ej12 = Ejemplo12()
    sys.exit(app.exec_())
