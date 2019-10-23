import os
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
browser.find_element_by_css_selector("input:nth-child(2)").send_keys(".")
browser.find_element_by_css_selector("input:nth-child(4)").send_keys(".")
browser.find_element_by_css_selector("input:nth-child(6)").send_keys(".")
browser.find_element_by_css_selector("input:nth-child(5)").send_keys(os.path.join(os.path.abspath(os.path.dirname('Test3.txt')), 'Test3.txt'))
browser.find_element_by_css_selector("button").click()
time.sleep(10)
browser.quit()