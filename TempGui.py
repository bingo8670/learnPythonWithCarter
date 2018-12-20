# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TempGui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnFtoC = QtWidgets.QPushButton(self.centralwidget)
        self.btnFtoC.setGeometry(QtCore.QRect(240, 160, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnFtoC.setFont(font)
        self.btnFtoC.setObjectName("btnFtoC")
        self.btnCtoF = QtWidgets.QPushButton(self.centralwidget)
        self.btnCtoF.setGeometry(QtCore.QRect(240, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCtoF.setFont(font)
        self.btnCtoF.setObjectName("btnCtoF")
        self.editCel = QtWidgets.QLineEdit(self.centralwidget)
        self.editCel.setGeometry(QtCore.QRect(100, 130, 113, 41))
        self.editCel.setObjectName("editCel")
        self.spinFahr = QtWidgets.QSpinBox(self.centralwidget)
        self.spinFahr.setGeometry(QtCore.QRect(420, 130, 91, 41))
        self.spinFahr.setObjectName("spinFahr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 200, 59, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 220, 59, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnFtoC.setText(_translate("MainWindow", "<<华氏度到摄氏度"))
        self.btnCtoF.setText(_translate("MainWindow", "摄氏度到华氏度>>"))
        self.label.setText(_translate("MainWindow", "摄氏度"))
        self.label_2.setText(_translate("MainWindow", "华氏度"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
