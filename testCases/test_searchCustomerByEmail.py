import time

from  pabeObjects.AddcustomerPage import AddCustomer
from pabeObjects.LoginPage import LoginPage
from pabeObjects.SearchCustomer import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import  random
import pytest

class Test_004_searchCustomerByEmail:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********* SearchCustomerByEmail_004*****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************** Login succesful**************")

        self.logger.info("********************  Starting Search Customer By Email *************+")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("********************** searching customer by emailID****************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail(("victoria_victoria@nopCommerce.com"))
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("************************** TC_SearchCustomerByEmail_004 Finished ************")
        self.driver.close();

