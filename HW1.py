from bs4 import BeautifulSoup as bs
import requests
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime

from openpyxl import Workbook

import time

url='https://www.genie.co.kr/chart/top200'

try:
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code ==200:
        html_text =response.text
        
        soup = bs(response.text, 'html.parser')
        
        titles=soup.find_all(class_='title ellipsis')
        titles = list(map(lambda x :x.text.strip(), titles))
        print(titles)
        
        artists = soup.find_all(class_='artist ellipsis')
        artists=list(map(lambda x: x.text, artists))
        print(artists)
        
        wb = Workbook()
        ws = wb.active
        
        ws.append(["순위", "제목", "아티스트"])
        
        # for a in enumerate(zip(titles,artists)):
        #     print(a)
        
        for i, (title, artist) in enumerate(zip(titles, artists)):
            print(i, title, artist)
            ws.append([i, title, artist])
                
                        
        today = datetime.now().strftime('%Y%m%d')
        
        filename = f'genie_chart_{today}.xlsx'
        wb.save(filename)
        print(f"엑셀 파일 저장 완료: {filename}")
        
    else:
        print(f"Error: HTTP 요청 실패, 상태코드: {response.status_code}")
        
except requests.exceptions.RequestException as e:
     print(f"Error: 요청 중 오류 발생. 오류 메세지: {e}")