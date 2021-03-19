from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class MyAccountPageAddressSectionElements(Locators):

    def __init__(self):
        Locators.__init__(self, "MyAccountPageAddressSectionLocators")

    def get_addressbook_title(self):
        return self.get_page_element(By.XPATH, "addressBookTitle")

    def get_add_new_address(self):
        return self.get_page_element(By.XPATH, "addNewAddress")

    def get_first_name(self):
        return self.get_page_element(By.XPATH, "firstNameField")

    def get_last_name(self):
        return self.get_page_element(By.XPATH, "lastNameField")

    def get_street_address(self):
        return self.get_page_element(By.XPATH, "streetAddress")

    def get_apartment_suite(self):
        return self.get_page_element(By.XPATH, "appartmentSuite")

    def get_city(self):
        return self.get_page_element(By.XPATH, "city")

    def get_province(self):
        return self.get_page_element(By.XPATH, "province")

    def get_postal_code(self):
        return self.get_page_element(By.XPATH, "postalCode")

    def get_phone(self):
        return self.get_page_element(By.XPATH, "phone")

    def get_phone_ext(self):
        return self.get_page_element(By.XPATH, "phoneExtension")

    def get_first_name_validation_text(self):
        return self.get_page_element(By.XPATH, "firstnameValidationText")

    def et_last_name_validation_text(self):
        return self.get_page_element(By.XPATH, "lastNameValidationText")

    def get_street_address_validation_text(self):
        return self.get_page_element(By.XPATH, "streetAddressValidationText")

    def get_city_validation_text(self):
        return self.get_page_element(By.XPATH, "cityValidationText")

    def get_province_validation_text(self):
        return self.get_page_element(By.XPATH, "provinceValidationText")

    def get_postal_code_validation_text(self):
        return self.get_page_element(By.XPATH, "postalCodeValidationText")

    def get_phoneno_validation_text(self):
        return self.get_page_element(By.XPATH, "phoneNumberValidationText")

    def get_address_pop_up_button(self):
        return self.get_page_element(By.XPATH, "addressPopUpButton")

    def get_set_primary_address_checkbox(self):
        return self.get_page_element(By.XPATH, "setprimaryAddressCheckbox")

    def get_add_new_address_button(self):
        return self.get_page_element(By.XPATH, "addNewAdressButton")

    def get_cancel_button(self):
        return self.get_page_element(By.XPATH, "cancelButton")

    def get_edit_saved_address(self):
        return self.get_page_element(By.XPATH, "editSavedAddress")

    def get_update_saved_address(self):
        return self.get_page_element(By.XPATH, "updateSavedAddress")

    def get_remove_saved_address(self):
        return self.get_page_element(By.XPATH, "removeSavedAddress")

    def get_street_address_suggestion(self):
        return self.get_page_element(By.XPATH, "streetAddressSuggestion")
