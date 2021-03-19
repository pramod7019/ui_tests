from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class SignInPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "SignInPageLocators")

    def get_page_title_text(self):
        return self.get_page_element(By.XPATH, "pageTitle")

    def get_user_name_field(self):
        return self.get_page_element(By.ID, "userNameField")

    def get_password_field(self):
        return self.get_page_element(By.ID, "passwordField")

    def get_sign_in_button(self):
        return self.get_page_element(By.XPATH, "signInButton")

    def get_sign_in_error_text(self):
        return self.get_page_element(By.XPATH, "signInErrorText")

    def get_register_button(self):
        return self.get_page_element(By.XPATH, "registerButton")

    def get_sign_in_with_facebook_button(self):
        return self.get_page_element(By.XPATH, "signInWithFacebookButton")

    def get_disabled_sign_in_button(self):
        return self.get_page_element(By.XPATH, "signInButtonDisabled")

    def get_forgot_password_button(self):
        return self.get_page_element(By.XPATH, "forgotPasswordButton")

    def get_show_password_button(self):
        return self.get_page_element(By.XPATH, "showPasswordButton")

    def get_sign_in_overlay_close_button(self):
        return self.get_page_element(By.XPATH, "signInOverlayCloseButton")

    def get_user_name_error_validation_text(self):
        return self.get_page_element(By.XPATH, "userNameErrorValidationText")

    def get_password_error_validation_text(self):
        return self.get_page_element(By.XPATH, "passwordErrorValidationText")
