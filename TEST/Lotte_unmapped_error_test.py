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



service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.minimize_window()
url = "https://www.koreannet.or.kr/front/koreannet/gtinSrch.do"

browser.get(url)
time.sleep(2)
search_bar = browser.find_element(By.ID, "gtin")
search_bar.clear()
time.sleep(0.5)
search_bar.send_keys("8801037041248")
time.sleep(0.5)
search_bar.send_keys("\n")
title = browser.find_element(By.CLASS_NAME, "nm").text
seller = browser.find_element(By.XPATH, "/html/body/div[2]/form/div/div/div[4]/div[2]/div[4]/div[1]/div[2]").text
print(seller)



