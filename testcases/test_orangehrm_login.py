import time

import allure
import pytest
from allure_commons.types import AttachmentType

from pageobjects.orangehrm_page import Orangehrm_Login
from utilities import xlutils_orangehrm
from utilities.ReadConfig import ReadConfig

from utilities.orangehrm_logger import LogGenerator


class Test_Orangehrm_Login():
    fpath = "D:\\credence\\Orangehrm_pytest_project\\testcases\\testdata\\orangehrm_login.xlsx"
    log = LogGenerator.loggen()
    con_username = ReadConfig.getuserName()
    con_password = ReadConfig.getuserPassword()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("Page title Test cases")
    @allure.issue("ABC123")
    @allure.story("This is story 1")
    def test_orangehrm_title_01(self, setup):
        self.driver = setup
        time.sleep(2)
        if self.driver.title == "OrangeHRM":
            self.log.info("Taking screenshot")
            time.sleep(1)
            self.driver.save_screenshot(".\\screenshots\\orangehrm title is passed.PNG")
            self.log.info("Tile test case is passed")
            self.driver.close()
            assert True
        else:
            self.log.info("Taking screenshot")
            time.sleep(1)
            self.driver.save_screenshot(".\\screenshots\\orangehrm title is failed.PNG")
            allure.attach(self.driver.get_screenshot_as_png(), name="orangehrm title is failed",
                          attachment_type=AttachmentType.PNG)
            self.log.info("Tile test case is failed\n")

            assert False

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("OrangeHRM Login Test Case")
    @allure.issue("ABC123")
    @allure.story("This is story 2")
    def test_orangehrm_login_02(self, setup):
        self.driver = setup
        self.log.info("Opening browser\n")
        self.olp = Orangehrm_Login(self.driver)
        self.row = xlutils_orangehrm.RowCount(self.fpath, "Sheet1")
        exp_result_list = []
        for r in range(2, self.row + 1):
            self.username = xlutils_orangehrm.ReadData(self.fpath, "Sheet1", r, 2)
            self.password = xlutils_orangehrm.ReadData(self.fpath, "Sheet1", r, 3)
            self.exp_result = xlutils_orangehrm.ReadData(self.fpath, "Sheet1", r, 4)
            self.olp.Enter_Username(self.username)
            self.log.info(f"enter username: {self.username}")
            self.olp.Enter_password(self.password)
            self.log.info(f"Enter password: {self.password}")
            self.olp.Login_Button()
            self.log.info("click login button")
            if self.olp.Login_Status() == True:
                if self.exp_result == 'pass':
                    exp_result_list.append("pass")
                    self.log.info("case is passed")
                    xlutils_orangehrm.WriteData(self.fpath, "Sheet1", r, 5, 'pass')
                    self.driver.save_screenshot(f".\\screenshots\\{self.username}_{self.password}.PNG")
                    allure.attach(self.driver.get_screenshot_as_png(), name=f"{self.username}_{self.password}",
                                  attachment_type=AttachmentType.PNG)
                    self.olp.Menu()
                    self.log.info("Click on menu button")
                    self.olp.SignOut()
                    self.log.info("Click on sign out")
                elif self.exp_result == "fail":
                    exp_result_list.append('fail')
                    self.log.info("case is failed")
                    xlutils_orangehrm.WriteData(self.fpath, "Sheet1", r, 5, 'fail')
                    self.driver.save_screenshot(f".\\screenshots\\{self.username}_{self.password}.PNG")
                    allure.attach(self.driver.get_screenshot_as_png(), name=f"{self.username}_{self.password}",
                                  attachment_type=AttachmentType.PNG)
                    self.olp.Menu()
                    self.log.info("Click on menu button")
                    self.olp.SignOut()
                    self.log.info("Click on sign out")
            elif self.olp.Login_Status() == False:
                if self.exp_result == 'pass':
                    exp_result_list.append('fail')
                    self.log.info("case is failed")
                    xlutils_orangehrm.WriteData(self.fpath, "Sheet1", r, 5, 'fail')
                    self.driver.save_screenshot(f".\\screenshots\\{self.username}_{self.password}.PNG")
                    allure.attach(self.driver.get_screenshot_as_png(), name=f"{self.username}_{self.password}",
                                  attachment_type=AttachmentType.PNG)
                elif self.exp_result == 'fail':
                    exp_result_list.append('pass')
                    self.log.info("case is passed")
                    xlutils_orangehrm.WriteData(self.fpath, "Sheet1", r, 5, 'pass')
                    self.driver.save_screenshot(f".\\screenshots\\{self.username}_{self.password}.PNG")
                    allure.attach(self.driver.get_screenshot_as_png(), name=f"{self.username}_{self.password}",
                                  attachment_type=AttachmentType.PNG)
        print(exp_result_list)
        if 'fail' not in exp_result_list:
            self.log.info("Data derive testing is passed\n")
            assert True
        else:
            self.log.info("Data derive testing is failed\n")
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("OrangeHRM login by Configuration Test Case")
    @allure.issue("ABC123")
    @allure.story("This is story 3")
    # @pytest.mark.only
    def test_orangehrm_login_by_configuration(self, setup):
        self.driver = setup
        self.log.info("Open browser")
        self.olp = Orangehrm_Login(self.driver)
        self.olp.Enter_Username(self.con_username)
        self.log.info(f"enter username: {self.con_username}")
        self.olp.Enter_password(self.con_password)
        self.log.info(f"Enter password: {self.con_password}")
        self.olp.Login_Button()
        self.log.info("click login button")
        time.sleep(2)

        if self.olp.Login_Status() == True:
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name=f"{self.con_username}_{self.con_password}",
                          attachment_type=AttachmentType.PNG)
            self.olp.Menu()
            self.log.info("Click on menu button")
            self.olp.SignOut()
            self.log.info("Click sign-out")
            assert True
        elif self.olp.Login_Status() == False:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"{self.con_username}_{self.con_password}",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("OrangeHRM Login By Parametrized method Test Case")
    @allure.issue("ABC123")
    @allure.story("This is story 4")
    # @pytest.mark.only
    def test_orangehrm_login_parameterized(self, setup, get_data_for_login):
        self.driver = setup
        self.log.info("Open browser")
        self.olp = Orangehrm_Login(self.driver)
        self.olp.Enter_Username(get_data_for_login[0])
        self.log.info(f"enter username: {get_data_for_login[0]}")
        self.olp.Enter_password(get_data_for_login[1])
        self.log.info(f"Enter password: {get_data_for_login[1]}")
        self.olp.Login_Button()
        self.log.info("click login button")
        time.sleep(2)

        if self.olp.Login_Status()==True:
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name=f"{get_data_for_login[0]}_{get_data_for_login[1]}",
                          attachment_type=AttachmentType.PNG)
            assert True

        elif self.olp.Login_Status()==False:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"{get_data_for_login[0]}_{get_data_for_login[1]}",
                          attachment_type=AttachmentType.PNG)
            assert False

# pytest -v -s -n=2 --browser chrome --alluredir="D:\credence\Orangehrm_pytest_project\allure-results"

#pytest -v -n=2 --browser chrome --html=HTML-Reports/orangehrm_test_cases.html
