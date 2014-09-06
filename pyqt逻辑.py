#! python3
from qtui import Ui_Form
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QInputDialog
import sys
from lxml import _elementpath


class myqt(QtWidgets.QWidget, Ui_Form):

    """docstring for myqt"""

    def __init__(self):
        super(myqt, self).__init__()
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
aa = myqt()
aa.show()
sys.exit(app.exec_())
