# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 331, 291))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn1 = QtWidgets.QPushButton(self.groupBox)
        self.btn1.setGeometry(QtCore.QRect(270, 50, 41, 23))
        self.btn1.setObjectName("btn1")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(18, 50, 241, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 201, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 47, 13))
        self.label_3.setObjectName("label_3")
        self.btn2 = QtWidgets.QPushButton(self.groupBox)
        self.btn2.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.groupBox)
        self.btn3.setGeometry(QtCore.QRect(130, 230, 75, 23))
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.groupBox)
        self.btn4.setGeometry(QtCore.QRect(240, 230, 75, 23))
        self.btn4.setObjectName("btn4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Módulo ráster"))
        self.groupBox.setTitle(_translate("MainWindow", "Datos de entrada"))
        self.label.setText(_translate("MainWindow", "Seleciona el archivo"))
        self.btn1.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Sistema de referencia geoespacial"))
        self.label_3.setText(_translate("MainWindow", "SRG"))
        self.btn2.setText(_translate("MainWindow", "Ayuda"))
        self.btn3.setText(_translate("MainWindow", "Ejecutar"))
        self.btn4.setText(_translate("MainWindow", "Cerrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
