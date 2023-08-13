import time

from pageobjects.orangehrm_emp_add_page import OrangeHRM_Emp_Add
from pageobjects.orangehrm_page import Orangehrm_Login
from utilities.ReadConfig import ReadConfig


class Test_Orangehrm_Emp_Add():
    con_username = ReadConfig().getuserName()
    con_password = ReadConfig().getuserPassword()


    def test_orangehrm_emp_add(self,setup):
        self.driver = setup
        self.olp = Orangehrm_Login(self.driver)
        self.oaep = OrangeHRM_Emp_Add(self.driver)
        self.olp.Enter_Username(self.con_username)
        self.olp.Enter_password(self.con_password)
        time.sleep(3)
        self.olp.Login_Button()
        time.sleep(6)
        self.oaep.Click_PIM()
        time.sleep(3)
        self.oaep.Click_Add_Emp()
        self.oaep.Enter_First_Name('Rahul')
        self.oaep.Enter_Last_Name('Gupta')
        time.sleep(2)
        self.oaep.Upload_Image("D:\\credence\\random photos\\anime1.jpg")
        time.sleep(3)
        self.driver.save_screenshot(".//screenshots//image_upload.png")
        time.sleep(2)
        self.oaep.Save_Button()
        time.sleep(1)
        if self.oaep.Message()==True:
            self.olp.Menu()
            self.olp.SignOut()
            assert True
        else:
            self.olp.Menu()
            self.olp.SignOut()
            assert False

#pytest -v -s --browser chrome "D:\credence\Orangehrm_pytest_project\testcases\test_orangehrm_emp_add.py"