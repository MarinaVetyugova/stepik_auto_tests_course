from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
 
link = "http://suninjuly.github.io/explicit_wait2.html"

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get(link)
    
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )        
    button = browser.find_element_by_id("book")
    button.click()

    #browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    print(browser.switch_to.alert.text)
    time.sleep(5)
