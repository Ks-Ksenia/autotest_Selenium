import os

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input = browser.find_element_by_css_selector("[name = firstname]")
    input.send_keys("a")
    input2 = browser.find_element_by_css_selector("[name = lastname]")
    input2.send_keys("a")
    input3 = browser.find_element_by_css_selector("[name = email]")
    input3.send_keys("a")
    file = browser.find_element_by_id("file")
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_dir, "file.txt")

    file.send_keys(file_path)
    print(os.path.abspath(os.path.dirname(__file__)))

    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()

finally:
    time.sleep(10)

    browser.quit()