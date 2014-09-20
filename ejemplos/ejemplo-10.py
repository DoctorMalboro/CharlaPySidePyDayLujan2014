# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from PySide import QtGui
from PySide import QtCore

class Ejemplo10(QtGui.QWidget):

    def __init__(self):
        super(Ejemplo10, self).__init__()
        self.WidgetsParte2_3()

    def WidgetsParte2_3(self):

        self.boton = QtGui.QPushButton('Abrir texto')
        self.boton.clicked.connect(self.abrir_archivo)
        self.etiqueta = QtGui.QLabel('')

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.etiqueta)
        vbox.addWidget(self.boton)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Ejemplo de widget N°3')
        self.show()

    def abrir_archivo(self):
        archivo_abierto = QtGui.QFileDialog.getOpenFileName(self,
            'Abrir archivo', QtCore.QDir.currentPath(),
            'Archivos de texto (*.txt)')

        if archivo_abierto:
            archivo_abierto = QtCore.QFile(archivo_abierto[0])
            if archivo_abierto.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
                texto = str(archivo_abierto.readAll())
                self.etiqueta.setText(texto)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ej10 = Ejemplo10()
    sys.exit(app.exec_())
