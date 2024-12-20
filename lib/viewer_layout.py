from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 832)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 681, 811))

        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(9)

        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.keywordBox = QtWidgets.QGroupBox(self.tab)
        self.keywordBox.setGeometry(QtCore.QRect(10, 3, 651, 111))
        self.keywordBox.setFont(font)
        self.keywordBox.setObjectName("keywordBox")
        self.keyword = QtWidgets.QLineEdit(self.keywordBox)
        self.keyword.setGeometry(QtCore.QRect(10, 17, 631, 41))
        self.keyword.setObjectName("keyword")
        self.keyword_append = QtWidgets.QPushButton(self.keywordBox)
        self.keyword_append.setGeometry(QtCore.QRect(10, 62, 191, 41))
        self.keyword_append.setObjectName("keyword_append")
        self.keyword_delete = QtWidgets.QPushButton(self.keywordBox)
        self.keyword_delete.setGeometry(QtCore.QRect(460, 62, 181, 41))
        self.keyword_delete.setObjectName("keyword_delete")
        self.keyword_reset = QtWidgets.QPushButton(self.keywordBox)
        self.keyword_reset.setGeometry(QtCore.QRect(240, 62, 181, 41))
        self.keyword_reset.setObjectName("keyword_reset")
        self.keyword_ListBox = QtWidgets.QGroupBox(self.tab)
        self.keyword_ListBox.setGeometry(QtCore.QRect(10, 120, 651, 281))
        self.keyword_ListBox.setFont(font)
        self.keyword_ListBox.setObjectName("keyword_ListBox")
        self.keyword_List = QtWidgets.QTableWidget(self.keyword_ListBox)
        self.keyword_List.setGeometry(QtCore.QRect(10, 22, 631, 251))
        self.keyword_List.setObjectName("keyword_List")
        
        self.page_box = QtWidgets.QGroupBox(self.tab)
        self.page_box.setGeometry(QtCore.QRect(10, 410, 651, 61))
        self.page_box.setObjectName("page_box")
        self.page_input = QtWidgets.QLineEdit(self.page_box)
        self.page_input.setGeometry(QtCore.QRect(105, 20, 541, 31))
        self.page_input.setObjectName("page_input")
        self.page_Label = QtWidgets.QLabel(self.page_box)
        self.page_Label.setGeometry(QtCore.QRect(12, 22, 91, 31))
        self.page_Label.setObjectName("page_Label")
        self.delivery_box = QtWidgets.QGroupBox(self.tab)
        self.delivery_box.setGeometry(QtCore.QRect(10, 470, 151, 61))
        self.delivery_box.setObjectName("delivery_box")
        self.roket_delivery = QtWidgets.QComboBox(self.delivery_box)
        self.roket_delivery.setGeometry(QtCore.QRect(5, 20, 141, 31))
        self.roket_delivery.setObjectName("roket_delivery")
        self.Sort_box = QtWidgets.QGroupBox(self.tab)
        self.Sort_box.setGeometry(QtCore.QRect(170, 470, 151, 61))
        self.Sort_box.setObjectName("Sort_box")
        self.Sort_Method = QtWidgets.QComboBox(self.Sort_box)
        self.Sort_Method.setGeometry(QtCore.QRect(6, 20, 141, 31))
        self.Sort_Method.setObjectName("Sort_Method")
        self.work_box = QtWidgets.QGroupBox(self.tab)
        self.work_box.setGeometry(QtCore.QRect(330, 470, 331, 61))
        self.work_box.setObjectName("work_box")
        self.work_root = QtWidgets.QToolButton(self.work_box)
        self.work_root.setGeometry(QtCore.QRect(8, 20, 121, 33))
        self.work_root.setObjectName("work_root")
        self.start_button = QtWidgets.QPushButton(self.work_box)
        self.start_button.setGeometry(QtCore.QRect(134, 20, 91, 33))
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.work_box)
        self.stop_button.setGeometry(QtCore.QRect(231, 20, 91, 33))
        self.stop_button.setObjectName("stop_button")
        self.Log_box = QtWidgets.QGroupBox(self.tab)
        self.Log_box.setGeometry(QtCore.QRect(10, 540, 651, 231))
        self.Log_box.setObjectName("Log_box")
        self.Log_text = QtWidgets.QPlainTextEdit(self.Log_box)
        self.Log_text.setReadOnly(True)
        self.Log_text.setGeometry(QtCore.QRect(10, 20, 631, 201))
        self.Log_text.setObjectName("Log_text")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "쿠팡 소싱 시스템"))
        self.keywordBox.setTitle(_translate("MainWindow", "키워드 "))
        self.keyword_append.setText(_translate("MainWindow", "키워드 추가"))
        self.keyword_delete.setText(_translate("MainWindow", "키워드 삭제"))
        self.keyword_reset.setText(_translate("MainWindow", "키워드 초기화"))
        self.keyword_ListBox.setTitle(_translate("MainWindow", " 키워드 목록"))
        self.page_box.setTitle(_translate("MainWindow", "페이지 설정"))
        self.page_Label.setText(_translate("MainWindow", "총페이지수"))
        self.delivery_box.setTitle(_translate("MainWindow", "로켓배송조회"))
        self.Sort_box.setTitle(_translate("MainWindow", "정렬방식"))
        self.work_box.setTitle(_translate("MainWindow", "작업시작"))
        self.work_root.setText(_translate("MainWindow", "저장경로열기"))
        self.start_button.setText(_translate("MainWindow", "시작"))
        self.stop_button.setText(_translate("MainWindow", "종료"))
        self.Log_box.setTitle(_translate("MainWindow", "로그"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "키워드 조회"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
