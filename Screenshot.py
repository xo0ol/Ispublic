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
# chrome_options.add_argument('--headless')


# 브라우저 킴
url = "https://ebook.claverse.com/knou/viewer_knou.jsp?qry=hFs3eImt5zDXDSjy9tLmsvsGS0dg9q9bHj9SD2W70_0pDkxeGUTs8c7rM5bp2mA8XCEx_i3L67pWMRBEdd7pf6RUgajg3RJseKSIYlnPcZpEJYB84zKlGnhEUB5Ax8Uasrm414WYrI4UZZYWNhNn84D7BEC298zpHAsa0JuDJ9I14VlvEl3rF1f3agSU-uk3SbENbdVSHM5x8Fg72X6qoRIv50FGGBRRfwpOGkNmGk9JHmtN8nqkIdOa0YvPvGy2NFVO8k3u5DR1hH7PJFq3asajIsiczblizDNN5pHn1BBqIzYAoZoezENXG6aD7Jgv#"
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
browser.maximize_window() # 화면 제일 크게
time.sleep(5)
# 저장할 폴더, 파일명 정의

pages = 10
x = 0
y = 1

while x < pages:
    # path = r"C:\세계의역사_교재\capture({}~{}).png".format(y-1,y)
    # pag.screenshot(path, region=(290, 160, 1400, 800))
    browser.save_screenshot(r"C:\세계의역사_교재\{}-{}.png".format(y-1,y))
    time.sleep(1)
    try:
        next_button  = browser.find_element(By.ID, 'btnPageNext')
        next_button.click()
    except:
        break
        print("element error : 종료")
    time.sleep(2)
    x += 1
    y += 2
    
browser.quit()
# 좌표 구하기
# time.sleep(2)
# print(pag.position())


# path = r"C:\Capture\Capture.png"

# time.sleep(2)
# pag.screenshot(path, region=(290, 160, 1400, 800))