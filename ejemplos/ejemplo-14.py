# -*- coding: utf-8 -*-
import sys

from PySide import QtCore, QtGui
from ui_ejemplo_14 import *

class Ejemplo14(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Ejemplo14, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Ejemplo14()
    window.show()
    sys.exit(app.exec_())