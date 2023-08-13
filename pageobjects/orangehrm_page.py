import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Orangehrm_Login():
    text_username_NAME = (By.NAME,"username")
    text_password_NAME = (By.NAME,"password")
    click_login_button_XPATH = (By.XPATH,"//button[@type='submit']")
    click_menu_css = (By.CSS_SELECTOR,".oxd-userdropdown-tab")
    click_signout_LINK_Text = (By.LINK_TEXT,"Logout")
    login_status_css = (By.CSS_SELECTOR,".oxd-userdropdown-tab")

    def __init__(self,driver):
        self.driver = driver
        # self.wait = WebDriverWait(self.driver,10)


    def Enter_Username(self,username):
        time.sleep(2)
        # self.wait.until(EC.visibility_of_element_located(self.text_username_XPATH))
        self.driver.find_element(*Orangehrm_Login.text_username_NAME).send_keys(username)

    def Enter_password(self,password):
        time.sleep(2)
        # self.wait.until(EC.visibility_of_element_located(self.text_password_XPATH))
        self.driver.find_element(*Orangehrm_Login.text_password_NAME).send_keys(password)


    def Login_Button(self):
        time.sleep(2)
        # self.wait.until(EC.visibility_of_element_located(self.click_login_button_XPATH))
        self.driver.find_element(*Orangehrm_Login.click_login_button_XPATH).click()

    def Menu(self):
        time.sleep(5)
        # self.wait.until(EC.visibility_of_element_located(self.click_menu_XPATH))
        self.driver.find_element(*Orangehrm_Login.click_menu_css).click()

    def SignOut(self):
        time.sleep(5)
        # self.wait.until(EC.visibility_of_element_located(self.click_signout_XPATH))
        self.driver.find_element(*Orangehrm_Login.click_signout_LINK_Text).click()


    def Login_Status(self):
        time.sleep(3)
        # self.wait.until(EC.visibility_of_element_located(self.login_status_XPATH))
        try:
            self.driver.find_element(*Orangehrm_Login.login_status_css)
            return True
        except:
            return False


