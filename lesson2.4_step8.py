import math

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser,13).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"$100")
    )
    btn = browser.find_element_by_id("book")
    btn.click()

    x = browser.find_element_by_id("input_value")
    x = x.text
    print(x)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    print(y)

    input = browser.find_element_by_id("answer")
    input.send_keys(str(y))

    btn2 = browser.find_element_by_id("solve")
    btn2.click()

finally:
    time.sleep(5)
    browser.quit()