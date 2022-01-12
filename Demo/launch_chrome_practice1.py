from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
driver.set_page_load_timeout(10)
driver.maximize_window()
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click
time.sleep(2)
driver.close()
driver.quit()
print("Test completed")
