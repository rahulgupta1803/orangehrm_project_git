import time

from pageobjects.emp_search_page import Emp_Search
from pageobjects.orangehrm_emp_add_page import OrangeHRM_Emp_Add
from pageobjects.orangehrm_page import Orangehrm_Login
from utilities import xlutils_orangehrm
from utilities.ReadConfig import ReadConfig
from utilities.orangehrm_logger import LogGenerator


class Test_Emp_Search_DDT():
    con_username = ReadConfig.getuserName()
    con_password = ReadConfig.getuserPassword()
    log = LogGenerator().loggen()
    fpath = "D:\\credence\\Orangehrm_pytest_project\\testcases\\testdata\\emp_add_ddt.xlsx"
    def test_emp_search_ddt(self,  setup):
        self.driver = setup
        self.log.info("Open brower")
        self.olp = Orangehrm_Login(self.driver)
        self.eap = OrangeHRM_Emp_Add(self.driver)
        self.esp = Emp_Search(self.driver)
        self.row = xlutils_orangehrm.RowCount(self.fpath, "Sheet1")
        self.olp.Enter_Username(self.con_username)
        self.log.info(f"Enter username: {self.con_username}")
        self.olp.Enter_password(self.con_password)
        self.log.info(f"Enter password: {self.con_password}")
        self.olp.Login_Button()
        self.log.info("Click login button")
        status_list=[]
        for r in range (2,self.row+1):
            emp_id = xlutils_orangehrm.ReadData(self.fpath,"Sheet1",r,5)
            time.sleep(4)
            self.eap.Click_PIM()
            self.log.info("Click on PIM")
            time.sleep(3)
            self.esp.Text_Emp_ID(emp_id)
            time.sleep(2)
            self.esp.Click_Search_Button()
            self.log.info("Click on search button")
            time.sleep(2)
            if self.esp.Search_Result()==True:
                self.esp.Page_Scroll()
                status_list.append('Record found')
                xlutils_orangehrm.WriteData(self.fpath, "Sheet1", r, 7, "Record found")
                time.sleep(2)
                self.driver.save_screenshot(f".//screenshots//{emp_id}.png")
                self.log.info(f"Take screenshot of {emp_id}")
            elif self.esp.Search_Result()==False:
                # time.sleep(1)
                self.esp.No_Record_Meassge()
                self.log.info("Print message")
                self.esp.Page_Scroll()
                status_list.append('Record not found')
                time.sleep(2)
                self.driver.save_screenshot(f".//screenshots//{emp_id} with no record.png")
                self.log.info(f"Take screenshot of {emp_id} having no record")
                xlutils_orangehrm.WriteData(self.fpath, "Sheet1", r, 7, "Record not found")

        print(status_list)

        if "Record not found" not in status_list:
            assert True
        else:
            assert False

        self.log.info("DDT for employee search is completed")


#pytest -v -s --browser chrome "D:\credence\Orangehrm_pytest_project\testcases\test_emp_search_ddt.py"

# /html[1]/body[1]/div[3]/div[3]/div[1]/div[7]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[1]
#
# /html[1]/body[1]/div[3]/div[3]/div[1]/div[7]/div[1]/div[1]/table[1]/tbody[1]/tr[8]/td[2]/a[1]




