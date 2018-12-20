#!/usr/bin/python3

import sys
import platform

from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class Example(QWidget):

    # Constructur
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        # Sample button
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(10, 10)

        # Quit button
        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip("This button will close the window")
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(10, 40)

        #self.resize(250, 100)  # Größe
        #self.move(300, 300)  # Position
        self.setGeometry(300, 300, 300, 200)  # Position & Größe
        self.setWindowTitle('My Qt5 window on ' + platform.system())
        self.center()
        self.show()

    # Center frame on screen
    def center(self):
        # Rectangle specifying the geometry of the main window
        qr = self.frameGeometry()
        # 'QDesktopWidget' provides information about the user's desktop
        # Figure out screen resolution of monitor and from this resolution, get center point
        cp = QDesktopWidget().availableGeometry().center()
        # Set the center of the rectangle to the center of the screen
        qr.moveCenter(cp)
        # Move top-left point of window to top-left point of qr rectangle,
        # thus centering the window on screen
        self.move(qr.topLeft())

    # Overwrite event to close window
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# Check if this script is run as the main module
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
