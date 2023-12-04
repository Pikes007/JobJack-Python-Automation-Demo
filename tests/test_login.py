import pytest
from page_objects.login_page import HomePage, LoginPage
from utilities.base_class import BaseClass


class TestLogin(BaseClass):
    @pytest.mark.web
    def test_sign_up(self):
        login = LoginPage(self.driver)
        login.perform_signup()

    @pytest.mark.web
    def test_complete_profile(self):
        login = LoginPage(self.driver)
        home = login.perform_login("signup1@gmail.com", "password")
        my_profile = home.go_to_my_profile()
        my_profile.complete_basic_information()
        my_profile.complete_experience()
        my_profile.complete_skills_select_all_no()

    @pytest.mark.web
    def test_log_in_retrieve_jobs(self):
        login = LoginPage(self.driver)
        home = login.perform_login("signup1@gmail.com", "password")
        all_jobs = home.go_to_all_jobs()
        print(all_jobs.retrieve_cards(all_jobs.job_ad_cards))
        self.click_button_by_text("Resources")
        print(all_jobs.retrieve_cards(all_jobs.resource_cards))

    @pytest.mark.web
    def test_delete_account(self):
        login = LoginPage(self.driver)
        home = login.perform_login("signup1@gmail.com", "password")
        my_profile = home.go_to_my_profile()
        my_profile.delete_account()






