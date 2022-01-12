from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(),options= chrome_options)

driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("vishulikes@gmail.com")
driver.find_element_by_id("pass").send_keys("Gane$h509")
driver.find_element_by_name("login").click()


