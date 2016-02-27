# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listaproductos.ui'
#
# Created: Sat Feb 27 10:05:15 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.IdIPrecio = QtGui.QLabel(self.centralwidget)
        self.IdIPrecio.setGeometry(QtCore.QRect(420, 110, 64, 21))
        self.IdIPrecio.setObjectName(_fromUtf8("IdIPrecio"))
        self.IdIProducto = QtGui.QLabel(self.centralwidget)
        self.IdIProducto.setGeometry(QtCore.QRect(420, 50, 64, 21))
        self.IdIProducto.setObjectName(_fromUtf8("IdIProducto"))
        self.IdICodigo = QtGui.QLabel(self.centralwidget)
        self.IdICodigo.setGeometry(QtCore.QRect(100, 50, 64, 21))
        self.IdICodigo.setObjectName(_fromUtf8("IdICodigo"))
        self.IdICantidad = QtGui.QLabel(self.centralwidget)
        self.IdICantidad.setGeometry(QtCore.QRect(100, 110, 64, 21))
        self.IdICantidad.setObjectName(_fromUtf8("IdICantidad"))
        self.btGuardar = QtGui.QPushButton(self.centralwidget)
        self.btGuardar.setGeometry(QtCore.QRect(250, 440, 95, 31))
        self.btGuardar.setObjectName(_fromUtf8("btGuardar"))
        self.btActualizar = QtGui.QPushButton(self.centralwidget)
        self.btActualizar.setGeometry(QtCore.QRect(400, 440, 95, 31))
        self.btActualizar.setObjectName(_fromUtf8("btActualizar"))
        self.txtCodigo = QtGui.QLineEdit(self.centralwidget)
        self.txtCodigo.setGeometry(QtCore.QRect(190, 40, 113, 33))
        self.txtCodigo.setObjectName(_fromUtf8("txtCodigo"))
        self.txtPrecio = QtGui.QLineEdit(self.centralwidget)
        self.txtPrecio.setGeometry(QtCore.QRect(500, 100, 113, 33))
        self.txtPrecio.setObjectName(_fromUtf8("txtPrecio"))
        self.txtCantidad = QtGui.QLineEdit(self.centralwidget)
        self.txtCantidad.setGeometry(QtCore.QRect(190, 100, 113, 33))
        self.txtCantidad.setObjectName(_fromUtf8("txtCantidad"))
        self.txtProducto = QtGui.QLineEdit(self.centralwidget)
        self.txtProducto.setGeometry(QtCore.QRect(500, 40, 113, 33))
        self.txtProducto.setObjectName(_fromUtf8("txtProducto"))
        self.tblproductos = QtGui.QTableWidget(self.centralwidget)
        self.tblproductos.setGeometry(QtCore.QRect(120, 220, 451, 192))
        self.tblproductos.setObjectName(_fromUtf8("tblproductos"))
        self.tblproductos.setColumnCount(0)
        self.tblproductos.setRowCount(0)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 160, 681, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.IdIPrecio.setText(_translate("MainWindow", "Precio", None))
        self.IdIProducto.setText(_translate("MainWindow", "Producto", None))
        self.IdICodigo.setText(_translate("MainWindow", "Codigo", None))
        self.IdICantidad.setText(_translate("MainWindow", "Cantidad", None))
        self.btGuardar.setText(_translate("MainWindow", "Guardar", None))
        self.btActualizar.setText(_translate("MainWindow", "Actualizar", None))

