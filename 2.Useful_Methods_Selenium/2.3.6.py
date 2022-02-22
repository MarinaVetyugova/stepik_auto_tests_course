from selenium import webdriver
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
 
link = "http://suninjuly.github.io/redirect_accept.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    print(browser.switch_to.alert.text)
    time.sleep(5)
