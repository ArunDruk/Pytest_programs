import pytest
from selenium.webdriver import Chrome
import time

class Test_Method1:
    @pytest.fixture()
    def setup(self):
        self.driver = Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(5)


    def test_getTitle(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        print(self.driver.title)



# def test_logout():
#         #driver = self.driver
#         driver.find_element_by_id("welcome").click()
#         time.sleep(3)
#         driver.find_element_by_link_text("Logout").click()
#         time.sleep(3)