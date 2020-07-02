import math

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value")
    x = x.text
    print(x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    print(y)

    input = browser.find_element_by_id("answer")
    input.send_keys(str(y))

    btn2 = browser.find_element_by_css_selector("button.btn")
    btn2.click()


finally:
    time.sleep(5)
    browser.quit()