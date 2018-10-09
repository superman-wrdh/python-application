from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()
# http://chromedriver.storage.googleapis.com/index.html
try:
    browser.get("https://www.baidu.com")
    input = browser.find_element_by_id("kw")
    input.send_keys("12306")
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "content_left")))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
    browser.find_element_by_name('a')
    links = browser.find_elements_by_tag_name("a")
    a = True
    for link in links:
        if a:
            if not "_blank" in link.get_attribute("target") and (
                    "12306" in link.et_attribute("href") or not "http" in link.get_attribute("href")):
                link.click()
            a = False

    time.sleep(10)
finally:
    pass
    # browser.close()
