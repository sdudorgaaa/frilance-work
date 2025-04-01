from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

delay = 10
option = webdriver.ChromeOptions()
option.add_argument("--disable-infobars") 
browser = webdriver.Chrome('chromedriver.exe',chrome_options=option)
browser.get('https://tyumen.cian.ru/sale/flat/285322036/')
sleep(delay)
elem  =  browser.find_element(By.CLASS_NAME,  'a10a3f92e9--fullscreen--s_6ZN.a10a3f92e9--fullscreen--ZZKyb' )
print(elem)