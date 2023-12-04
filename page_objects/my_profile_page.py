import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.base_class import BaseClass


class MyProfilePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    home_language_option = (By.XPATH, "//ng-select[@placeholder='Add home language']")
    additional_language_option = (By.XPATH, "//ng-select[@placeholder='Add languages']")
    id_number_option = (By.XPATH, "//input[@formcontrolname='RSAID']")
    dob_option = (By.XPATH, "//input[@placeholder='DD/MM/YYYY']")
    personal_info_heading = (By.XPATH, "//span[normalize-space()='Personal & Contact Information']")
    marital_status_option = (By.XPATH, "//ng-select[@placeholder='Add marital status']")
    ethnicity_option = (By.XPATH, "//ng-select[@formcontrolname='ethnicity']")
    criminal_record_option = (By.XPATH, "//ng-select[@formcontrolname='criminalRecord']")
    disability_option = (By.XPATH, "//ng-select[@formcontrolname='hasDisability']")
    gender_option = (By.XPATH, "//ng-select[@formcontrolname='gender']")
    about_yourself_paragraph = (By.XPATH, "//textarea[@formcontrolname='description']")
    location_and_transport_heading = (By.XPATH, "//span[normalize-space()='Location & Transport']")
    transport_option = (By.XPATH, "//ng-select[@placeholder='Add Transport option']")
    drivers_licence_option = (By.XPATH, "//ng-select[@class='ng-select-multiple ng-select ng-select-disabled ")
    relocate_option = (By.XPATH, "//ng-select[@formcontrolname='willingToRelocate']")
    availability_option = (By.XPATH, "//ng-select[@formcontrolname='availability']")
    terms_and_conditions_box = (By.XPATH, "(//input[@type='checkbox'])[2]")
    educational_level_box = (By.XPATH, "//ng-select[@placeholder='Select education level']")
    enter_school_box = (By.XPATH, "//input[@placeholder='Enter School']")
    select_year_box = (By.XPATH, "//ng-select[@placeholder='Select a year']")
    highest_grade_passed_box = (By.XPATH, "//ng-select[@placeholder='Select highest grade']")
    skills_select_no_box = (By.XPATH, "//button[normalize-space()='No']")
    delete_account_password_confirmation = (By.XPATH, "//input[@name='password']")
    reason_for_leaving = (By.XPATH, "//ng-select[@placeholder='-- Reason for leaving --']")
    pop_up_close_button = (By.XPATH, "//div[@class='modal-content']//button[normalize-space()='No Thanks!']")

    def complete_basic_information(self):
        self.click_button_by_text("Basic Information")
        self.select_ng_select_option_by_text(self.home_language_option, "English")
        self.select_ng_select_option_by_text(self.additional_language_option, "None")
        self.driver.find_element(*MyProfilePage.id_number_option).send_keys("8407015099087")
        self.driver.find_element(*MyProfilePage.dob_option).send_keys("01071984")
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   (self.driver.find_element(*MyProfilePage.personal_info_heading)))
        time.sleep(1)
        self.select_ng_select_option_by_text(self.marital_status_option, "Married")
        self.select_ng_select_option_by_text(self.ethnicity_option, "Coloured")
        self.select_ng_select_option_by_text(self.criminal_record_option, "No")
        self.select_ng_select_option_by_text(self.gender_option, "Male")
        self.select_ng_select_option_by_text(self.disability_option, "No")
        self.driver.find_element(*MyProfilePage.about_yourself_paragraph).send_keys("Passionate worker and problem "
                                                                                    "solver, dedicated to continuous "
                                                                                    "improvement, test test test test "
                                                                                    "test test")
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   (self.driver.find_element(*MyProfilePage.location_and_transport_heading)))
        time.sleep(1)
        self.select_ng_select_option_by_text(self.transport_option, "Public Transport")
        self.select_ng_select_option_by_text(self.relocate_option, "Yes")
        self.select_ng_select_option_by_text(self.availability_option, "Permanent")
        self.driver.find_element(*MyProfilePage.availability_option).click()
        self.driver.find_element(*MyProfilePage.terms_and_conditions_box).click()
        self.click_button_by_text("Save changes")

    def complete_experience(self):
        self.click_button_by_text("Experience")
        self.select_ng_select_option_by_text(self.educational_level_box, "High School")
        self.driver.find_element(*MyProfilePage.enter_school_box).send_keys("Parow High School")
        self.select_ng_select_option_by_text(self.select_year_box, "2022")
        self.select_ng_select_option_by_text(self.highest_grade_passed_box, "Matric")
        time.sleep(1)
        self.click_button_by_text("Save changes")

    def complete_skills_select_all_no(self):
        self.click_button_by_text("Skills")
        for i in range(1, 4):
            self.driver.find_element(By.XPATH, f"(//button[normalize-space()='No'])[{i}]").click()
        self.click_button_by_text("Save changes")
        self.close_popup_if_present("Apply to Jobs")
        self.close_popup_if_present("Cancel")
        self.click_button_by_text("Logout")

    def delete_account(self):
        self.close_popup_if_present("None")
        self.click_button_by_text("Delete Account")
        self.click_button_by_text("Yes")
        self.select_ng_select_option_by_text(self.reason_for_leaving, "Found a job on JOBJACK")
        self.driver.find_element(*MyProfilePage.delete_account_password_confirmation).send_keys("password")
        self.click_button_by_text("Delete")
        self.close_popup_if_present("Close")
