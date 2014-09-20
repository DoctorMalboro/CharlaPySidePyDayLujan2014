# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(500, 150)
widget.setWindowTitle('Aplicación con ícono')
widget.setWindowIcon(QtGui.QIcon('icon.ico'))
widget.show()

sys.exit(app.exec_())
