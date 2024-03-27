from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
# stealth
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
import os
import requests
import json

service = ChromeService(executable_path=ChromeDriverManager().install())

# create a ChromeOptions object
options = webdriver.ChromeOptions()

# disable the AutomationControlled feature of Blink rendering engine
options.add_argument('--disable-blink-features=AutomationControlled')

# disable pop-up blocking
options.add_argument('--disable-popup-blocking')

# start the browser window in maximized mode
options.add_argument('--start-maximized')

# disable extensions
options.add_argument('--disable-extensions')

# disable sandbox mode
options.add_argument('--no-sandbox')

# disable shared memory usage
options.add_argument('--disable-dev-shm-usage')

#create a new driver instance


# Change the property value of the navigator for webdriver to undefined


options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=service, options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
def login():
    #login
    driver.get('https://salonboard.com/login')
    # input_id
    id_input = driver.find_element(By.XPATH, '//*[@id="idPasswordInputForm"]/div/div[1]/dl[1]/dd/input')
    id_input_value = id_input.get_attribute("value")
    id_input.send_keys("CD66356")
    x1 = id_input.is_displayed()
    print("id input tag ok: ", x1)
    # input_pass
    pass_input = driver.find_element(By.XPATH, '//*[@id="jsiPwInput"]')
    pass_input.send_keys("bridge123!!!")
    x2 = pass_input.is_displayed()
    print("pass input tag ok: ", x2)
    #button
    button_input = driver.find_element(By.XPATH, '//*[@id="idPasswordInputForm"]/div/div[2]/a')
    x3 = button_input.is_displayed()
    print("button tag ok: ", x3)
    button_input.click()
    print("button click ok")
    time.sleep(10)

    #style add
    driver.get('https://salonboard.com/CNB/draft/styleEdit/')

def input():
    #stylist name
    driver.implicitly_wait(100)
    select_element = driver.find_element(By.XPATH, '//*[@id="styleEditForm"]/table[2]/tbody/tr[2]/td/select')
    select = Select(select_element)
    select.select_by_visible_text('COCORO 髪質改善')
    #stylist comment
    text_element = driver.find_element(By.XPATH, '//*[@id="stylistCommentTxt"]')
    text_element.send_keys("aaa")
    #stylist_poiint
    text_element1 = driver.find_element(By.XPATH, '//*[@id="pointsTxt"]')
    text_element1.send_keys("bbb")
    #stylist_name
    text_element2 = driver.find_element(By.XPATH, '//*[@id="styleNameTxt"]')
    text_element2.send_keys("ccc")
    #category
    radio_element = driver.find_element(By.XPATH, '//*[@id="styleCategoryCd02"]')
    radio_element.click()
    #length
    select1_element = driver.find_element(By.XPATH, '//*[@id="mensHairLengthCd"]')
    select1 = Select(select1_element)
    select1.select_by_visible_text('ショート')
    #hair_color
    select2_element = driver.find_element(By.XPATH, '//*[@id="styleEditForm"]/table[4]/tbody/tr[5]/td/select')
    select2 = Select(select2_element)
    select2.select_by_visible_text('イエロー・オレンジ系')
    #image
    hair_element = driver.find_element(By.XPATH, '//*[@id="mensHairImageCd01"]')
    hair_element.click()
    #menu_content
    menu_content_1 = driver.find_element(By.XPATH, '//*[@id="styleEditForm"]/table[4]/tbody/tr[7]/td/table/tbody/tr/td[1]/label/input')
    menu_content_1.click()

    menu_content_2 = driver.find_element(By.XPATH, '//*[@id="styleEditForm"]/table[4]/tbody/tr[7]/td/table/tbody/tr/td[2]/label/input')
    menu_content_2.click()

    menu_content_3 = driver.find_element(By.XPATH, '//*[@id="styleEditForm"]/table[4]/tbody/tr[7]/td/table/tbody/tr/td[3]/label/input')
    menu_content_3.click()

    #menu_content
    menu_content_content = driver.find_element(By.XPATH, '//*[@id="menuDetailTxt"]')
    menu_content_content.send_keys("aaa")

    #haircontent
    hair_content1 = driver.find_element(By.XPATH, '//*[@id="styleEditForm"]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[1]/label/input')
    hair_content1.click()

    hair_content2 = driver.find_element(By.XPATH, '//*[@id="styleEditForm"]/table[5]/tbody/tr[3]/td[1]/table/tbody/tr/td[1]/label/input')
    hair_content2.click()

    hair_content3 = driver.find_element(By.XPATH, '//*[@id="styleEditForm"]/table[5]/tbody/tr[4]/td/table/tbody/tr/td[1]/label/input')
    hair_content3.click()

    hair_content4 = driver.find_element(By.XPATH, '//*[@id="styleEditForm"]/table[5]/tbody/tr[5]/td/table/tbody/tr/td[1]/label/input')
    hair_content4.click()

    time.sleep(5)

def imageUpload():
    driver.implicitly_wait(10)
    image1 = driver.find_element(By.XPATH, '//*[@id="FRONT_IMG_ID_IMG"]')
    image1.click()
    time.sleep(10)
    print("image click")
    try:
        driver.implicitly_wait(50)
        image1_model = driver.find_element(By.XPATH, '//*[@id="imageUploaderModal"]/div')
        print("image model find")
        time.sleep(5)
        driver.implicitly_wait(50)
        input_upload = driver.find_element(By.XPATH, '//*[@id="formFile"]')
        input_upload.send_keys(os.getcwd() + "./images/1.png")
        print("input upload ok")
        time.sleep(5)
        try:
            driver.implicitly_wait(50)
            image_button = driver.find_element(By.XPATH, '//*[@id="imageUploaderModal"]/div/div[2]/div/div[3]/input')
            image_button.click()
            print("image button find")
            time.sleep(5)
        except:
            print("image button none")
    except:
        print("no")

def get_data():
    print("get start")
    response = requests.get("https://os3-318-48579.vs.sakura.ne.jp/api/style")

    if(response.status_code == 200):
        print("GET request successful")
        print("Response: ", response.text[0])
        data = json.loads(response.text)
        
        if data:
            first_array = data[0]
            print("Frist Array: ", first_array.items())
            for key, value in first_array.items():
                # print(f"{key}: {value}")
                if key == 'selectedImage1':
                    thickness_thin_value = value
                    break
            
        else:
            print("No arrays found in the response")
    else:
        print("Get request failed")

    print("value of 'thickness_thin': ", thickness_thin_value)

def main():
    # login()
    # input()
    # imageUpload()
    get_data()

main()
time.sleep(10)
driver.quit()

