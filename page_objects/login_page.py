import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.home_page import HomePage
from utilities.base_class import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    email_box = (By.XPATH, "//input[@name='email']")
    password_box = (By.XPATH, "//input[@name='password']")
    forgot_password = (By.XPATH, "//a[normalize-space()='Forgot password?']")
    display_password_eye = (By.XPATH, "//button[@id='button_addon2']")
    sign_up_first_name_box = (By.XPATH, "//input[@placeholder='e.g John']")
    sign_up_last_name_box = (By.XPATH, "//input[@placeholder='e.g Doe']")
    sign_up_mobile_box = (By.XPATH, "//input[@placeholder='e.g 0123456789']")
    whatsapp_number_option_dropdown = (By.XPATH, "//ng-select[@placeholder='Do you have a WhatsApp number?']")
    receive_notification_options = (By.XPATH, "//ng-select[@placeholder='Select an option...']")
    location_text_input = (By.XPATH, "(//input[@type='text'])[5]")
    sign_up_enter_email = (By.XPATH, "//input[@placeholder='e.g example@gmail.com']")
    location_box = (By.XPATH, "//ng-select[@placeholder='Type and select from suggested list']")
    sign_up_enter_password = (By.XPATH, "//input[@name='password']")
    hear_about_us_option = (By.XPATH, "//ng-select[@placeholder='How did you hear about us?']")
    are_you_qualified_popup = (By.XPATH, "//div[@class='modal-content']")

    def fill_in_sign_up_form(self):
        self.driver.find_element(*LoginPage.sign_up_first_name_box).send_keys("Test")
        self.driver.find_element(*LoginPage.sign_up_last_name_box).send_keys("SignUp")
        self.driver.find_element(*LoginPage.sign_up_mobile_box).send_keys("0810810810")
        self.select_ng_select_option_by_text(self.whatsapp_number_option_dropdown, "Same as mobile number")
        self.select_ng_select_option_by_text(self.receive_notification_options, "No")
        self.driver.find_element(*LoginPage.sign_up_enter_email).send_keys("signup1@gmail.com")
        self.driver.execute_script("arguments[0].scrollIntoView();", (self.driver.find_element(*LoginPage.location_box)))
        time.sleep(1)
        self.driver.find_element(*LoginPage.location_box).click()
        self.driver.find_element(*LoginPage.location_text_input).send_keys("C")
        self.select_ng_select_option_by_text(self.location_box, "Cape Town, Western Cape, South Africa")
        self.driver.find_element(*LoginPage.sign_up_enter_password).send_keys("password")
        self.driver.execute_script("arguments[0].scrollIntoView();", (self.driver.find_element(*LoginPage.hear_about_us_option)))
        time.sleep(1)
        self.select_ng_select_option_by_text(self.hear_about_us_option, "Facebook")
        print("successfully filled in sign up form")
        self.click_button_by_text("Register")
        self.wait.until(EC.presence_of_element_located(self.are_you_qualified_popup))
        self.close_popup_if_present("None")

    def perform_signup(self):
        self.click_button_by_text("Sign Up")
        self.click_button_by_text("Job Seeker")
        self.fill_in_sign_up_form()
        self.click_button_by_text("Logout")

    def perform_login(self, email, password):
        self.driver.find_element(*LoginPage.email_box).send_keys(email)
        self.driver.find_element(*LoginPage.password_box).send_keys(password)
        self.click_button_by_text("Log In")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[normalize-space()='Logout']")))
        home_page = HomePage(self.driver)
        return home_page


