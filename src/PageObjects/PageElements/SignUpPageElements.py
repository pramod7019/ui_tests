from ...Helpers.LocatorDatabase.Locators import Locators
from selenium.webdriver.common.by import By


class SignUpPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "SignUpPageLocators")

    def get_page_title(self):
        return self.get_page_element(By.XPATH, "pageTitle")

    def get_email_field(self):
        return self.get_page_element(By.XPATH, "emailField")

    def get_first_name_field(self):
        return self.get_page_element(By.XPATH, "firstNameField")

    def get_last_name_field(self):
        return self.get_page_element(By.XPATH, "lastNameField")

    def get_password_field(self):
        return self.get_page_element(By.XPATH, "passwordField")

    def get_confirm_password_field(self):
        return self.get_page_element(By.XPATH, "confirmPasswordField")

    def get_create_account_button(self):
        return self.get_page_element(By.XPATH, "createAccountButton")

    def get_show_password_button(self):
        return self.get_page_element(By.XPATH, "showPasswordButton")

    def get_sign_in_button(self):
        return self.get_page_element(By.XPATH, "signInButton")

    def get_join_fb_button(self):
        return self.get_page_element(By.XPATH, "joinFBButton")

    def get_phone_number_field(self):
        return self.get_page_element(By.XPATH, "phoneNumberField")

    def get_postal_code_field(self):
        return self.get_page_element(By.XPATH, "postalCodeField")

    def get_male_radio_button(self):
        return self.get_page_element(By.XPATH, "maleRadioButton")

    def get_female_radio_button(self):
        return self.get_page_element(By.XPATH, "femaleRadioButton")

    def get_dob_day(self):
        return self.get_page_element(By.XPATH, "dobDay")

    def get_dob_month(self):
        return self.get_page_element(By.XPATH, "dobMonth")

    def get_dob_year(self):
        return self.get_page_element(By.XPATH, "dobYear")

    def get_aldo_crew_sign_up_banner(self):
        return self.get_page_element(By.XPATH, "aldoCrewSignUpBanner")

    def get_legal_disclaimer(self):
        return self.get_page_element(By.XPATH, "legalDisclaimer")

    def get_last_name_error_validation(self):
        return self.get_page_element(By.XPATH, "lastNameErrorValidation")

    def get_first_name_error_validation(self):
        return self.get_page_element(By.XPATH, "firstNameErrorValidation")

    def get_email_error_validation(self):
        return self.get_page_element(By.XPATH, "emailErrorValidation")

    def get_phone_number_error_validation(self):
        return self.get_page_element(By.XPATH, "phoneNumberErrorValidation")

    def get_postal_code_error_validation(self):
        return self.get_page_element(By.XPATH, "postalCodeErrorValidation")

    def get_password_error_validation(self):
        return self.get_page_element(By.XPATH, "passwordErrorValidation")

    def get_confirm_password_error_validation(self):
        return self.get_page_element(By.XPATH, "confirmPasswordErrorValidation")

    def get_cis_sign_up_alist_checkbox(self):
        return self.get_page_element(By.XPATH, "cisSignUpAlistCheckbox")

    def get_sign_up_message_bar(self):
        return self.get_page_element(By.XPATH, "signUpMessageBar")

    def get_facebook_page_header(self):
        return self.get_page_element(By.XPATH, "facebookPageheader")
