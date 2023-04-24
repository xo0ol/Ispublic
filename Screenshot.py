import pyautogui as py
import time # time.sleep
import timeit
import math
from PIL import ImageGrab
from datetime import datetime


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])



# 교재 설정
book_url = "https://ebook.claverse.com/knou/viewer_knou.jsp?qry=Cz1uyuB93RbLDpteCe9yBoIl3Vb5mFocFnYzx8WmWpooXd4eXlACvlMIcPXvhepgf2FHFKJQ8xLN54oioHnU-li8YuzERA59D76J2QH8IWHd9YcUryi8f2ifSdcOfGgrslYhQdjGMr4yBd9KGUrkX1B8CMYB4BJvQ4Pti2_9dAY9vcijIzOCe7ly_BXPRF9ucxGSSFnNrdyL4-HH5Iuptcrou4qy9zsd-wK7Vpdh9PC_At8D1IeUfdbnBl61KQR0GujJxxhonFoqhFG87_jz9oMYuxYplknmh9aIBst5RWDs2KIHDPQrX6SmrJu9kRxJ"
last_pages = 5 # ebook의 마지막 페이지 +1(홀수로)
folder_name = "ss" # 캡쳐본을 저장할 폴더의 이름
image_saved_adress = r"C:\Users\xo0ol\OneDrive\바탕 화면" # 캡쳐본을 저장할 폴더의 주소
################



# 작업 시작시간 알림 / 작업 시간 체크
start_time_now = datetime.now()
print(f"『 {start_time_now.strftime('%H:%M:%S')} {folder_name} 이미지 저장 시작. 』")
start_time = timeit.default_timer()




# 브라우저 킴
browser = webdriver.Chrome(options=chrome_options)
browser.get(book_url)
browser.maximize_window() # 화면 제일 크게
time.sleep(5)
# 저장할 폴더, 파일명 정의




# 캡쳐 시작
x = 0
y = 1
image_count = 0
while y <= last_pages:

    path = "{}\{}\{}-{}.png".format(image_saved_adress,folder_name,y-1,y)
    py.screenshot(path, region=(365, 155, 1190, 845))
  
    # browser.save_screenshot("{}\{}\{}-{}.png".format(image_saved_adress,folder_name,y-1,y))
    print(f'『 {y-1}-{y} pages Saved. 』')
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

# 작업 시간 체크
finish_time_now = datetime.now()
finish_time = timeit.default_timer()
running_time = start_time - finish_time
print(f"『 {finish_time_now.strftime('%H:%M:%S')} {folder_name} 이미지 저장 완료. 』")
print(f'『 [{image_count}] image capture. [{math.trunc(running_time/60)}]분 소요되었습니다. 』')
# 좌표 구하기
# time.sleep(2)
# print(pag.position())


# path = r"C:\Capture\Capture.png"

# time.sleep(2)
# pag.screenshot(path, region=(290, 160, 1400, 800))