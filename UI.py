# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from Jarvis import Jarvis

class Ui_MainWindow(object):

    text = "Say something....."

    def setupUi(self, MainWindow):

        sheet = """
        
                QMainWindow{
                    background-image: url(background.jpg);
                }
                
                QLabel#video_label{
                    top: 100px;
                }
                
                QLabel#status_label{
                    background-color: rgb(180,255,160);
                    text-align: right;
                }
                
                QPushButton{
                    background-color: rgb(53,200,255,0);
                    text-align: center;
                }
                """

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(sheet)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.video = QtWidgets.QLabel(self.centralwidget)
        self.video.setGeometry(160, 70, 481, 240)
        self.video.setFont(font)
        self.video.setObjectName("video_label")
        self.video.setAlignment(Qt.Qt.AlignCenter)
        self.movie = QtGui.QMovie("gif1.gif")
        self.video.setMovie(self.movie)
        self.movie.start()

        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(160, 350, 481, 50))
        self.status_label.setFont(font)
        # self.status_label.setStyleSheet("text-align: center;")
        self.status_label.setObjectName("status_label")
        self.status_label.setStyleSheet(sheet)
        self.status_label.setAlignment(Qt.Qt.AlignCenter)

        self.give_command = QtWidgets.QPushButton(self.centralwidget)
        self.give_command.setGeometry(QtCore.QRect(340, 500, 50, 50))
        self.give_command.setObjectName("give_command")
        self.give_command.setStyleSheet(sheet)
        self.give_command.setIcon(QtGui.QIcon("mic.png"))
        self.give_command.setIconSize(QtCore.QSize(70,70))
        self.give_command.resize(70, 70)

        # self.mic = QtWidgets.QLabel(self.centralwidget)
        # self.mic.setGeometry(QtCore.QRect(340, 450, 121, 45))
        # self.mic.setPixmap(QtGui.QPixmap("mic.png"))
        # self.mic.setScaledContents(True)
        # self.mic.resize(100, 100)
        # self.mic.setObjectName("mic_label")
        # self.mic

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def mic_clicked(self):
        j = Jarvis()
        self.text = j.text
        j.start()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.give_command.setText(_translate("MainWindow", "Give Command"))
        self.status_label.setText(_translate("MainWindow", self.text))
        self.give_command.clicked.connect(self.mic_clicked)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



# 20002692506125592
# 20112692506162404-RAIYAN