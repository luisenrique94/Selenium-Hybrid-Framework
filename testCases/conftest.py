from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
       driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Selenium-Hybrid-Framework\\Drivers\\chromedriver.exe")
       print("Launching Chrome browser........")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path="C:\\Users\\Luis\\Desktop\\Selenium-Hybrid-Framework\\Drivers\\geckodriver.exe")
        print("Launching Firefox browser........")
    else:
        driver = webdriver.Ie(executable_path="C:\\Users\\Luis\\Desktop\\Selenium-Hybrid-Framework\\Drivers\\IEDriverServer.exe")
    return driver


def pytest_addoption(parser): #this will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #this will return the browser value to setup method
    return request.config.getoption("--browser")

############## pytest HTML REPORT #####################
#IT IS HOOK OR ADDING ENVIROMENT INFO TO HTML REPORT
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'
# IT IS HOOK FOR DELETE/MODIFY ENVIRONMENT INFO TO HTML REPORT
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

