from selenium import webdriver
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
 
link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
#element.send_keys(file_path)


with webdriver.Chrome() as browser:
    browser.get(link)

    firstname = browser.find_element_by_xpath("//input[@name='firstname']")
    firstname.send_keys("Ivan")

    lastname = browser.find_element_by_xpath("//input[@name='lastname']")
    lastname.send_keys("Ivanov")

    email = browser.find_element_by_xpath("//input[@name='email']")
    email.send_keys("IvanIvanov@gmail.com")

    upload = browser.find_element_by_id("file")
    upload.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(10)
