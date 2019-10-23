import math
import time
from selenium import webdriver

def calc(x):
    return str(str(math.log(abs(12*math.sin(int(x))))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")
x = calc(int(browser.find_element_by_id("input_value").text))
text_field = browser.find_element_by_id("answer")
text_field.send_keys(x)
checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
radiobox = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobox)
radiobox.click()
button = browser.find_element_by_css_selector("button")
browser.execute_script("return arguments[0].scrollIntoView(true)", button)
button.click()
time.sleep(10)
browser.quit()