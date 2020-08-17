import unittest
from  selenium import webdriver
import  time
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Selenium-Hybrid-Framework\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.implicitly_wait(5)
    def test_something(self):

        # self.driver.find_element_by_xpath("//div[@class='subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3']").click()
         time.sleep(2)
         self.driver.find_element_by_xpath("//input[@id='subjectsInput']").send_keys("hindi", Keys.ENTER)
         time.sleep(5)
         self.driver.find_element_by_id("react-select-3-input").send_keys("NCR", Keys.ENTER)
         time.sleep(5)



if __name__ == '__main__':
    unittest.main()
