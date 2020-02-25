# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'let_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from letter import un_archived,letter_trace,get_data


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 80, 151, 21))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 40, 61, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 80, 31, 20))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 170, 261, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(70, 330, 411, 201))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 200, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 180, 71, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 150, 451, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(60, 310, 441, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 10, 421, 121))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 21))
        self.menubar.setObjectName("menubar")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actioncreator = QtWidgets.QAction(MainWindow)
        self.actioncreator.setObjectName("actioncreator")
        self.menuabout.addAction(self.actioncreator)
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.unArchiced()
        self.fillCombobox()
        self.pushButton.clicked.connect(self.record)
        self.lineEdit.returnPressed.connect(self.record)
        self.pushButton_2.clicked.connect(self.traceForm)
        self.lineEdit_2.returnPressed.connect(self.traceForm)


    def fillCombobox(self):
        recivers=['مدیر','معاون توسعه','معاون راهداری','معاون حمل و نقل',
        'معاون فنی','حراست','امور اداری','IT واحد','پیمان و رسیدگی','بایگانی']
            
        
        for x in recivers:
            self.comboBox.addItem(x)


    def record(self):
        name=self.lineEdit.text()
        self.lineEdit.clear()
        receiver=self.comboBox.currentText()
        print(name,receiver)
        get_data(name,receiver)
        

    def unArchiced(self):
        z=un_archived()
        z="---".join(z)
        self.textBrowser_2.setText(z)

    def traceForm(self):
        letter_name=self.lineEdit_2.text()
        
        z=letter_trace(letter_name)
        z="\n".join(z)
        self.textBrowser.setText(z)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ثبت و بایگانی نامه ها"))
        self.pushButton.setText(_translate("MainWindow", "ثبت"))
        self.label.setText(_translate("MainWindow", "شماره نامه"))
        self.label_2.setText(_translate("MainWindow", "گیرنده"))
        self.pushButton_2.setText(_translate("MainWindow", "جستجو"))
        self.label_3.setText(_translate("MainWindow", "شماره نامه"))
        self.groupBox_2.setTitle(_translate("MainWindow", "سوابق نامه"))
        self.groupBox_3.setTitle(_translate("MainWindow", "بایگانی نشده ها"))
        self.groupBox.setTitle(_translate("MainWindow", "ثبت نامه"))
        self.menuabout.setTitle(_translate("MainWindow", "درباره"))
        self.actioncreator.setText(_translate("MainWindow", "creator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
