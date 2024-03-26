from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://salonboard.com/login")

search_box = driver.find_element(By.XPATH, '//*[@id="idPasswordInputForm"]/div/div[1]/dl[1]/dd/input')
search_box.send_keys('aaa')

time.sleep(5)
