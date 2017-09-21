import os
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
        self.normal_mode()
        self.processBrain()
        self.connectWidgets()

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

    def normalOutputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def connectWidgets(self):
        self.actionOn.triggered.connect(self.debug_mode)
        self.actionOff.triggered.connect(self.normal_mode)
        self.pushButton.setShortcut("Return")
        self.pushButton.clicked.connect(self.userPrint)

    def processBrain(self):
        dir = 'brain'
        if os.path.exists(dir):
            for file in os.listdir(dir):
                if file.endswith(".aiml"):
                    k.learn(os.path.join(dir, file))
        else:
            print("AI: I'm broken without a brain")

    def userPrint(self):
        print("You: " + self.lineEdit.text())
        self.lineEdit.clear()


def get_splash(app):
    """
    Get the splash screen for the application
    But check to see if the image even exists
    :param app:
    :return:
    """
    dir = '../images/'
    if os.path.exists(dir + 'robot.png'):
        splash_pix = QPixmap(dir + 'robot.png')  # default
        app_icon = QtGui.QIcon(dir + 'robot.png')
        app.setWindowIcon(app_icon)
        splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        splash.setMask(splash_pix.mask())
        splash.show()
        time.sleep(0.6)
        app.processEvents()


def main():
    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

    app = QtWidgets.QApplication(sys.argv)
    get_splash(app)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
