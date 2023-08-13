import time

from pageobjects.orangehrm_emp_add_page import OrangeHRM_Emp_Add
from pageobjects.orangehrm_page import Orangehrm_Login
from utilities import xlutils_orangehrm
from utilities.ReadConfig import ReadConfig
from utilities.orangehrm_logger import LogGenerator


class Test_Emp_Add_DDT():
    con_username = ReadConfig.getuserName()
    con_password = ReadConfig.getuserPassword()
    log = LogGenerator().loggen()
    fpath = "D:\\credence\\Orangehrm_pytest_project\\testcases\\testdata\\emp_add_ddt.xlsx"

    def test_emp_add_ddt(self,setup):
        self.driver = setup
        self.log.info("Open brower")
        self.olp=Orangehrm_Login(self.driver)
        self.eap= OrangeHRM_Emp_Add(self.driver)

        self.row = xlutils_orangehrm.RowCount(self.fpath,"Sheet1")
        emp_id_list = []
        for r in range (2,self.row+1):
            fname = xlutils_orangehrm.ReadData(self.fpath,"Sheet1",r,2)
            lname = xlutils_orangehrm.ReadData(self.fpath, "Sheet1", r, 3)
            im_path = xlutils_orangehrm.ReadData(self.fpath, "Sheet1", r, 4)
            self.olp.Enter_Username(self.con_username)
            self.log.info(f"Enter username: {self.con_username}")
            self.olp.Enter_password(self.con_password)
            self.log.info(f"Enter password: {self.con_password}")
            self.olp.Login_Button()
            self.log.info("Click login button")
            time.sleep(4)
            self.eap.Click_PIM()
            self.log.info("Click on PIM")
            time.sleep(4)
            self.eap.Click_Add_Emp()
            self.log.info("Click on Add Employee")
            self.eap.Enter_First_Name(fname)
            self.log.info("Enter First Name")
            self.eap.Enter_Last_Name(lname)
            self.log.info("Enter Last Name")
            self.eap.Upload_Image(im_path)
            self.log.info("Upload Image")
            time.sleep(3)
            c = self.eap.Emp_Id()
            xlutils_orangehrm.WriteData(self.fpath,"Sheet1",r,5,c)
            emp_id_list.append(c)
            self.eap.Save_Button()
            self.log.info("Click on save button")
            time.sleep(1)
            if self.eap.Message()==True:
                time.sleep(5)
                self.driver.save_screenshot(f".//screenshots//{fname}_{lname} with mess.png")
                self.log.info("Take Screenshot of successful message")
                xlutils_orangehrm.WriteData(self.fpath,"Sheet1",r,6,"mss_found")
                self.olp.Menu()
                self.log.info("Click on menu")
                self.olp.SignOut()
                self.log.info("Click Sign-out")

            else:
                time.sleep(5)
                self.driver.save_screenshot(f".//screenshots//{fname}_{lname} without mess.png")
                self.log.info("Take Screenshot of unsuccessful message")
                xlutils_orangehrm.WriteData(self.fpath, "Sheet1", r, 6, "mss_not_found")
                self.olp.Menu()
                self.log.info("Click on menu")
                self.olp.SignOut()
                self.log.info("Click Sign-out")

        print(emp_id_list)
        self.log.info("DDT of Add Employee is completed\n")



#pytest -v -s --browser chrome "D:\credence\Orangehrm_pytest_project\testcases\test_emp_add_ddt.py"




