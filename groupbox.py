# coding=utf-8
import sys

from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot

from pyqtmate.buttonwithclose import buttonwc
from pyqtmate.guiqt import ui_compile, guiqt

ui_compile('groupbox')
from uigroupbox import Ui_MainWindow


class gui(guiqt, Ui_MainWindow):
    def __init__(self, splash, odoo, *args):
        guiqt.__init__(self, *args)

    @pyqtSlot(bool)
    def on_btn_add_clicked(self,b):
        lb = buttonwc(self.groupBox)
        lb.setText(u'我是标签')
        self.groupBox.update()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    g = gui(0, 0)
    app.exec_()
