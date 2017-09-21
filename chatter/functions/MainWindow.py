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
from chatter.util.excepthook import my_exception_hook
from pyAIML.Kernel import Kernel

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass


class Ui_MainWindow(Ui_MainWindow, Basics):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.connectWidgets()
        self.normal_mode()

    def normal_mode(self):
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = sys.__stderr__
        # sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)
        self.actionOn.setDisabled(False)
        self.actionOff.setDisabled(True)

    def debug_mode(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__
        self.actionOn.setDisabled(True)
        self.actionOff.setDisabled(False)

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