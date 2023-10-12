import pyautogui as py
import math
import os # 폴더 생성

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


# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])


# 교재 설정
book_url = "https://ebook.claverse.com/knou/viewer_knou.jsp?qry=iMUH2qgMtxUb7IvRcfTsEKZj8-UDS5MN4OHc6Q4JfjarLDh7z4NMtddTdcKtaTr133ifLzEwS3V8uf4PpG7Wu5d0N4PWtdBd1IjmT35rza61ZpDOWm0w5dkJOS7ryW7COapcBTN-5kWtvbV7aO8YyE3tT4ZvK7fbHYd1QoC7m_3fcuHltcphU40mcVhT5lvTrhjjZREJuX5p87kMSYBmGOfaw-3w5KXfVH-99L1HqgD75K_Vsm8RqXOWDeegEezl7xjmC0u6ApWE87ggBg-N9Mm3xJT5pz6hjJ4DF5FA59qdH99HKdqGDHG7N78q-EHq"
last_pages = 407 # ebook의 마지막 페이지 +1(홀수로)
folder_name = "데이터처리와활용" # 캡쳐본을 저장할 폴더의 이름
image_saved_adress = r"C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\통계데이터과학과\워크북캡쳐" # 캡쳐본을 저장할 폴더의 주소
################


# 작업 시작시간 알림 / 작업 시간 체크
start_time_now = datetime.now()
print(f"『 {start_time_now.strftime('%H:%M:%S')} {folder_name} 이미지 저장 시작. 』")
start_time = timeit.default_timer()


# 폴더 생성
os.mkdir(r"C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\통계데이터과학과\워크북캡쳐\{}".format(folder_name))


# 브라우저 설정
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get(book_url)
browser.maximize_window() # 화면 제일 크게
time.sleep(5)




# 캡쳐 시작
x = 0
y = 1
image_count = 0
while y <= last_pages:

    path = "{}\{}\{}-{}.png".format(image_saved_adress,folder_name,y-1,y)
    py.screenshot(path, region=(365, 155, 1190, 845))
  
    # browser.save_screenshot("{}\{}\{}-{}.png".format(image_saved_adress,folder_name,y-1,y))
    print(f'『 {y-1}-{y} 』 page saved')
    time.sleep(1)
    
    try:
        next_button  = browser.find_element(By.ID, 'btnPageNext')
        next_button.click()

    except:
        break
        print("element error : 종료")

    time.sleep(1)
    x += 1
    y += 2
    image_count += 1


# 브라우저 자동 종료
browser.quit()


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


print(f'『 [{image_count}] image capture. [{(x_time)}] 소요되었습니다. 』')
print(f"『 [{end_now_str}] {folder_name} 작업 종료. 』")