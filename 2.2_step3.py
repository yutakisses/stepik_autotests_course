from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = int(browser.find_element_by_id("num1").text)
    y_element = int(browser.find_element_by_id("num2").text)
    sum_x_y = str(x_element+y_element)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_x_y)
    
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

