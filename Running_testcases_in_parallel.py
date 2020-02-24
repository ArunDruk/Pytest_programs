import pytest
from selenium import webdriver
import time

class Test_Method1:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        yield
        self.driver.quit()

    # def test_login(self,setup):
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/")
    #     time.sleep(5)
    #     self.driver.find_element_by_id("txtUsername").send_keys("Admin")
    #     self.driver.find_element_by_id("txtPassword").send_keys("admin123")
    #     self.driver.find_element_by_id("btnLogin").click()
    #     time.sleep(5)


    def test_getTitle(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        self.driver.get_screenshot_as_png()
        print(self.driver.title)

    def test_verifyingTitle(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        assert self.driver.title == "orangeHRM" #OrangeHRM
        

#Use the command "pytest -v -s Running_testcases_in_parallel.py -n 2", to run three test cases in parallel,
# by opening multiple (2) browsers above
#Command to execute the file and generate a
# html report : pytest -v -s --html=Running_testcases_parallel_report.html Running_testcases_in_parallel.py -n 3