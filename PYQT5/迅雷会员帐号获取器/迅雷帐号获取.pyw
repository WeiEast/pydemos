from qtui import Ui_Form
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QInputDialog
import sys
import requests
import re
import os
from ahk import goahk
import lxml.html
from lxml import _elementpath


class myqt(QtWidgets.QWidget, Ui_Form):

    """docstring for myqt"""

    def __init__(self):
        super(myqt, self).__init__()
        self.setupUi(self)
        goahk('''
            forf1=
            forf2=
            F1::
            send ^a%forf1%{Tab}%forf2%
            sleep 150
            send {enter}


            return
            F3::
            run,taskkill /F /IM py.exe
            run,taskkill /F /IM python.exe
            run,taskkill /F /IM pythonw.exe
            exitapp
            return
            ''')
        self.aa, self.bb = self.getid()
        self.labeltime.setText(self.bb)
        for i in self.aa:
            self.listWidget.addItem('------'.join(i))
        self.listWidget.itemClicked.connect(self.bindll)
        self.pushButton.clicked.connect(self.suiji)

    def suiji(self):
        import random
        # 迅雷7登录
        self.ra, self.rb = random.choice(self.aa)
        goahk(r'''
            forf1={}
            forf2={}
            WinActivate 迅雷7登录
            click 91,291
            Click 0, 0, 0
            send ^a%forf1%{{Tab}}%forf2%
            sleep 150
            send {{enter}}
           
            '''.format(self.ra, self.rb))

    def bindll(self, item):
        ss = item.text()
        self.labelxuan.setText(ss)
        sss = ss.split('------')
        self.ab = sss[0]
        self.cd = sss[1]
        goahk('''
            forf1={}
            forf2={}
            '''.format(self.ab, self.cd))

    def getid(self):
        r = requests.get('http://www.fenxs.com/category/gongxiang')
        doc = lxml.html.fromstring(r.text)
        aa = doc.xpath('//article//h2/a/@title')
        bb = doc.xpath('//article//h2/a/@href')
        cc = tuple(zip(aa, bb))
        for i in cc:
            if '迅雷会员账号分享' in i[0]:
                url = i[1]

                break
        r = requests.get(url)
        doc = lxml.html.fromstring(r.text)
        aa = doc.xpath(
            '//div/article[@class="article-content"]/p[last()-1]//text()')
        tt = doc.xpath('//title/text()')[0]
        tt = re.findall('\d+月\d+日', tt)[0]
        aa = ''.join(aa)
        zhanghao = re.findall('号(.*?)分', aa)
        mima = re.findall('码(.*?)\n', aa)
        return list(zip(zhanghao, mima)), tt


app = QtWidgets.QApplication(sys.argv)
aa = myqt()
aa.show()
sys.exit(app.exec_())
