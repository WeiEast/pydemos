from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import ui_9

class TestDialog(QDialog,ui_9.Ui_Dialog):
    def __init__(self,parent=None):
        super(TestDialog,self).__init__(parent)
        self.setupUi(self)

app=QApplication(sys.argv)
dialog=TestDialog()
dialog.show()
app.exec_()