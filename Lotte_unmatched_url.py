import requests
from bs4 import BeautifulSoup
# python.exe -m pip install --upgrade pip
import openpyxl
import webbrowser
import time





# 엑셀 파일 열기
ref_file = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\Crawling\lotte_unmatched_url.xlsx'
wb = openpyxl.load_workbook(ref_file)
ws = wb.active



# 엑셀 파일 데이터 추출하기
j = 1
sample_list = []
for i in ws.rows:
    sample_list.append(ws[f'a{j}'].value)
    j = j + 1

lotte_url = list(filter(None, sample_list))



# 상품 정보가 남아있는 url 오픈하기
j = 1
for i in lotte_url:

    try:
        respon = requests.get(i)
    except:
        next
    html = respon.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        result = soup.find('input',{'id':'metaData'}).get('value')
    except:
        result = None
    if result != None:
        title = soup.select_one('title').text
        print(title)
        print(f"\n{i}\n")

        # 웹브라우저 바로 열기
        # webbrowser.open(i)
        # time.sleep(2)


    

