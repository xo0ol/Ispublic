import pyautogui as pag
import time
from PIL import ImageGrab

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])



url1 = 'https://www.lotteon.com/p/product/LM8801104301091' # 
url2 = 'https://www.lotteon.com/p/product/LM8801111186247' # 판매중단


browser = webdriver.Chrome(options=chrome_options)
browser.get(url2)

time.sleep(2)


s = browser.find_element(By.CLASS_NAME, "titleError").text
print(s)

browser.quit()