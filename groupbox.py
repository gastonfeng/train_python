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
        lb = buttonwc()
        lb.setText(u'我是标签')
        lb.Closed.connect(self.on_remove_lb)
        self.groupLayout.addWidget(lb)

    @pyqtSlot(bool)
    def on_btn_del_clicked(self,b):
        self.groupLayout.removeWidget()

    def on_remove_lb(self):
        lb=self.sender()
        lb.hide()
        self.groupLayout.removeWidget(lb)

        #self.groupBox.update()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    g = gui(0, 0)
    app.exec_()
