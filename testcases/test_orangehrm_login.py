import time

from pageobjects.orangehrm_page import Orangehrm_Login
from utilities import xlutils_orangehrm
from utilities.orangehrm_logger import LogGenerator


class Test_Orangehrm_Login():
    fpath = "D:\\credence\\Orangehrm_pytest_project\\testcases\\testdata\\orangehrm_login.xlsx"
    log = LogGenerator.loggen()

    def test_orangehrm_title_01(self,setup):
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
            self.log.info("Tile test case is failed")
            self.driver.close()
            assert False

    def test_orangehrm_login_02(self,setup):
        self.driver = setup
        self.log.info("Opening browser")
        self.olp = Orangehrm_Login(self.driver)
        self.row = xlutils_orangehrm.RowCount(self.fpath,"Sheet1")
        exp_result_list = []
        for r in range(2,self.row+1):
            self.username = xlutils_orangehrm.ReadData(self.fpath,"Sheet1",r,2)
            self.password = xlutils_orangehrm.ReadData(self.fpath,"Sheet1",r,3)
            self.exp_result = xlutils_orangehrm.ReadData(self.fpath,"Sheet1",r,4)
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
                    xlutils_orangehrm.WriteData(self.fpath,"Sheet1",r,5,'pass')
                    self.driver.save_screenshot(f".\\screenshots\\{self.username}_{self.password}.PNG")
                    self.olp.Menu()
                    self.olp.SignOut()
                elif self.exp_result =="fail":
                    exp_result_list.append('fail')
                    self.log.info("case is failed")
                    xlutils_orangehrm.WriteData(self.fpath, "Sheet1", r, 5, 'fail')
                    self.driver.save_screenshot(f".\\screenshots\\{self.username}_{self.password}.PNG")
                    self.olp.Menu()
                    self.olp.SignOut()
            elif self.olp.Login_Status() == False:
                if self.exp_result == 'pass':
                    exp_result_list.append('fail')
                    self.log.info("case is failed")
                    xlutils_orangehrm.WriteData(self.fpath, "Sheet1", r, 5, 'fail')
                    self.driver.save_screenshot(f".\\screenshots\\{self.username}_{self.password}.PNG")
                elif self.exp_result == 'fail':
                    exp_result_list.append('pass')
                    self.log.info("case is passed")
                    xlutils_orangehrm.WriteData(self.fpath, "Sheet1", r, 5, 'pass')
                    self.driver.save_screenshot(f".\\screenshots\\{self.username}_{self.password}.PNG")
        print(exp_result_list)
        if 'fail' not in exp_result_list:
            self.log.info("Data derive testing is passed")
            assert True
        else:
            self.log.info("Data derive testing is failed")
            assert False
