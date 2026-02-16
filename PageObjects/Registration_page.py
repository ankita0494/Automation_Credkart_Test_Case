from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Login_Page import Login_Page_Class


class Registration_Page_Class(Login_Page_Class):
    text_name_id="name"
    text_confirm_password_id="password-confirm"

    def enter_name(self, name):
        self.driver.find_element(By.ID, self.text_name_id).send_keys(name)
    def enter_confirm_password_id(self, confirm_password_id):
        self.driver.find_element(By.ID, self.text_confirm_password_id).send_keys(confirm_password_id)

