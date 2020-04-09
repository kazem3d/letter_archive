# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'let_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from letter import record_in_database,read_from_datebase,delete_from_database,today_date
import jdatetime


class Ui_MainWindow(object):

    def fill_tabel(self):
        tabel_list=read_from_datebase()
        match_row=[]
        self.tableWidget.setRowCount(0)
        for row_id , row_data in enumerate(tabel_list):
            
            match_row=row_data
            # print(match_row)


            self.tableWidget.insertRow(row_id)
            row_data=tabel_list[row_id]
            for column_id , column_data in enumerate(row_data) :
                # if type(column_data) is float:
                   
                #     column_data=int(column_data)
                self.tableWidget.setItem(row_id,column_id,QtWidgets.QTableWidgetItem(str(column_data)))


                d1=jdatetime.date.today()
                D=int((row_data[3].split('/'))[2])
                M=int((row_data[3].split('/'))[1])
                Y=int((row_data[3].split('/'))[0])
                d2=jdatetime.date(Y,M,D)
             
                if d1 == d2:
                    self.tableWidget.item(row_id,column_id).setBackground(QtGui.QColor(102, 255, 51))


                elif d1 > d2:
            
                    self.tableWidget.item(row_id,column_id).setBackground(QtGui.QColor(255, 55, 5))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(60, 180, 781, 281))
        self.groupBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 751, 251))
        font = QtGui.QFont()
        font.setFamily("B Homa")
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 55, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 1, item)

        #just resize end coulumn
        header=self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)


        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 10, 781, 161))
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(690, 30, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(502, 30, 171, 20))
        font = QtGui.QFont()
        font.setFamily("B Homa")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(690, 70, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(396, 30, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(182, 30, 191, 20))
        font = QtGui.QFont()
        font.setFamily("B Homa")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(310, 70, 61, 22))
        font = QtGui.QFont()
        font.setFamily("B Homa")
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(380, 70, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(690, 120, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(262, 120, 411, 20))
        font = QtGui.QFont()
        font.setFamily("B Homa")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(250, 70, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(60, 92, 91, 31))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(500, 70, 171, 22))
        font = QtGui.QFont()
        font.setFamily("B Homa")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setObjectName("comboBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 470, 421, 81))
        self.groupBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(40, 20, 341, 41))
        font = QtGui.QFont()
        font.setFamily("B Lotus")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        #change label7 to red
        pal = self.label_7.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
        self.label_7.setPalette(pal)
        self.label_7.setText("I am trying to make this red?")


        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(260, 500, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(170, 500, 81, 21))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setObjectName("label_9")
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 21))
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

        self.fillCombobox()
        self.fill_tabel()
        self.pushButton.clicked.connect(self.record)
        self.lineEdit.returnPressed.connect(self.record)
        self.label_9.setText(today_date)
        self.tableWidget.cellDoubleClicked.connect(self.delete)


    def fillCombobox(self):
        recivers=['معاون راهداری','معاون توسعه','معاون حمل و نقل','معاون فنی',
                     'حراست','امور اداری','حقوقی','برنامه و بودجه','دفتر']
            
        
        for x in recivers:
            self.comboBox.addItem(x)



    def delete(self):
        row = self.tableWidget.currentRow()
        # column = self.tableWidget.currentColumn()
        self.item = self.tableWidget.item(row, 0) 
        name = self.item.text() 
        delete_from_database(name)
        print('deleted %s' %name)
        self.fill_tabel()
        self.label_7.setText('نامه شماره %s حذف شد' %name)
           

    # def delete(self):
    #     name=self.lineEdit_5.text()
    #     self.lineEdit_5.clear()
    #     delete_from_database(name)
    #     print('deleted')
    #     self.fill_tabel()


    def record(self):
        name=self.lineEdit.text()
        self.lineEdit.clear()
        receiver=self.comboBox.currentText()
        letter_date=self.lineEdit_3.text()
        self.lineEdit_3.clear()
        description=self.lineEdit_4.text()
        self.lineEdit_4.clear()
        deadline=int(self.spinBox.text())
        self.spinBox.clear()
        self.spinBox.setValue(0)
        
        record_in_database(name,letter_date,deadline,receiver,description)
        self.fill_tabel()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "پیگیری نامه ها"))
        self.groupBox_3.setTitle(_translate("MainWindow", "لیست نامه ها"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "شماره نامه"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "تاریخ نامه"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "تاریخ ارجاء"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "مهلت نامه"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "گیرنده"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "توضیحات"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "323"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "ثبت نامه"))
        self.label.setText(_translate("MainWindow", "شماره نامه :"))
        # self.lineEdit.setText(_translate("MainWindow", "32323"))
        self.label_2.setText(_translate("MainWindow", "گیرنده :"))
        self.label_3.setText(_translate("MainWindow", "تاریخ نامه :"))
        self.label_4.setText(_translate("MainWindow", "مهلت نامه :"))
        self.label_5.setText(_translate("MainWindow", "توضیحات :"))
        self.label_6.setText(_translate("MainWindow", "روز"))
        self.pushButton.setText(_translate("MainWindow", "ثبت"))
        self.groupBox_2.setTitle(_translate("MainWindow", "حذف نامه"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f80000;\"></span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "تاریخ امروز :"))
        self.label_9.setText(_translate("MainWindow", "1399/01/01"))
        self.menuabout.setTitle(_translate("MainWindow", "about"))
        self.actioncreator.setText(_translate("MainWindow", "تهیه کننده کاظم قناتی"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())