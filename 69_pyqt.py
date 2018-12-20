import sys
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.resize(250, 150)
    window.move(300, 300)
    window.setWindowTitle("Simple")
    button = QtWidgets.QPushButton("Hello, PyQt!")
    window.setCentralWidget(button)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
