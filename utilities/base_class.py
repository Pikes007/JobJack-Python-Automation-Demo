import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def is_popup_present(self, close_button_text):
        try:
            button_text_xpath = f"//div[@class='modal-content']//button[normalize-space()='{close_button_text}']"
            self.wait.until(EC.presence_of_element_located((By.XPATH, button_text_xpath)))
            return True
        except TimeoutException:
            return False

    def close_popup_if_present(self, close_button_text):
        if self.is_popup_present(close_button_text):
            button_text_xpath = f"//div[@class='modal-content']//button[normalize-space()='{close_button_text}']"
            self.driver.find_element(By.XPATH, button_text_xpath).click()

    def click_button_by_text(self, button_text):
        try:
            button_xpath = f"//button[normalize-space()=\"{button_text}\"] | //div[normalize-space()=\"{button_text}\"] | //a[normalize-space()=\"{button_text}\"]"
            button = self.driver.find_element(By.XPATH, button_xpath)
            button.click()
            print(f"Clicked on button with text: {button_text}")
        except NoSuchElementException as e:
            print(f"Button with text '{button_text}' not found", str(e))

    def select_ng_select_option_by_text(self, locator, text):
        ng_select = self.driver.find_element(*locator)
        ng_select.click()

        option_locator = (By.CLASS_NAME, 'ng-option-label')

        try:
            option = self.wait.until(
                EC.presence_of_element_located(option_locator)
            )
            options = self.driver.find_elements(*option_locator)
            desired_option = next((option for option in options if option.text == text), None)

            if desired_option:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", desired_option)
                self.driver.execute_script("arguments[0].click();", desired_option)
            else:
                print(f"Text {text} not found in ng-select options")
        except TimeoutError:
            print(f"Text '{text}' not found in the ng-select options.")


