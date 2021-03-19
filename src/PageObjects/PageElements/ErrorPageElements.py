from selenium.webdriver.common.by import By
from uitests.src.Helpers.LocatorDatabase.Locators import Locators


class ErrorPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "ErrorPageLocators")

    def get_error_modal_title(self):
        return self.get_page_element(By.XPATH, "errorModalTitle")

    def get_error_message(self):
        return self.get_page_element(By.ID, "errorMessage")

    def get_error_code(self):
        return self.get_page_element(By.ID, "errorCode")

    def get_chat_button(self):
        return self.get_page_element(By.XPATH, "chatButton")

    def get_continue_button(self):
        return self.get_page_element(By.XPATH, "continueButton")

    def get_close_button(self):
        return self.get_page_element(By.XPATH, "closeButton")
