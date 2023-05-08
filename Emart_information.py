import openpyxl
import pyautogui
import requests
from bs4 import BeautifulSoup
import os
import math

import time # time.sleep() 을 위한 패키지
import timeit # 시간을 숫자단위로 측정. 시작시간-종료시간으로 작업시간을 계산
from datetime import datetime # datetime.now() 을 위한 패키지
from datetime import timedelta # 시간끼리의 연산을 위한 패키지



# running time check
start_time = timeit.default_timer()




## 이곳에서 ref file과 new file의 경로와 이름을 설정하시오. ##

# 1.새로 만들 파일을 저장할 주소와 이름을 설정하시오.
new_file_name = '\emart_infomation'
new_file_adress = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling\emart'


# 2.url정보를 가져올 엑셀파일의 주소와 이름을 설정하시오.
ref_file = r'C:\Users\xo0ol\OneDrive\바탕 화면\xoyoung\crawling\emart.txt'

############################################################





# ref 파일에서 데이터 리스트로 가져오기
file = open(ref_file, 'r')
read = file.readlines()
emart_url = [x.strip('\n') for x in read]



# 공란인 데이터는 "https://emart.ssg.com/" 으로 변경하기
emart_url_clean = []
idx = 0
for x in emart_url:
    if x == '':
        emart_url_clean.append("https://emart.ssg.com/")
    else:
        emart_url_clean.append(x)

count_bar = len(emart_url_clean)




# 새로 만들 파일을 오픈하기.
open_file = openpyxl.Workbook()
open_file_ws = open_file.active
open_file_ws['a1'] = 'title'
open_file_ws['b1'] = 'new_price'
open_file_ws['c1'] = 'price'
open_file_ws['d1'] = 'delivery'
open_file_ws['e1'] = 'out_of_stock'
open_file_ws['f1'] = 'promotion'



# 데이터 크롤링 시작
rows = 2
idx = 1
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

for i in emart_url_clean:

    requests.get(i, headers=headers)
    respon = requests.get(i, headers=headers)
    html = respon.text
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(2)

    try:
        title = soup.select_one("div.cdtl_prd_info.v2 > h2 > span > span").text.strip()
    except:
        open_file_ws[f'a{rows}'] = ""
        open_file_ws[f'b{rows}'] = ""
        open_file_ws[f'c{rows}'] = ""
        open_file_ws[f'd{rows}'] = ""
        open_file_ws[f'e{rows}'] = ""
        open_file_ws[f'f{rows}'] = ""
        next
        
    else:     
        try:
            new_price = soup.select_one(".cdtl_new_price").text.strip()
        except:
            new_price = "new price error"
        
        try:
            price = soup.select_one(".ssg_price").text
        except:
            price = "price error"


        # 품절/일시품절 확인
        s = soup.select("span > span")
        ss = []
        for i in s:
            ss.append(i.text)

        if '품절' in ss:
            out_of_stock = '품절'
        elif '일시품절' in ss:
            out_of_stock = '일시품절'
        else:
            out_of_stock = 0


        # 택배배송 확인
        try:
            if soup.select_one("div.shipping_type_head > div > span").text is not None:
                delv = '택배배송'
        except:
            try:
                if soup.select_one(".cdtl_delv_type").text is not None:
                    delv = 'ssg delivery'
            except:
                delv = ""


        # 행사 확인
        try:
            # promotion = soup.find("div",{"class":"txt"}).text.strip()
            promotion = soup.select_one(".cdtl_benefit_info").text
        except:
            promotion = ""
        
        
    open_file_ws[f'a{rows}'] = title
    open_file_ws[f'b{rows}'] = new_price
    open_file_ws[f'c{rows}'] = price
    open_file_ws[f'd{rows}'] = delv
    open_file_ws[f'e{rows}'] = out_of_stock
    open_file_ws[f'f{rows}'] = promotion

    print(f'『 ({str(count_bar)}/{str(idx)}) 완료. 』')
    rows += 1
    idx += 1

    time.sleep(2)



# new file 저장하기.
today = datetime.now().strftime('%Y-%m-%d %H-%M')
new_file = new_file_adress  + new_file_name + '({}).xlsx'.format(today)

open_file.save(new_file)
print('『 new file saved. 』')




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

