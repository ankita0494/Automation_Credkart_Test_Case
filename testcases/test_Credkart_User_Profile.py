import allure
import pytest
from faker import Faker

from PageObjects.Login_Page import Login_Page_Class
from PageObjects.Registration_page import Registration_Page_Class
from utilities.Logger import log_generator_class
from utilities.readConfig import readconfigclass

@pytest.mark.usefixtures("browser_setup")
class Test_User_Profile:
    driver = None
    email_id=readconfigclass.get_data_for_email()
    pass_word=readconfigclass.get_data_for_password()
    login_url=readconfigclass.get_data_login_url()
    registration_url=readconfigclass.get_data_registration_url()
    log=log_generator_class.log_gen_method()

    def test_verify_credkart_url_001(self):
        # self.log.debug("This is debug message")
        # self.log.info("This is info message")
        # self.log.warning("This is warning message")
        # self.log.error("This is error message")
        # self.log.critical("This is critical message")
        self.log.info(f"Verifying credkart url 001 started")
        self.driver.maximize_window()
        self.driver.get(self.login_url)
        self.log.info(f"Opening the Browser and getting {self.login_url}")
        self.log.info(f"Checking driver title")
        if self.driver.title=="CredKart":
            self.log.info(f"test case for credkart url 001 is passed")
            self.log.info(f"Taking screenshots")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_credkart_url_001_Pass.png")
        else:
            self.log.info(f"test case for credkart url 001 is failed")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_credkart_url_001_Fail.png")
            assert False
        self.log.info(f"Verifying credkart url 001 complete")
    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=1,reruns_delay=1)
    @pytest.mark.depend(depends=["test_verify_credkart_url_001"])
    @pytest.mark.order(1)
    @allure.title("Test User Profile")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic("Epic:Userprofile")
    @allure.link(login_url)
    @allure.story("CredKart:Login")
    @allure.feature("test_verify_credkart_url_001")
    def test_Credkart_Login_007(self):
        self.log.info(f"Verifying credkart_login 002 started")
        self.driver.get(self.login_url)
        self.driver.maximize_window()
        self.log.info(f"Opening the Browser and getting {self.login_url}")
        #email_id = "Credence_user_4494@gmail.com"
        #pass_word = "Credence_user_100@124"
        self.lb=Login_Page_Class(self.driver)
            # enter username
        self.log.info(f"Entering email id {self.email_id}")
        self.lb.Enter_Email(self.email_id)
            # password
        self.log.info(f"Entering password {self.pass_word}")
        self.lb.Enter_Password(self.pass_word)
            # login button
        self.log.info(f"click on login button")
        self.lb.Click_Login_Register_Button()

        if self.lb.verify_menu_button_visibility():
          self.log.info(f"Verifying user login is successful")
          self.driver.save_screenshot(f".\\Screenshots\\user_login_success_{self.email_id}.png")
          self.log.info(f"clicking on menu button")
          self.lb.Click_Menu_button()
          self.log.info(f"Clicking on logoff button")
          self.lb.Click_Logout_button()
        else:
            self.log.info(f"Verifying user login is failed")
            self.driver.save_screenshot(f".\\Screenshots\\user_login_fail_{self.email_id}.png")
            allure.attach.file(f".\\Screenshots\\user_login_fail_{self.email_id}.png",attachment_type=allure.attachment_type.PNG)
            assert False,"User Login Failed"
        self.log.info(f"Test case for credkart login completed")
    @pytest.mark.smoke
    @allure.title("Test User Profile")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic("Epic:Userprofile")
    @allure.link(registration_url)
    @allure.story("CredKart:Registration")
    @allure.feature("test_verify_credkart_url_002")
    def test_Credkart_Registration_002(self):
        self.log.info(f"Verifying credkart_register 002 started")
        self.driver.get(self.registration_url)
        self.log.info(f"Opening the Browser and getting {self.registration_url}")
        self.driver.maximize_window()
        fake_name=Faker().name()
        fake_email=Faker().email()
        pass_word = "Credence_user_100@448"
        confirm_password_id = "Credence_user_100@448"
        self.rp=Registration_Page_Class(self.driver)
        self.log.info(f"Entering fake name {fake_name}")
        self.rp.enter_name(fake_name)
        self.log.info(f"Entering fake email {fake_email}")
        self.rp.Enter_Email(fake_email)
        self.log.info(f"Entering password {pass_word}")
        self.rp.Enter_Password(pass_word)
        self.log.info(f"Entering confirm password {confirm_password_id}")
        self.rp.enter_confirm_password_id(confirm_password_id)
        self.log.info(f"Click on Register button")
        self.rp.Click_Login_Register_Button()

        if self.rp.verify_menu_button_visibility():
          self.log.info(f"Verifying user register is successful")
          self.driver.save_screenshot(f".\\Screenshots\\user_registration_success_{fake_email}.png")
          self.log.info(f"clicking on menu button")
          self.rp.Click_Menu_button()
          self.log.info(f"Clicking on logout button")
          self.rp.Click_Logout_button()
        else:
            self.log.info(f"Verifying user register is failed")
            self.driver.save_screenshot(f".\\Screenshots\\user_registration_fail_{fake_email}.png")
            assert False,"User registration Failed"
        self.log.info(f"Test case for registration completed")



        # wait = WebDriverWait(self.driver, 10)
        # try:
        #     wait.until(
        #     expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
        #     element = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
        #     print("user login successful")
        #     self.driver.save_screenshot(f"User login Successful_{email_id}.png")
        #     menu = self.driver.find_element(By.CSS_SELECTOR, "a[role='button']")
        #     menu.click()
        #     logout = self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        #     logout.click()
        # except:
        #     print("user login failed")
        #     self.driver.save_screenshot(f"User login Failed.png")
        #     assert False, "user login failed"
