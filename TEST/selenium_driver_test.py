from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver.quit()


service = Service(executable_path=ChromeDriverManager().install())
service = Service()

driver = webdriver.Chrome()
driver = webdriver.Chrome(Service=Service)
driver.get("https://www.google.com/")