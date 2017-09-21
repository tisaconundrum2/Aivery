# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tisaconundrum\Documents\GitHub\Aivery\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
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

