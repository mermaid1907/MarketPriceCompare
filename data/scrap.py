from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from tqdm import *
import pandas as pd
import requests
import time


class CarrefourScraper:
    
    def __init__(self, market_name):
        self.market_name = market_name
        self.category_links = list()
        self.products= list()
        
    def get_links(self):
        base_url = "https://www.carrefoursa.com"
        r = requests.get(base_url)
        soup = BeautifulSoup(r.content, 'lxml')
        category_list = list(soup.find_all('a', class_ = 'main-menu-dropdown-item-link'))
        for item in category_list:
            self.category_links.append(base_url + item['href'] + '?q=%3Arelevance&show=All')
        

    def get_names_and_prices(self):
        
        for link in tqdm(self.category_links):
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'lxml')
            
            product_list = soup.find_all('li', {'class':'product-listing-item'})
            
            for li in product_list:
                try:
                    name = li.find("span", {"class":"item-name"})
                    stripped_name = name.text.strip().replace(" ", "_")
                    
                    price = li.find("span", {"class":"item-price"})
                    stripped_price = float(price.text.strip("TL").replace(",", "."))
                    
                    self.products.append([stripped_name, stripped_price])
      
                    #print(self.products)
                    
                except Exception as e:
                    print(e)                
    
    def save_data(self):
        #saving data to excel
        data = pd.DataFrame(self.products, columns = ["Product Name", "Price"])
        data.to_csv('.\\carrefour_data.csv', encoding='utf-8', index=False)

    

class Migros:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.maximize_window()
        self.browser.implicitly_wait(2)
        self.links = ["https://www.migros.com.tr/meyve-sebze-c-2",
                      "https://www.migros.com.tr/et-tavuk-balik-c-3",
                      "https://www.migros.com.tr/sut-kahvaltilik-c-4",
                      "https://www.migros.com.tr/temel-gida-c-5",
                      "https://www.migros.com.tr/meze-hazir-yemek-donuk-c-7d",
                      "https://www.migros.com.tr/firin-pastane-c-7e",
                       "https://www.migros.com.tr/dondurma-c-41b",
                       "https://www.migros.com.tr/atistirmalik-c-113fb",
                       "https://www.migros.com.tr/icecek-c-6",
                       "https://www.migros.com.tr/deterjan-temizlik-c-7",
                      "https://www.migros.com.tr/kisisel-bakim-kozmetik-c-8",
                       "https://www.migros.com.tr/bebek-c-9",
                       "https://www.migros.com.tr/ev-yasam-c-a",
                       "https://www.migros.com.tr/kitap-kirtasiye-oyuncak-c-118ec",
                       "https://www.migros.com.tr/cicek-c-502",
                       "https://www.migros.com.tr/pet-shop-c-a0",
                       "https://www.migros.com.tr/elektronik-c-a6"]
        
    def getNamesAndPrice(self):

        namesList = []
        pricesList = []
        for link in tqdm(self.links):
            self.browser.get(link)
            self.browser.implicitly_wait(3)
            while True:
                cards = self.browser.find_elements(By.CLASS_NAME, 'mat-mdc-card')
                self.browser.implicitly_wait(3)

                for card in cards:
                    try:
                        names = card.find_element(By.CLASS_NAME, 'product-name')
                        prices = card.find_element(By.CLASS_NAME, 'amount')
                        pricesList.append(float(prices.text.strip("TL").replace(" ", "").strip(".").replace(",",".")))
                        namesList.append(names.text)
                    except:
                        print("No Product")

                self.browser.implicitly_wait(1)
                self.browser.execute_script("window.scrollBy(0,800)")
                self.browser.implicitly_wait(2)
            
                pageWay = self.browser.find_element(By.ID, 'pagination-button-next')
                
                if pageWay.is_enabled() == False:
                    break
                
                else:
                    pageWay.click()


        products = zip(namesList,pricesList)            
        data = pd.DataFrame(products,columns=["Product Name","Price"])
        data.to_csv(".\\migros_data.csv", encoding="utf-8",index=False)

        self.browser.quit()
        
    
if __name__ == '__main__':
    '''
    carrefour = CarrefourScraper("Carrefour")
    carrefour.get_links()
    carrefour.get_names_and_prices()
    carrefour.save_data()
    '''
    migros = Migros()
    migros.getNamesAndPrice()
