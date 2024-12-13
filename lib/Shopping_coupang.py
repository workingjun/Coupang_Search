from bs4 import BeautifulSoup
import re
import requests

class ShopManager:       
        def __init__(self):
                self.header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.9"}
                (self.link_list, self.imageLink_list, self.title_list, 
                self.price_list, self.point_list, self.delivery_list, self.rocket_list) = [], [], [], [], [], [], [] 
        
        def set_keyword(self, keyword):
                self.keyword = keyword
                self.url = f"https://www.coupang.com/np/search?&q={self.keyword}&filterType=&page=&sorter=scoreDesc&listSize=72"
                
        def move_page(self, page_num):
                self.url = re.sub(r'page=\d+', f'page={page_num}', self.url)

        def Append_rocket(self, trend_option):
                if '로켓전체' in trend_option:
                        self.url = re.sub(r"&filterType[^&]*", "&filterType=rocket_luxury%2Crocket%2Ccoupang_global", self.url)
                        
                elif '로켓럭셔리' in trend_option:
                        self.url = re.sub(r"&filterType[^&]*", "&filterType=rocket_luxury", self.url)
                        
                elif '로켓배송' in trend_option:
                        self.url = re.sub(r"&filterType[^&]*", "&filterType=rocket", self.url)
                
                elif '로켓직구' in trend_option:
                        self.url = re.sub(r"&filterType[^&]*", "&filterType=coupang_global", self.url)
                
        def Append_sorting(self, sort_option):
                if '판매량순' in sort_option:
                        self.url = re.sub(r"&sorter[^&]*", "&sorter=saleCountDesc", self.url)
                        
                elif '낮은 가격순' in sort_option:
                        self.url = re.sub(r"&sorter[^&]*", "&sorter=salePriceAsc", self.url)
                        
                elif '높은 가격순' in sort_option:
                        self.url = re.sub(r"&sorter[^&]*", "&sorter=salePriceDesc", self.url)
                
                elif '최신순' in sort_option:
                        self.url = re.sub(r"&sorter[^&]*", "&sorter=latestAsc", self.url)
                                
        def Find_ShoppingList(self, page_num=1):
                if page_num != 1:
                        self.move_page(page_num)

                self.raw = requests.get(self.url, headers=self.header) 
                self.search = BeautifulSoup(self.raw.text, 'html.parser')

                self.box = self.search.find('ul', {'id' : 'productList'})
                self.all_product = self.box.find_all('li', {'class': 'search-product'})

                for product in self.all_product:
                        imagefind = product.find("img", {'class' : 'search-product-wrap-img'})
                        if imagefind.get("data-img-src") is None:
                                imageLink = "http:" + imagefind.get('src')
                        else:
                                imageLink = "http:" + imagefind.get("data-img-src")

                        title = product.find('div', {'class' : 'name'})
                        price = product.find('strong', {'class' : 'price-value'})
                        point = product.find('span', {'class' : 'rating-total-count'})
                        link_humi = product.find('a')['href']
                        
                        link = "https://www.coupang.com" + link_humi
                        self.imageLink_list.append(imageLink)
                        self.link_list.append(link)    

                        if title is None:
                                self.title_list.append('')
                        else:
                                self.title_list.append(title.text.strip())

                        if price is None:
                                self.price_list.append('')
                        else:
                                self.price_list.append(price.text)
                        
                        if point is None:
                                self.point_list.append('')
                        else:
                                self.point_list.append(point.text)
                        
                        try:
                                delivery = product.find('span', {'class': 'arrival-info'})
                                rocket = product.find('span', {'class': 'badge rocket'})
                        except:
                                pass
                        else:
                                if rocket is None:
                                        self.rocket_list.append('')
                                else:
                                        src_link = rocket.find("img")['src']
                                        if src_link == "https://image6.coupangcdn.com/image/delivery_badge/default/pc/global_b/global_b.png":
                                                self.rocket_list.append('로켓직구')
                                        elif src_link == 'https://image6.coupangcdn.com/image/cmg/icon/ios/logo_rocket_large@3x.png':
                                                self.rocket_list.append('로켓배송')
                                        elif src_link == 'https://image7.coupangcdn.com/image/coupang/rds/logo/iphone_2x/logoRocketMerchantLargeV3R3@2x.png':
                                                self.rocket_list.append('판매자로켓')
                                        elif src_link == 'https://image9.coupangcdn.com/image/badges/falcon/v1/web/rocket_luxury@2x.png':
                                                self.rocket_list.append('로켓럭셔리')

                                if delivery is None:
                                        self.delivery_list.append('')
                                else:
                                        self.delivery_list.append(delivery.text.strip())

        def Return_Lists(self):
                return (self.link_list, self.imageLink_list, self.title_list, self.price_list, self.point_list, self.delivery_list, self.rocket_list)  


if __name__=="__main__":
        shopmanager = ShopManager()
        shopmanager.set_keyword("노트북")
        (link_list, imageLink_list, title_list, 
        price_list, point_list, delivery_list, rocket_list) = shopmanager.Find_ShoppingList()

        print(title_list)
        print(delivery_list)
        print(rocket_list)
        