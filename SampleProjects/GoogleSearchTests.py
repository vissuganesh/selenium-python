from selenium import webdriver
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_search_automation(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()




