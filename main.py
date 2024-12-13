import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from lib.viewer_layout import Ui_MainWindow
from lib.Shopping_coupang import ShopManager
import datetime
from lib.Thread_Shopping import ScrapingThread

class Main(QMainWindow, Ui_MainWindow): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.initkeyword()
        self.initCombobox()
        self.initSignal()
        self.shopmanager = ShopManager()
        
        self.index = 0

    def initkeyword(self):
        self.keyword.setFocus(True)
        self.keyword_List.setRowCount(10)  
        self.keyword_List.setColumnCount(1) 
        self.keyword_List.setHorizontalHeaderLabels(["키워드"])
        self.keyword_List.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    def initCombobox(self):
        self.roket_delivery.addItem("전체")
        self.roket_delivery.addItem("로켓전체")
        self.roket_delivery.addItem("로켓럭셔리")
        self.roket_delivery.addItem("로켓배송")
        self.roket_delivery.addItem("로켓직구")
        
        self.Sort_Method.addItem("쿠팡 랭킹순")
        self.Sort_Method.addItem("리뷰순")
        self.Sort_Method.addItem("낮은 가격순")
        self.Sort_Method.addItem("높은 가격순")
        self.Sort_Method.addItem("판매량순")
        self.Sort_Method.addItem("최신순")
        
        
        self.append_log_msg("Program started and initialized.")

    def initSignal(self):
        self.keyword_append.clicked.connect(self.Append_items)
        self.keyword_delete.clicked.connect(self.Delete_selected_items)
        self.keyword_reset.clicked.connect(self.Reset_items)
        self.work_root.clicked.connect(self.set_save_directory)
        self.start_button.clicked.connect(self.Start_Scrapping)
        self.stop_button.clicked.connect(QApplication.instance().quit)

    def append_log_msg(self, act):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        app_msg = 'CoupangSystem-User: ' + act + ' - (' + nowDatetime + ')'
        self.Log_text.appendPlainText(app_msg) 

        with open('./log/log.txt','a') as f:
            f.write(app_msg+'\n')

    ###########################################################################################

    def Append_items(self):
        keyword_text = self.keyword.text()  
        if keyword_text: 
            self.keyword_List.clearSelection()  

            item = QTableWidgetItem(keyword_text)
            self.keyword_List.setItem(self.index, 0, item)
            self.keyword.clear()  
            self.keyword.setFocus(True)
            self.append_log_msg(f"No.{self.index+1} Keyword appended.")
            self.index += 1
        else:
            QMessageBox.about(self, "키워드 입력 오류", "키워드가 입력 안됨.")

    def Delete_selected_items(self):
        selected_rows = self.keyword_List.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.about(self, "선택 형식 오류", "선택된 행이 없습니다.")
            return
        
        for index in sorted(selected_rows, reverse=True):
            self.keyword_List.removeRow(index.row())
        self.keyword.setFocus(True)
        self.append_log_msg(f"No.{self.index+1} keyword deleted.")
        self.index -= 1
    
    def Reset_items(self):
        self.keyword_List.setRowCount(0)  
        self.initStart()
        self.append_log_msg("Keywords Initialized.")

    #####################################################################################
    def set_save_directory(self):
        self.append_log_msg(f"SaveDrictory Click.")
        self.directory = QFileDialog.getExistingDirectory(self, "저장 경로 선택")

    def Start_Scrapping(self):
        self.append_log_msg("Start Button Click.")
        self.page_text = self.page_input.text()

        if self.page_text == '':
            QMessageBox.about(self, "페이지 형식 오류", "총 페이지 수를 입력하세요.")
            return
        
        selected_sort = self.Sort_Method.currentText()
        selected_rocket = self.roket_delivery.currentText()

        self.Scraping = ScrapingThread(self.shopmanager, selected_rocket, selected_sort, 
                                       self.page_text, self.keyword_List, self.directory)
        self.thread = QThread()

        # Scraping 객체를 스레드로 이동
        self.Scraping.moveToThread(self.thread)

        # 신호 및 슬롯 연결
        self.Scraping.log_message.connect(self.append_log_msg)
        self.Scraping.finished.connect(self.thread.quit)  # 작업 완료 시 스레드 종료
        self.Scraping.finished.connect(self.Scraping.deleteLater)  # Scraping 객체 삭제
        self.thread.finished.connect(self.thread.deleteLater)  # 스레드 객체 삭제

        # 스레드 시작
        self.thread.started.connect(self.Scraping.run)
        self.thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()



    
    