import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Emp_Search():
    click_PIM_XPATH = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]")
    text_emp_id_XPATH = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]")
    click_search_button_CSS = (By.CSS_SELECTOR,"button[type='submit']")
    search_result_XPATH = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
    no_record_message_CSS =(By.CSS_SELECTOR,".oxd-toast.oxd-toast--info.oxd-toast-container--toast")
    def __init__(self, driver):
        self.driver = driver
        # self.wait=WebDriverWait(self.driver,3,poll_frequency=0.1)

    def Click_PIM(self):
        self.driver.find_element(*Emp_Search.click_PIM_XPATH).click()

    def Text_Emp_ID(self,id):
        self.driver.find_element(*Emp_Search.text_emp_id_XPATH).send_keys(id)

    def Click_Search_Button(self):
        self.driver.find_element(*Emp_Search.click_search_button_CSS).click()

    def Page_Scroll(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def No_Record_Meassge(self):
        # self.wait.until(expected_conditions.visibility_of_element_located(self.no_record_message_CSS))
        message = self.driver.find_element(*Emp_Search.no_record_message_CSS).text
        print(message)

    def Search_Result(self):
        # time.sleep(2)
        try:
            firstname = self.driver.find_element(*Emp_Search.search_result_XPATH).text
            print(firstname)
            return True
        except:
            return False
