import pyautogui as pag
import openpyxl
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
new_file_name = '\lotte_barcode_url'
new_file_adress = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling\lotte_barcode_url'


# 2.url정보를 가져올 파일의 주소와 이름을 설정하시오.
ref_file = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling\lotte_barcode_url.txt'
############################################################





# 새로 만들 파일을 오픈하기.
open_file = openpyxl.Workbook()
open_file_ws = open_file.active



# 바코드 파일에서 바코드 데이터 리스트로 가져오기
file = open(ref_file, 'r')
read = file.readlines()

# sample_list = [x.strip('\n') for x in read]
lotte_url = [x.strip('\n') for x in read]


# lotte_url = list(filter(None, sample_list))
# idx = 0
# for x in lotte_url:
#     if x == '':
#         lotte_url[idx] = ""
#     idx += 1



# Total url 출력
count_bar = len(lotte_url)
print(f"[ Total URL : {count_bar} ]")
count_bar_len = len(str(count_bar))


# 상품 정보가 남아있는 url 출력 및 수집
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.minimize_window()
delivery_type = "내일 발송"
idx = 1
find_count= 0

for i in lotte_url:

    if i == '': # url이 존재하지 않으면(공백이면) "-" 입력 후 넘어가기.
        open_file_ws[f'a{idx}'] = ""
        open_file_ws[f'b{idx}'] = ""
        print(f"[{str(idx).rjust(count_bar_len,'0')}/{len(lotte_url)}] - ")
        
    else: # url이 존재하면서,
        try: # 상품 페이지가 존재하지 않으면 else문 실행.
            browser.get(i)
            time.sleep(3)
            title_error = browser.find_element(By.CLASS_NAME, 'titleError').text

        except: # 상품 페이지가 존재하면 except문 실행.
            title = browser.find_element(By.CLASS_NAME, "pd-widget1__product-name").text
            delv = browser.find_element(By.CLASS_NAME, "pd-DeliveryInfo__inner").text

            if delivery_type in delv:
                open_file_ws[f'a{idx}'] = ""
                open_file_ws[f'b{idx}'] = ""
                print(f"[{str(idx).rjust(count_bar_len,'0')}/{len(lotte_url)}] case deleted by delivery")
                next

            else:
                open_file_ws[f'a{idx}'] = str(i)
                open_file_ws[f'b{idx}'] = i[str(i).find('LM')+2:]

                print(f"[{str(idx).rjust(count_bar_len,'0')}/{len(lotte_url)}] {title}")
                find_count += 1
                next
        
        else:
            open_file_ws[f'a{idx}'] = ""
            open_file_ws[f'b{idx}'] = ""
            print(f"[{str(idx).rjust(count_bar_len,'0')}/{len(lotte_url)}] no search url")

    idx += 1
    time.sleep(1)


browser.quit()
print(f"『 browser exited. [{find_count}] Target url match. 』")




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


# print(f'『 {(x_time)} 소요되었습니다. 』')
print(f"『 {end_now_str} 작업을 종료합니다. [소요시간 : {x_time}] 』")