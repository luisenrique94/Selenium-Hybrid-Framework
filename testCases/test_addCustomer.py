from  pabeObjects.AddcustomerPage import AddCustomer
from pabeObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import  random
import pytest

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("******* Test_003_AddCustomer*******")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***************Login succesful***********")

        self.logger.info("**************+Starting Add Customer Test**************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()
        self.logger.info("****************Providin customer infor******************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setGender("Male")
        self.addcust.setDob("7/05/1985")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")




        self.addcust.setAdminConten("This is for testong ------")
        self.addcust.clickOnSave()
        self.logger.info("**********Saving customer info **********++")
        self.logger.info("**********Add customer validation started ********")
        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("******************* Add customer Test Passed *********+")
        else:
            self.driver.save_screeshot("C:\\Users\\Luis\\Desktop\\Selenium-Hybrid-Framework\\Screenshots\\test_addCustomer_src.png") #screenshot
            self.logger.error("*********************** Add customer Test Failed ***************")
            assert True == False
        self.driver.close()
        self.logger.info("*****************Ending Home Page Title Test ***********************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars)for x in range(size))



