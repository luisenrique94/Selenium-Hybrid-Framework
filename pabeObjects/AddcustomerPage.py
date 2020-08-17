import time
from selenium.webdriver.support.ui import Select
class AddCustomer:
    #menu
    lnkCustomers_menu_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/a"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span"
    #btn nuevo customer
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    #datos de registro
    txtEmail_xpath =  "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdGenderMA_id = "Gender_Male"
    rdGenderFe_id = "Gender_Female"
    txtDateOB_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_id = "Company"
    checkIsTaxExemp_xpath = "//input[@id='IsTaxExempt']"
    txtNewsletter_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div/div[1]/div"
    #lista de roles
    txtCustomerRoles_xpath = "//div[10]//div[2]//div[1]//div[1]//div[1]"
       # "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-border-down']"
    lstietemAdministrators_xpath = "//li[contains(text(),'Administradors')]"
    lstietemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstietemGuest_xpath = "//li[contains(text(),'Guests')]"
    lstietemForum_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstietemVendors_xpath = "//li[contains(text(),'Vendors')]"
    # lista de vendedor
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    #active
    inputActive_xpath = "//input[@id='Active']"
    #comment
    txtComment_xpath = "//textarea[@id='AdminComment']"
    #btn save
    btnSave_xpath = "//button[@name='save']"
    btnSaveEdict_xpath = "//button[@name='save-continue']"
    #link back
    link_BackToCustomer_xpath = "//a[contains(text(),'back to customer list')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstietemRegistered_xpath)
        elif role ==  'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstietemAdministrators_xpath)
        elif role == 'Guests':
            #here user can be registered (or) guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstietemGuest_xpath)
        elif role =='Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstietemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstietemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstietemGuest_xpath)
        time.sleep(3)
        #self.listitem.click();
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender =='Male':
            self.driver.find_element_by_id(self.rdGenderMA_id).click()
        elif gender == 'Femalel':
            self.driver.find_element_by_id(self.rdGenderFe_id).click()
        else:
            self.driver.find_element_by_id(self.rdGenderMA_id).click()



    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDateOB_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_id(self.txtCompanyName_id).send_keys(comname)

    def setAdminConten(self, content):
        self.driver.find_element_by_id(self.txtCompanyName_id).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()



