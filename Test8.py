import time
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")
browser.find_element_by_css_selector("button").click()
browser.switch_to.alert.accept()
time.sleep(1)
browser.find_element_by_id("answer").send_keys(str(calc(int(browser.find_element_by_id("input_value").text))))
browser.find_element_by_css_selector("button").click()
time.sleep(10)
browser.quit()