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



# 교재 설정
last_pages = 3 # ebook의 마지막 페이지 +1(홀수로)
folder_name = "엑셀데이터분석교재" # 캡쳐본을 저장할 폴더의 이름
url = "https://ebook.claverse.com/knou/viewer_knou.jsp?qry=Cz1uyuB93RbLDpteCe9yBoIl3Vb5mFocFnYzx8WmWpooXd4eXlACvlMIcPXvhepgf2FHFKJQ8xLN54oioHnU-li8YuzERA59D76J2QH8IWHd9YcUryi8f2ifSdcOfGgrslYhQdjGMr4yBd9KGUrkX1B8CMYB4BJvQ4Pti2_9dAY9vcijIzOCe7ly_BXPRF9ucxGSSFnNrdyL4-HH5IuptRoS5CFNceGJ-p_2fwkTVEPh3N4UF2VeSmu4VsWoGUAfPyRScBFEmsTn0892Hn_nv2yt5bwYZZPBEEc-a724UbWTninu81b_8VBX7NvVYoFt#"
################



# 브라우저 킴
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
browser.maximize_window() # 화면 제일 크게
time.sleep(5)
# 저장할 폴더, 파일명 정의



x = 0
y = 1

while y <= last_pages:
    # path = r"C:\세계의역사_교재\capture({}~{}).png".format(y-1,y)
    # pag.screenshot(path, region=(290, 160, 1400, 800))
    browser.save_screenshot(r"C:\Users\xo0ol\OneDrive\바탕 화면\{}\{}-{}.png".format(folder_name,y-1,y))
    print(f'『{y-1}-{y} pages Saved』')
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