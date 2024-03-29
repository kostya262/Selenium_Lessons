import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
browser.find_element_by_css_selector("button").click()
browser.find_element_by_id("answer").send_keys(str(calc(int(browser.find_element_by_id("input_value").text))))
button = browser.find_element_by_css_selector("button")
browser.execute_script("return arguments[0].scrollIntoView(true)",button)
button.click()
time.sleep(10)
browser.quit()