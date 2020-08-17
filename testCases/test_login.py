from pabeObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import unittest
import pytest



class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression

    def test_homePageTittle(self, setup):
        self.logger.info("********** Test_001_Login  *******")
        self.logger.info("********** Verifing Home Page Title  *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Home page title test is passed *******")
        else:
            self.driver.save_screenshot("C:\\Users\\Luis\\Desktop\\Selenium-Hybrid-Framework\\Screenshots\\"+"test_homePageTittle.png")
            self.driver.close()
            self.logger.error("********Home page title is failed *******")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("********Home Verifying Login Test *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #self.lp.clickLogout()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("******** Login test is passed *******")
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Luis\\Desktop\\Selenium-Hybrid-Framework\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.error("********Home Verifying is failed *******")
            assert False




#if __name__ == '__main__':
 #   unittest.main()
