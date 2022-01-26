import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Julia")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Vagina")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Jul@yandex.ru")
    current_dir = os.path.abspath(os.path.dirname('2.2_step8.py'))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()