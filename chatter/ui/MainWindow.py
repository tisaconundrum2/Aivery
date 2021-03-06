# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tisaconundrum\Documents\GitHub\Aivery\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 525)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/robot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.talkForMePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.talkForMePushButton.setObjectName("talkForMePushButton")
        self.horizontalLayout.addWidget(self.talkForMePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 393, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuDebug = QtWidgets.QMenu(self.menuHelp)
        self.menuDebug.setObjectName("menuDebug")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Chat = QtWidgets.QAction(MainWindow)
        self.actionNew_Chat.setObjectName("actionNew_Chat")
        self.actionYou_Don_t_Need_Help = QtWidgets.QAction(MainWindow)
        self.actionYou_Don_t_Need_Help.setObjectName("actionYou_Don_t_Need_Help")
        self.actionOn = QtWidgets.QAction(MainWindow)
        self.actionOn.setObjectName("actionOn")
        self.actionOff = QtWidgets.QAction(MainWindow)
        self.actionOff.setObjectName("actionOff")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLoad_Brainz = QtWidgets.QAction(MainWindow)
        self.actionLoad_Brainz.setObjectName("actionLoad_Brainz")
        self.menuFile.addAction(self.actionNew_Chat)
        self.menuFile.addAction(self.actionLoad_Brainz)
        self.menuDebug.addAction(self.actionOn)
        self.menuDebug.addAction(self.actionOff)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.menuDebug.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aivery"))
        self.textBrowser.setToolTip(_translate("MainWindow", "<html><head/><body><p>The box in which you see your chat</p></body></html>"))
        self.textBrowser.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Type Here</p></body></html>"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Send your messages to the bot</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.talkForMePushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Make the bot talk to itself</p></body></html>"))
        self.talkForMePushButton.setText(_translate("MainWindow", "Talk for me"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuDebug.setTitle(_translate("MainWindow", "Debug"))
        self.actionNew_Chat.setText(_translate("MainWindow", "New Chat"))
        self.actionYou_Don_t_Need_Help.setText(_translate("MainWindow", "You Don\'t Need Help"))
        self.actionOn.setText(_translate("MainWindow", "On"))
        self.actionOff.setText(_translate("MainWindow", "Off"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLoad_Brainz.setText(_translate("MainWindow", "Load Brainz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

