# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from PySide import QtGui
from PySide import QtCore

class Ejemplo9(QtGui.QWidget):

    def __init__(self):
        super(Ejemplo9, self).__init__()
        self.WidgetsParte2_2()

    def WidgetsParte2_2(self):

        self.progreso = QtGui.QProgressBar(self)
        self.progreso.setGeometry(30, 40, 200, 25)

        self.btn = QtGui.QPushButton('Comenzar', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.empieza)

        self.timer = QtCore.QBasicTimer()
        self.paso = 0

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.progreso)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Ejemplo de widget N°2')
        self.show()

    def timerEvent(self, e):
          
        if self.paso >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.paso = self.paso + 1
        self.progreso.setValue(self.paso)

    def empieza(self):
          
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Comezar')
        else:
            self.timer.start(100, self)
            self.btn.setText('Terminar')

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ej9 = Ejemplo9()
    sys.exit(app.exec_())
