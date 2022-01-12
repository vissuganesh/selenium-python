import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox_path = "../drivers/geckodriver.exe"

driver = webdriver.Firefox(executable_path = firefox_path)
driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("Automate step by step")
driver.find_element_by_name("btnK").send_keys(Keys.RETURN)
time.sleep(2)
driver.close()
driver.quit()
print("Test completed")
