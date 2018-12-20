from PyQt5 import QtWidgets
from TempGui import Ui_MainWindow

class myWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent=parent)
        self.setupUi(self)
        #将事件处理器与事件相连接
        self.btnCtoF.clicked.connect(self.btnCtoF_Clicked)
        self.btnFtoC.clicked.connect(self.btnFtoC_Clicked)

    #定义CtoF时间处理器
    def btnCtoF_Clicked(self):
        cel = float(self.editCel.text())
        fahr = cel * 9.0 / 5 + 32
        self.spinFahr.setValue(int(fahr + 0.5))

    #定义CtoF时间处理器
    def btnFtoC_Clicked(self):
        fahr = self.spinFahr.value()
        cel = (fahr - 32) * 5 / 9.0
        cel_text = '%.2f'%cel
        self.editCel.setText(str(cel_text))

    def menuExit_selected(self):
        self.close()

import sys
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWindow()
    myshow.show()
    sys.exit(app.exec_())
