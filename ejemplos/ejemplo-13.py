# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import datetime
from PySide import QtGui
from PySide import QtCore

class Ejemplo13(QtGui.QMainWindow):

    def __init__(self):
        super(Ejemplo13, self).__init__()
        self.EditorConToolbar()

    def EditorConToolbar(self):

        self.area_texto = QtGui.QTextEdit()
        self.cant_texto = 0

        hbox = QtGui.QVBoxLayout()
        hbox.addWidget(self.area_texto)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.guardar_texto)
        self.timer.setInterval(1000)
        self.timer.start(1000)

        abrir_archivo = QtGui.QAction('Abrir archivo', self)
        abrir_archivo.setShortcut('Ctrl+A')
        abrir_archivo.setStatusTip('Abre un archivo de texto')
        abrir_archivo.triggered.connect(self.abrir_archivo)
        guardar_archivo = QtGui.QAction('Guardar archivo', self)
        guardar_archivo.setShortcut('Ctrl+G')
        guardar_archivo.setStatusTip('Guardar un archivo')
        guardar_archivo.triggered.connect(self.guardar_archivo)
        guardar_archivo_como = QtGui.QAction('Guardar archivo como', self)
        guardar_archivo_como.setShortcut('Ctrl+Shift+G')
        guardar_archivo_como.setStatusTip('Guarda un archivo de texto'
            ' con otro nombre o extension')
        guardar_archivo_como.triggered.connect(self.guardar_archivo_como)
        salir = QtGui.QAction('Salir', self)
        salir.setShortcut('Ctrl+Q')
        salir.setStatusTip('Salir del programa')
        salir.triggered.connect(QtCore.QCoreApplication.instance().quit)

        menu = self.menuBar()
        menu_archivo = menu.addMenu('&Archivo')
        menu_archivo.addAction(abrir_archivo)
        menu_archivo.addAction(guardar_archivo)
        menu_archivo.addAction(guardar_archivo_como)
        menu_archivo.addAction(salir)

        self.setCentralWidget(self.area_texto)
        self.statusBar().showMessage('Iniciado')
        self.setLayout(hbox)
        self.setGeometry(300, 50, 900, 650)
        self.setWindowTitle('Editor de Texto')
        self.show()

    def abrir_archivo(self):

        archivo_x_abrir = QtGui.QFileDialog.getOpenFileName(self,
            'Abrir archivo', QtCore.QDir.currentPath())

        if archivo_x_abrir:
            self.archivo_de_texto = archivo_x_abrir[0]
            self.nombre = self.archivo_de_texto.split('/')[-1]
            archivo_a_abrir = QtCore.QFile(self.archivo_de_texto)
            if archivo_a_abrir.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
                self.area_texto.setText(str(archivo_a_abrir.readAll()))
                self.setWindowTitle('Editor de Texto - %s' % self.nombre)

    def guardar_archivo(self):

        if hasattr(self, 'archivo_de_texto'):
            archivo_a_guardar = open(self.archivo_de_texto, 'wb+')
            archivo_a_guardar.write(self.area_texto.toPlainText())
            archivo_a_guardar.close()
            self.statusBar().showMessage('Archivo %s guardado.' % self.archivo_de_texto)


    def guardar_archivo_como(self):

        archivo_x_guardar = QtGui.QFileDialog.getSaveFileName(self,
            'Guardar archivo', QtCore.QDir.currentPath())

        if self.archivo_de_texto == archivo_x_guardar[0]:
            archivo_a_guardar = open(self.archivo_de_texto, 'wb+')
            archivo_a_guardar.write(self.area_texto.toPlainText())
            archivo_a_guardar.close()
        else:
            self.archivo_de_texto = archivo_x_guardar[0]
            archivo_a_guardar = open(self.archivo_de_texto, 'wb+')
            archivo_a_guardar.write(self.area_texto.toPlainText())
            archivo_a_guardar.close()
        self.statusBar().showMessage('Archivo %s guardado.' % self.archivo_de_texto)
        self.setWindowTitle('Editor de texto - %s' % self.archivo_de_texto.split('/')[-1])


    def guardar_texto(self):

        if not self.area_texto.isReadOnly() and hasattr(self, 'archivo_de_texto'):
            if len(self.area_texto.toPlainText()) > self.cant_texto:
                self.cant_texto = len(self.area_texto.toPlainText())
                archivo_a_guardar = open(self.archivo_de_texto, 'wb+')
                if archivo_a_guardar:
                    archivo_a_guardar.write(self.area_texto.toPlainText())
                    archivo_a_guardar.close()
                self.statusBar().showMessage('Archivo guardado %s' \
                    % datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ej13 = Ejemplo13()
    sys.exit(app.exec_())
