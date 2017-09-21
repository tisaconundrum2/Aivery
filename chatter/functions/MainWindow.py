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
from pyAIML.core_aiml.kernel import Kernel

timer = QtCore.QTimer()


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass


class Ui_MainWindow(Ui_MainWindow, QThread, Basics):
    def __init__(self):
        super().__init__()
        self.kern = Kernel()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.normal_mode()
        self.connectWidgets()
        self.start()

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
        self.kern.set_name("Aivery")
        self.dir = '../brain'
        self.actionOn.triggered.connect(self.debug_mode)
        self.actionOff.triggered.connect(self.normal_mode)
        self.actionLoad_Brainz.triggered.connect(self.brainDir)
        self.pushButton.setShortcut("Return")
        self.pushButton.setShortcut("Enter")
        self.pushButton.clicked.connect(self.interact)
        self.actionNew_Chat.triggered.connect(self.new_chat_triggered)
        self.talkForMePushButton.clicked.connect(self.talkForMe)

    def new_chat_triggered(self):
        self.textBrowser.clear()
        self.start()

    def brainDir(self):
        # TODO add a Qsetting in here to remember where the brains are.
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Brain Directory", '.')
        self.start()

    def run(self):
        if os.path.exists(self.dir):
            for file in os.listdir(self.dir):
                if file.endswith(".aiml"):
                    print("Loaded: {}".format(file))
                    self.kern.learn(os.path.join(self.dir, file))
                    self.flag = True
            print("{}: {}".format(self.kern.get_name(), "Brain dump is done."))
            print("{}: {}".format(self.kern.get_name(), "You may now talk to me."))
        else:
            print("{}: {}".format(self.kern.get_name(), "I couldn't upload my memory"))
            print("{}: {}".format(self.kern.get_name(), "Please click File and locate my memory"))

    def interact(self):
        if self.flag:
            self.textBrowser.clear()
            self.flag = False
        print("You: " + self.lineEdit.text())
        self.response = self.kern.respond(self.lineEdit.text())
        self.lineEdit.clear()
        timer.singleShot((len(self.response) * 30),
                         lambda: print("{}: {}".format(self.kern.get_name(), self.response)))
        self.lineEdit.clear()
        timer.singleShot((len(response) * 30),
                         lambda: print("{}: {}".format(self.kern.get_name(), response)))


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
