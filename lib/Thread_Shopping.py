from PyQt5.QtCore import QObject, pyqtSignal
import xlsxwriter
from urllib.request import urlopen
from io import BytesIO
from PIL import Image
from lib.Sorting_items import SortManager
from urllib.error import URLError, HTTPError
from PIL import UnidentifiedImageError

class ScrapingThread(QObject):
    log_message = pyqtSignal(str)
    finished = pyqtSignal()  # 작업 완료 신호 추가

    def __init__(self, shopmanager, selected_rocket, selected_sort, page_text, keyword_List, directory):
        super().__init__()
        self.shopmanager = shopmanager
        self.selected_rocket = selected_rocket
        self.selected_sort = selected_sort
        self.page_text = page_text
        self.keyword_List = keyword_List
        self.directory = directory
        self._is_running = True  # 작업 중인지 확인하는 플래그
        self._is_sorting = False
        self.sortmanager = SortManager()

    def run(self):
        all_data = []
        row_count = self.keyword_List.rowCount()

        for row in range(row_count):
            if not self._is_running:  # 작업 취소가 요청된 경우
                break
            item = self.keyword_List.item(row, 0)
            if item is not None:
                all_data.append(item.text())

        file_path = rf"{self.directory}/ShopList.xlsx"
        self.workbook = xlsxwriter.Workbook(file_path)
        self.cell_format = self.workbook.add_format({'text_wrap': True}) ##자동 줄바꿈

        try:
            for item in all_data:
                if not self._is_running:  # 작업 취소가 요청된 경우
                    break

                self.shopmanager.set_keyword(item)
                page_index = 1  

                self.shopmanager.Append_rocket(self.selected_rocket)
                if self.selected_sort == "리뷰순":
                    self._is_sorting = True
                else:
                    self.shopmanager.Append_sorting(self.selected_sort)

                while page_index <= int(self.page_text):
                    if not self._is_running:  # 작업 취소가 요청된 경우
                        break

                    self.shopmanager.Find_ShoppingList(page_index)
                    page_index += 1

                (self.link_list, self.imageLink_list, self.title_list, 
                self.price_list, self.point_list, self.delivery_list, self.rocket_list) = self.shopmanager.Return_Lists()
                self.log_message.emit(f"{item} - Coupang Shopping finished.")

                if self._is_sorting:
                    items_inItem = list(zip(self.link_list, self.imageLink_list, self.title_list, 
                                        self.price_list, self.point_list, self.delivery_list, self.rocket_list))
                    sorted_items = self.sortmanager.sort_items(items_inItem)
                    (self.link_list, self.imageLink_list, self.title_list, 
                    self.price_list, self.point_list, self.delivery_list, self.rocket_list) = zip(*sorted_items)

                worksheet = self.workbook.add_worksheet(item)
                for i in range(7):
                    worksheet.set_column(i, i, 15)
                for row_num in range(len(self.link_list)):
                    if not self._is_running:  # 작업 취소가 요청된 경우
                        break
                    worksheet.set_row(row_num + 1, 100)
                    worksheet.write(row_num + 1, 0, self.link_list[row_num], self.cell_format)
                    worksheet.write(row_num + 1, 2, self.title_list[row_num], self.cell_format)
                    worksheet.write(row_num + 1, 3, self.price_list[row_num], self.cell_format)
                    worksheet.write(row_num + 1, 4, self.point_list[row_num], self.cell_format)
                    worksheet.write(row_num + 1, 5, self.delivery_list[row_num], self.cell_format)
                    worksheet.write(row_num + 1, 6, self.rocket_list[row_num], self.cell_format)
                
                    try:
                        image = Image.open(BytesIO(urlopen(self.imageLink_list[row_num]).read()))
                        image = image.resize((100, 100))  
                        image_stream = BytesIO()
                        image.save(image_stream, format='PNG')
                        image_stream.seek(0)
                        worksheet.insert_image(row_num + 1, 1, 'image.png', {'image_data': image_stream})
                    except HTTPError as e:
                        self.log_message.emit(f"HTTP Error: {e.code} for URL")
                    
                    except URLError as e:
                        self.log_message.emit(f"Failed to reach the server. Reason: {e.reason} for URL: {self.imageLink_list[row_num]}")
                    
                    except UnidentifiedImageError:
                        self.log_message.emit(f"Failed to identify image file from URL: {self.imageLink_list[row_num]}")
                    
                    except Exception as e:
                        self.log_message.emit(f"Unexpected error: {str(e)} occurred while processing image from URL: {self.imageLink_list[row_num]}")

                self.log_message.emit(f"{item} - Appending WorkSheet finished.")
        except Exception as e:
            self.log_message.emit(f"Error : {str(e)}")
        else:
            self.finished.emit()  # 작업 완료 신호 발행
            self.log_message.emit("ShoppingList was restored in your Filepath.")
        finally:
            self.workbook.close()
    
    def stop(self):
        """작업 중지 요청을 처리합니다."""
        self._is_running = False

        
    
