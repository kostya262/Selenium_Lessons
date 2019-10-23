import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")
Select(browser.find_element_by_id("dropdown")).select_by_visible_text(str(int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)))
browser.find_element_by_css_selector("button").click()
time.sleep(10)
browser.quit()