import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")
x_element = browser.find_element_by_id("input_value")
x = x_element.text
TF = browser.find_element_by_id("answer")
TF.send_keys(calc(x))
checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
radiobox = browser.find_element_by_id("robotsRule")
radiobox.click()
button = browser.find_element_by_css_selector("button")
button.click()
time.sleep(10)
browser.quit()
 
