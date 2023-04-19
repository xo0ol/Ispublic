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
today = now.strftime('%Y-%m-%d-%H-%M')



## 이곳에서 ref file과 new file의 경로와 이름을 설정하시오. ##

# 1.새로 만들 파일의 주소와 이름을 설정하시오.
new_file_name = '\Lotte_unmatched_url'
new_file_adress = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\Crawling'
new_file = new_file_adress  + new_file_name + '({}).xlsx'.format(today)

print(new_file)