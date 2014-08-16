import sys
from PyQt4 import QtGui


class ceshi(QtGui.QWidget):

    """docstring for ceshi"""

    def __init__(self):
        super(ceshi, self).__init__()
        self.setGeometry(120, 222, 222, 222)
        self.setWindowTitle('llala')
        self.aa = QtGui.QLabel('adfadf', self)
        self.aa.setGeometry(11, 3, 99, 99)


app = QtGui.QApplication(sys.argv)
aa = ceshi()
aa.show()

app.exec_()
