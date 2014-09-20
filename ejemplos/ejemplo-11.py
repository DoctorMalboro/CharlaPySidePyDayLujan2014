# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from PySide import QtGui
from PySide import QtCore

class Ejemplo11(QtGui.QWidget):

    def __init__(self):
        super(Ejemplo11, self).__init__()
        self.WidgetsParte2_4()

    def WidgetsParte2_4(self):

        self.boton = QtGui.QPushButton('Abrir imagen')
        self.boton.clicked.connect(self.abrir_imagen)
        self.imagen_etiqueta = QtGui.QLabel()
        self.imagen_etiqueta.setBackgroundRole(QtGui.QPalette.Base)
        self.imagen_etiqueta.setSizePolicy(QtGui.QSizePolicy.Ignored,
            QtGui.QSizePolicy.Ignored)

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.imagen_etiqueta)
        self.vbox.addWidget(self.boton)
        self.setLayout(self.vbox)

        self.setGeometry(300, 50, 500, 650)
        self.setWindowTitle('Ejemplo de widget N°4')
        self.show()

    def abrir_imagen(self):
        imagen_abierta = QtGui.QFileDialog.getOpenFileName(self,
            'Abrir imagen', QtCore.QDir.currentPath(),
            'Archivos de imagen (*.jpg *.png *gif)')

        if imagen_abierta:
            imagen = QtGui.QImage(imagen_abierta[0])
            if imagen.isNull():
                print imagen.isNull()

            self.imagen_etiqueta.setPixmap(
                QtGui.QPixmap.fromImage(imagen))
            self.imagen_etiqueta.setScaledContents(True)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ej11 = Ejemplo11()
    sys.exit(app.exec_())
