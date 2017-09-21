import os.path
import sys
import time

from PyQt5 import Qt
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen

from chatter.ui.MainWindow import Ui_MainWindow
from chatter.util.BasicFunctionality import Basics


class Ui_MainWindow(Ui_MainWindow, Basics):
    def setupUi(self, MainWindow):
        super().setupUi()

    def connectWidgets(self):
        self.se


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())