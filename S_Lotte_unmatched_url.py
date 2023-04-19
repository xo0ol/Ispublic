import pyautogui as pag
import time
import openpyxl
import time
import datetime
import timeit
from PIL import ImageGrab

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


#  URL 저장할 엑셀파일 정의하기
now = datetime.datetime.now()
today = now.strftime('%Y-%m-%d-%H-%M')
new_file_adress = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\Crawling\Lotte_unmatched_url\Lotte_unmatched_url({}).xlsx'.format(today) #울집컴
new_file = openpyxl.Workbook()
new_file_ws = new_file.active



# 엑셀 파일 열기
ref_file = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\Crawling\(Ref)Lotte_unmatched_url.xlsx'
ref_wb = openpyxl.load_workbook(ref_file)
ref_ws = ref_wb.active


# 엑셀 파일 데이터 추출하기
j = 1
sample_list = []
for i in ref_ws.rows:
    sample_list.append(ref_ws[f'a{j}'].value)
    j = j + 1
lotte_url = list(filter(None, sample_list))



browser = webdriver.Chrome(options=chrome_options)

# 상품 정보가 남아있는 url 출력 및 수집
matched = []
idx = 1
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
        print(f"{idx}) {title}")
        print(f"{i}\n")
        matched.append(i)
        new_file_ws[f'a{idx}'] = str(i)
        idx += 1
        next


browser.quit()



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



# 작업 종료 알림
new_file.save(new_file_adress)
print('『new file saved.』')

end_now = datetime.datetime.now()
end_now_str = now.strftime('%Y-%m-%d %H:%M:%S')
finished_time = timeit.default_timer()
running_time = finished_time - start_time

running_time = finished_time - start_time
print(f'[{running_time/60}] 소요되었습니다.')
print(f"[{end_now_str}] 작업을 종료합니다.")


