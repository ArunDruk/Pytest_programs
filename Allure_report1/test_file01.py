from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
import pytest
import time

@allure.severity(allure.severity_level.NORMAL)
@allure.feature()
class Test_Suite01:

    # @allure.severity(allure.severity_level.MINOR)
    def test_case03(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.yahoo.com")
        allure.attach(self.driver.get_screenshot_as_png(),name="yahoo_home_page",attachment_type=AttachmentType.PNG)
        time.sleep(5)
        self.driver.close()

    def test_case01(self):
        print("Hello, Welcome you ARUN")
        #pytest.skip("Am skipping this test case 01")

    def test_case02(self):
        print("Hello, Am from test case 02")
        i = 10
        assert i == 20

#  To run this program, command is :
#E:\PYTEST_test_programs\Allure_report1>pytest -v -s --alluredir=test_file01_Allure_report test_file01.py

# To generate the report, command is:
# E:\PYTEST_test_programs\Allure_report1\test_file01_Allure_report>allure serve
