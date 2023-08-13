import time

from pageobjects.emp_search_page import Emp_Search
from pageobjects.orangehrm_page import Orangehrm_Login
from utilities.ReadConfig import ReadConfig


class Test_Emp_Search():
    con_username = ReadConfig.getuserName()
    con_password = ReadConfig.getuserPassword()
    def test_emp_search(self,setup):
        self.driver = setup
        self.olp = Orangehrm_Login(self.driver)
        self.esp = Emp_Search(self.driver)
        self.olp.Enter_Username(self.con_username)
        self.olp.Enter_password(self.con_password)
        time.sleep(3)
        self.olp.Login_Button()
        time.sleep(6)
        self.esp.Click_PIM()
        time.sleep(2)
        self.esp.Text_Emp_ID("0268")
        time.sleep(2)
        self.esp.Click_Search_Button()
        time.sleep(2)
        if self.esp.Search_Result()==True:
            self.driver.execute_script("window.scrollBy(0,3000)","")
            time.sleep(10)
            self.driver.save_screenshot(".//screenshots//emp_search.png")
            assert True
        else:
            self.driver.save_screenshot(".//screenshots//emp_search.png")
            assert False



# pytest -v -s --browser chrome "D:\credence\Orangehrm_pytest_project\testcases\test_emp_search.py"






