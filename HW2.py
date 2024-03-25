import csv
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chromedriver_path = '/Users/dlalswl/Documents/2024_NEXT/chromedriver'
user_data_dir = "/Users/dlalswl/Documents/2024_NEXT/Session6/HW"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.oliveyoung.co.kr/store/main/getBestList.do?t_page=%EC%98%A4%ED%8A%B9&t_click=GNB&t_gnb_type=%EB%9E%AD%ED%82%B9&t_swiping_type=N')

infos = driver.find_elements(By.XPATH, '//*[@id="prd_info"]')
for i, info in enumerate(infos, start=1):
    name= info.find_element(By.XPATH, f"/html/body/div[3]/div[8]/div[2]/div[2]/ul[1]/li[{i}]/div/div/a/p").text
    price = info.find_element(By.XPATH,f"/html/body/div[3]/div[8]/div[2]/div[2]/ul[1]/li[{i}]/div/p[1]/span[2]").text
    
    time.sleep(5)
    print(name, price)
    
# today = datetime.now().strftime('%Y%m%d')

# file = open(f'{today}webtoon.csv', mode="w",newline='')
# writer = csv.writer(file)
# writer.writerow(["episode","title","date"])