import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = "https://www.ssg.com/item/itemView.ssg?itemId=2097000875330"
url2= "https://www.ssg.com/item/itemView.ssg?itemId=1000207635413"
respon = requests.get(url, headers=headers)
html = respon.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one("div.shipping_type_head > div > span").text
print(title)