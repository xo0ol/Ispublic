import pyautogui as pag
import openpyxl
import math

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time # time.sleep() 을 위한 패키지
import timeit # 시간을 숫자단위로 측정. 시작시간-종료시간으로 작업시간을 계산
from datetime import datetime # datetime.now() 을 위한 패키지
from datetime import timedelta # 시간끼리의 연산을 위한 패키지





# running time check
start_time = timeit.default_timer()


# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])







## 이곳에서 ref file과 new file의 경로와 이름을 설정하시오. ##

# 1.새로 만들 파일을 저장할 주소와 이름을 설정하시오.
new_file_name = '\lotte_infomation'
new_file_adress = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling\lotte'


# 2.url정보를 가져올 엑셀파일의 주소와 이름을 설정하시오.
ref_file = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling\lotte.txt'

############################################################





# 바코드 파일에서 바코드 데이터 리스트로 가져오기
file = open(ref_file, 'r')
read = file.readlines()
lotte_url = [x.strip('\n') for x in read]



# 공란인 데이터는 "https://emart.ssg.com/" 으로 변경하기
lotte_url_clean = []
idx = 0
for x in lotte_url:
    if x == '':
        lotte_url_clean.append("https://www.lotteon.com/")
    else:
        lotte_url_clean.append(x)

print(lotte_url_clean)
count_bar = len(lotte_url_clean)



# 새로 만들 파일을 오픈하기.
open_file = openpyxl.Workbook()
open_file_ws = open_file.active
open_file_ws['a1'] = 'title'
open_file_ws['b1'] = 'new_price'
open_file_ws['c1'] = 'price'
open_file_ws['d1'] = 'delivery'
open_file_ws['e1'] = 'out_of_stock'
open_file_ws['f1'] = 'promotion'



# 데이터 크롤링 시작
rows = 2
idx = 1
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

browser = webdriver.Chrome(options=chrome_options)
browser.minimize_window()

for i in lotte_url_clean:

    browser.get(i)
    time.sleep(2)
    
    try:
        title = browser.find_element(By.CLASS_NAME,"pd-widget1__product-name").text
        
    except:
        open_file_ws[f'a{rows}'] = ""
        open_file_ws[f'b{rows}'] = ""
        open_file_ws[f'c{rows}'] = ""
        open_file_ws[f'd{rows}'] = ""
        open_file_ws[f'e{rows}'] = ""
        open_file_ws[f'f{rows}'] = ""
        next
        
        
    else:     
        try:
            new_price = browser.find_element(By.CLASS_NAME,"won").text
        except:
            new_price = "new price error"
        
        try:
            price = browser.find_element(By.CLASS_NAME,"price").text
        except:
            price = "price error"

        try:
            if browser.find_element(By.CLASS_NAME, "inner").text is not None:
                out_of_stock = 0
        except:
            out_of_stock = 1


        # 택배배송 확인
        try:
            if browser.find_element(By.CLASS_NAME, "purchaseInfoBox").text is not None:
                delv = browser.find_element(By.CLASS_NAME, "purchaseInfoBox").text
        except:
            delv = 'delivery error'




        promotion = ""
        
        
        open_file_ws[f'a{rows}'] = title
        open_file_ws[f'b{rows}'] = new_price
        open_file_ws[f'c{rows}'] = price
        open_file_ws[f'd{rows}'] = delv
        open_file_ws[f'e{rows}'] = out_of_stock
        open_file_ws[f'f{rows}'] = promotion

    print(f'『 ({str(count_bar)}/{str(idx)}) 완료. 』')
    rows += 1
    idx += 1

    time.sleep(2)

browser.quit()

# new file 저장하기.
today = datetime.now().strftime('%Y-%m-%d %H-%M')
new_file = new_file_adress  + new_file_name + '({}).xlsx'.format(today)

open_file.save(new_file)
print('『 new file saved. 』')




# 작업 종료 알림
end_now_str = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
finished_time = timeit.default_timer()
running_time = math.trunc(finished_time - start_time)


if running_time % 60 == running_time:
    x_time = f'00:{str(running_time).rjust(2,"0")}'
else:
    x1 = math.trunc(running_time / 60)
    x2 = running_time & 60
    x_time = f'{str(x1).rjust(2,"0")}:{str(x2).rjust(2,"0")}'


print(f'『 {(x_time)} 소요되었습니다. 』')
print(f"『 {end_now_str} 작업을 종료합니다. 』")
