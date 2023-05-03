import pyautogui as pag
import time
import openpyxl
import time
import datetime
import timeit
import math


import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# running time check
start_time = timeit.default_timer()


# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])


# new file명에 입력되는 시간 정의하기
now = datetime.datetime.now()




## 이곳에서 ref file과 new file의 경로와 이름을 설정하시오. ##

# 1.새로 만들 파일을 저장할 주소와 이름을 설정하시오.
new_file_name = '\Lotte_unmatched_url'
new_file_adress = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling\Lotte_unmatched_url'


# 2.url정보를 가져올 엑셀파일의 주소와 이름을 설정하시오.
ref_file = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling\lotte_barcode_url.txt'

############################################################





# 새로 만들 파일을 오픈하기.
open_file = openpyxl.Workbook()
open_file_ws = open_file.active



# 바코드 파일에서 바코드 데이터 리스트로 가져오기
file = open(ref_file, 'r')
read = file.readlines()

sample_list = [x.strip('\n') for x in read]



lotte_url = list(filter(None, sample_list))
count_bar = len(lotte_url)

# 상품 정보가 남아있는 url 출력 및 수집
browser = webdriver.Chrome(options=chrome_options)
browser.minimize_window()
matched = []
idx = 1
working_num = 1
for i in lotte_url:

    try:
        browser.get(i)
        time.sleep(2)
        title_error = browser.find_element(By.CLASS_NAME, 'titleError').text

    except:
        respon = requests.get(i)
        html = respon.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('title').text
        print(f"『 {working_num}/{len(lotte_url)} 완료. 』 {idx}) {title}")
        # print(f"{i}\n") 
        matched.append(i)
        open_file_ws[f'a{idx}'] = str(i)
        idx += 1
        next
    print(f'『 {working_num}/{len(lotte_url)} 완료. 』 ')
    working_num += 1
    


browser.quit()
print('『 browser exited. 』')


# # 수집된 URL이 {minimum}개 이하면 바로 오픈하기
# minimum = 5
# if len(matched) <= minimum:
#     print(f"『추적 가능 lotte URL이 {len(matched)}개 발견되었습니다.』\nWebbrowser open")
#     time.sleep(2)
#     for x in matched:
#         webbrowser.open(x)
#         time.sleep(2)
# else:
#     print(f"『추적 가능한 lotte URL이 {len(matched)}개 발견되었습니다.』\nQuit\n")



# new file 저장하기.
today = now.strftime('%Y-%m-%d-%H-%M')
new_file = new_file_adress  + new_file_name + '({}).xlsx'.format(today)

open_file.save(new_file)
print('『 new file saved. 』')




# 작업 종료 알림
end_now_str = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
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