from selenium.webdriver.support.wait import WebDriverWait
from page_objects.my_profile_page import MyProfilePage
from page_objects.all_jobs_page import AllJobsPage
from utilities.base_class import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_my_profile(self):
        self.click_button_by_text("My Profile")
        my_profile = MyProfilePage(self.driver)
        return my_profile

    def go_to_all_jobs(self):
        self.click_button_by_text("All Jobs")
        all_jobs = AllJobsPage(self.driver)
        return all_jobs



