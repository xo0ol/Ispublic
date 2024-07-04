import pyautogui as pag
import openpyxl
import os
import math

import requests
from bs4 import BeautifulSoup
# import urllib3


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# pip install ChromeDriverManager


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
new_file_name = '\koreanet_crawling'


new_file_adress = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling\koreanet'
# new_file_adress = r'C:\Users\user\Desktop\소영파일\koreanet' # 궁동집
# new_file_adress = r'C:\Users\PC\OneDrive\바탕 화면\xoyoung\crawling\koreanet' # 궁동집안방


# 2. 바코드 정보를 가져올 파일의 주소와 시트명을 설정하시오.
ref_file = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling\koreanet.txt'
# ref_file = r'C:\Users\user\Desktop\소영파일\koreanet.txt' # 궁동집
# ref_file = r'C:\Users\PC\OneDrive\바탕 화면\xoyoung\crawling\koreanet.txt' # 궁동집안방

############################################################






# txt 바코드 파일에서 바코드 데이터 리스트로 가져오기
file = open(ref_file, 'r')
read = file.readlines()

barcode = [x.strip('\n') for x in read]
count_bar = len(barcode)
count_bar_len = len(str(count_bar))
print(f"[ 작업 수량 : {count_bar} ]")




# 워크시트 생성
wb_2 = openpyxl.Workbook()
ws_2 = wb_2.active
idx = 1



# 크롬 브라우저 설정
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.minimize_window()
url = "https://www.koreannet.or.kr/front/koreannet/gtinSrch.do"



# 브라우저 열기
browser.get(url)
time.sleep(1.5)



# 웹 크롤링 시작
for x in barcode:

    if x == '':
        print(f"[{str(idx).rjust(count_bar_len,'0')}/{count_bar}] - ")
        today = (datetime.now()).strftime('%y.%m.%d %H:%M:%S')
        ws_2[f'a{idx}'] = ""
        time.sleep(0.5)
    
    else:
        time.sleep(0.5)
        # 코리아넷 브라우저 열고 기존 바코드 삭제하기
        search_bar = browser.find_element(By.ID, "gtin")
        search_bar.clear()
        time.sleep(0.3)

        search_bar.send_keys(x)
        time.sleep(0.3)

        search_bar.send_keys("\n")
        time.sleep(0.3)

        
        # 바코드가 검색이 되면 try
        # 검색 안될 시 except
        try:
            title = browser.find_element(By.CLASS_NAME, "nm").text

            # 판매자 정보 없으면 No information 입력
            try:
                seller = browser.find_element(By.XPATH, "/html/body/div[2]/form/div/div/div[4]/div[2]/div[4]/div[1]/div[2]").text
            except:
                seller = "no information"

            today = (datetime.now()).strftime('%y.%m.%d %H:%M:%S')
            ws_2[f'a{idx}'] = f"{x}_{str(title)} | {seller} | {today}"
            print(f"[{str(idx).rjust(count_bar_len,'0')}/{count_bar}] {x}_{str(title)} | {seller} | {today}")
            # print(f"[{str(idx).rjust(count_bar_len,'0')}/{count_bar}] {str(x)} {title} | {seller}")

        except:
            today = (datetime.now()).strftime('%y.%m.%d %H:%M:%S')
            ws_2[f'a{idx}'] = f"no product({str(x)}) | {today}"
            print(f"[{str(idx).rjust(count_bar_len,'0')}/{count_bar}] no product({str(x)}) | {today}")
            # print(f"[{str(idx).rjust(count_bar_len,'0')}/{count_bar}] {str(x)} no product")

            
    idx += 1
    time.sleep(0.5)

browser.quit()

# new file 저장하기.
now = datetime.now()
today = now.strftime('%Y-%m-%d')
new_file = new_file_adress  + new_file_name + '({}).xlsx'.format(today)


uniq = 1
while os.path.exists(new_file):
    new_file = new_file_adress  + new_file_name + '({})({}).xlsx'.format(today, uniq)
    uniq += 1

wb_2.save(new_file)



# 작업 종료 알림
end_now_str = (datetime.now()).strftime('%m.%d %H:%M:%S')
finished_time = timeit.default_timer()
running_time = math.trunc(finished_time - start_time)


if running_time % 60 == running_time:
    # print(running_time)
    x_time = f'00:{str(running_time).rjust(2,"0")}'
else:
    x1 = math.trunc(running_time / 60)
    x2 = running_time & 60
    x_time = f'{str(x1).rjust(2,"0")}:{str(x2).rjust(2,"0")}'

print(f'『 {(x_time)} 소요되었습니다. 』')
print(f"『 {end_now_str} 작업을 종료합니다. 』")