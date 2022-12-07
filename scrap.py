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
import csv

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
                    stripped_name = name.text.strip()
                    
                    price = li.find("span", {"class":"item-price"})
                    stripped_price = price.text.strip("TL")
                    
                    self.products.append([stripped_name, stripped_price])
      
                    print(self.products)
                    
                except Exception as e:
                    print(e)                
    
    def save_data(self):
        #saving data to excel
        data = pd.DataFrame(self.products, columns = ["Product Name", "Price"])
        data.to_csv('.\\carrefour_data.csv', encoding='utf-8', index=False)

    
class MigrosScraper:
    
    def __init__(self, market_name):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.browser = webdriver.Chrome(PATH)
        
        #in addition to prevent the code from "1048 Failed to read descriptor from node connection"
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        self.browser = webdriver.Chrome(options=options)
        self.market_name = market_name
        
        self.links = list()
        self.products= list()
        
    def get_links(self):
        self.browser.get("https://www.migros.com.tr")
        time.sleep(1)
        #ok = WebDriverWait(self.browser, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.mdc-button'))).click()
        
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
        
              
    def get_names_and_prices(self):
   
        page = 1
        name_list = list()
        price_list = list()
        there_is_next_page = True
        
        for link in tqdm(self.links):
            
            while there_is_next_page:
                r = self.browser.get(link+f'/?sayfa={page}')
                time.sleep(2)
                
            
                container = self.browser.find_element(By.XPATH, '/html/body/sm-root/div/main/sm-product/article/sm-list/div/div[4]/div[2]/div[4]')

                try:
                    names = container.find_elements(By.CSS_SELECTOR, 'a.product-name')
                    prices = container.find_elements(By.CSS_SELECTOR, 'span.amount')

                    for name in names:
                        name_list.append(name.text)
                    for price in prices:
                        price_list.append(price.text.strip("TL"))
                    
                    self.products = zip(name_list,price_list)

                except Exception as e:
                    print(e)

                page += 1
                
                
                if self.browser.find_element(By.XPATH, '//*[@id="pagination-button-next"]/span[5]') == None:
                    page = 1
                    there_is_next_page = False

        self.browser.quit() 
                 
        
    
if __name__ == '__main__':
    carrefour = CarrefourScraper("Carrefour")
    carrefour.get_links()
    carrefour.get_names_and_prices()
    carrefour.save_data()
    '''
    migros = MigrosScraper("Migros")
    migros.get_links()
    migros.get_names_and_prices()
    '''

    
 