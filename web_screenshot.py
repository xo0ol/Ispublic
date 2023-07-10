import pyautogui as py
import openpyxl
import math


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

# 화면 최대화
# chrome_options.add_argument('--start-maximized')





## 이곳에서 ref file과 new file의 경로와 이름을 설정하시오. ##

# 1.새로 만들 파일을 저장할 주소와 이름을 설정하시오.
web_name = "homeplus"
adress = r"C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling"


# 2.url정보를 가져올 파일의 주소와 이름을 설정하시오.
ref_file = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling\screenshot.txt'
############################################################







# 바코드 파일에서 바코드 데이터 리스트로 가져오기
file = open(ref_file, 'r')
read = file.readlines()

sample_list = [x.strip('\n') for x in read]



lotte_url = list(filter(None, sample_list))
count_bar = len(lotte_url)

# print(lotte_url)



# 작업 시작시간 알림 / 작업 시간 체크
start_time_now = datetime.now()
print(f"『 {start_time_now.strftime('%H:%M:%S')} {web_name} 이미지 저장 시작. 』")
start_time = timeit.default_timer()




# 상품 정보가 남아있는 url 출력 및 수집
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
matched = []
idx = 1
working_num = 1

for i in lotte_url:
        
    try:
        browser.get(i)
        time.sleep(2)
        path = "{}\{}_{}.png".format(adress, web_name, idx)
        print(path)
        py.screenshot(path, region=(365, 155, 1190, 845))
        idx += 1
        time.sleep(1)
    except:
        print(f"{idx} error")
        browser.get(i)
        time.sleep(2)
        path = "{}\{}_{}.png".format(adress, web_name, idx)
        print(path)
        py.screenshot(path, region=(365, 155, 1190, 845))
        idx += 1
        time.sleep(1)
        continue
    
    


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



# # new file 저장하기.
# today = datetime.now().strftime('%Y-%m-%d %H-%M')
# new_file = new_file_adress  + new_file_name + '({}).xlsx'.format(today)

# open_file.save(new_file)
# print('『 new file saved. 』')




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