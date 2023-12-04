from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.base_class import BaseClass


class AllJobsPage(BaseClass):
    def __init__ (self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    job_ad_cards = (By.XPATH, "//div[@class = 'my-3 col-md-6 col-lg-4']")
    resource_cards = (By.XPATH, "//app-resource-card")

    def retrieve_cards(self, locator):
        self.close_popup_if_present("Cancel")
        retrieved_cards = []

        while True:
            initial_card_count = len(retrieved_cards)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                self.wait.until(lambda driver: len(self.driver.find_elements(*locator)) > initial_card_count)
                all_cards = self.driver.find_elements(*locator)
                new_cards = all_cards[initial_card_count:]
                if all(card.is_displayed() for card in new_cards):
                    for card in new_cards:
                        retrieved_cards.append(f"\n{card.text}")
                else:
                    print("Not all new cards are visible. Assuming end of page.")
                    break
            except TimeoutException:
                print(f"No more cards. {len(retrieved_cards)} items retrieved. Assuming end of page.")
                break

        return '\n'.join(retrieved_cards)
