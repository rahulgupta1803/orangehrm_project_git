import os
import time

from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By


class OrangeHRM_Emp_Add():
    click_PIM_XPATH = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]")
    click_add_employee_XPATH = (By.XPATH, "//a[normalize-space()='Add Employee']")
    text_first_name_NAME = (By.NAME, "firstName")
    text_last_name_NAME = (By.NAME, "lastName")
    upload_image_XPATH = (
    By.XPATH, "//button[@class='oxd-icon-button oxd-icon-button--solid-main employee-image-action']")
    click_save_button_css = (By.CSS_SELECTOR, "button[type='submit']")
    text_message_XPATH = (By.XPATH, "//div[@class='oxd-toast-content oxd-toast-content--success']")
    emp_id_XPATH = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')

    def __init__(self, driver):
        self.driver = driver

    def Click_PIM(self):
        self.driver.find_element(*OrangeHRM_Emp_Add.click_PIM_XPATH).click()

    def Click_Add_Emp(self):
        self.driver.find_element(*OrangeHRM_Emp_Add.click_add_employee_XPATH).click()

    def Enter_First_Name(self, fname):
        time.sleep(2)
        self.driver.find_element(*OrangeHRM_Emp_Add.text_first_name_NAME).send_keys(fname)

    def Enter_Last_Name(self, lname):
        time.sleep(2)
        self.driver.find_element(*OrangeHRM_Emp_Add.text_last_name_NAME).send_keys(lname)

    def Upload_Image(self,path):
        self.driver.find_element(*OrangeHRM_Emp_Add.upload_image_XPATH).click()
        time.sleep(8)
        keyboard = Controller()
        keyboard.type(path)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def Emp_Id(self):
        m = self.driver.find_element(*OrangeHRM_Emp_Add.emp_id_XPATH).get_attribute("value")
        return m


    def Save_Button(self):
        time.sleep(2)
        self.driver.find_element(*OrangeHRM_Emp_Add.click_save_button_css).click()

    def Message(self):
        try:
            success = self.driver.find_element(*OrangeHRM_Emp_Add.text_message_XPATH).text
            print(success)
            return True
        except:
            return False
