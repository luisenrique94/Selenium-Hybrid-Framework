from pabeObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time
import unittest
import pytest



class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path="C:\\Users\\Luis\\Desktop\\Selenium-Hybrid-Framework\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("********Test_002_DDT_Login***************")
        self.logger.info("********Home Verifying Login Test *******")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Hoja1')
        print("Number of Rows i a Excel:", self.rows)

        lst_status=[] #empaty list varaible

        for r in range(2, self.rows+1):
            self.user=XLUtils.readData(self.path, 'Hoja1',r,1)
            self.password=XLUtils.readData(self.path, 'Hoja1',r,2)
            self.exp=XLUtils.readData(self.path,'Hoja1',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

        #self.lp.clickLogout()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***Passed***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Failed***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***failed***")
                    lst_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info("***passed***")
                    lst_status.append("Fail")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test passed...")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT  test failed...")
            self.driver.close()
            assert False
        self.logger.info("************* End of Login DDT Test *****")
        self.logger.info("************Completed TC_LoginDDT_002****")












#if __name__ == '__main__':
 #   unittest.main()
