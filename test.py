import pyautogui as py
import time
import timeit
from PIL import ImageGrab
from datetime import datetime
from datetime import timedelta

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

s = datetime.now()
time.sleep(1)

d = datetime.now()
print(s-d)