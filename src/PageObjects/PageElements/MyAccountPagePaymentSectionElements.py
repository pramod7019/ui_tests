from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class MyAccountPagePaymentSectionElements(Locators):

    def __init__(self):
        Locators.__init__(self, "MyAccountPagePaymentSectionLocators")

    def get_add_new_card(self):
        return self.get_page_element(By.XPATH, "addNewCard")

    def get_credit_card_number(self):
        return self.get_page_element(By.XPATH, "creditCardNumber")

    def get_credit_card_expiry(self):
        return self.get_page_element(By.XPATH, "creditCardExpiry")

    def get_credit_card_cvc(self):
        return self.get_page_element(By.XPATH, "creditCardCVC")

    def get_select_country(self):
        return self.get_page_element(By.XPATH, "countrySelection")

    def get_street_address(self):
        return self.get_page_element(By.XPATH, "streetAddress")

    def get_appartment(self):
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

    def get_credit_card_validation_text(self):
        return self.get_page_element(By.XPATH, "creditCardValidationText")

    def get_credit_card_expiry_validation_text(self):
        return self.get_page_element(By.XPATH, "creditCardExpiryValidationText")

    def get_credit_card_cvc_validation_text(self):
        return self.get_page_element(By.XPATH, "creditCardCvcValidationText")

    def get_street_address_validation_text(self):
        return self.get_page_element(By.XPATH, "streetAddressValidationText")

    def get_apartment_suite_validation_text(self):
        return self.get_page_element(By.XPATH, "apartmentSuiteValidationText")

    def get_city_validation_text(self):
        return self.get_page_element(By.XPATH, "cityValidationText")

    def get_province_validation_text(self):
        return self.get_page_element(By.XPATH, "provinceValidationText")

    def get_postal_code_validation_text(self):
        return self.get_page_element(By.XPATH, "postalCodeValidationText")

    def get_phone_number_validation_text(self):
        return self.get_page_element(By.XPATH, "phoneNumberValidationText")

    def get_primary_card_checkbox(self):
        return self.get_page_element(By.XPATH, "setprimaryCardCheckbox")

    def get_add_card_button(self):
        return self.get_page_element(By.XPATH, "addCardButton")

    def get_cancel_button(self):
        return self.get_page_element(By.XPATH, "cancelButton")

    def get_edit_card_button(self):
        return self.get_page_element(By.XPATH, "editSavedCardButton")

    def get_update_saved_card(self):
        return self.get_page_element(By.XPATH, "updateSavedCard")

    def get_remove_saved_card(self):
        return self.get_page_element(By.XPATH, "removeSavedCard")

    def get_credit_card_iframe(self):
        return self.get_page_element(By.XPATH, "creditCardIframe")

    def get_street_address_suggestion(self):
        return self.get_page_element(By.XPATH, "streetAddressSuggestion")

    def get_remove_primary_card_from_profile(self):
        return self.get_page_element(By.XPATH, "removePrimaryCardFromProfile")

    def get_remove_secondary_card_from_profile(self):
        return self.get_page_element(By.XPATH, "removeSecondaryCardFromProfile")

    def get_make_card_primary_from_profile(self):
        return self.get_page_element(By.XPATH, "makeCardPrimaryFromProfile")

    def get_remove_all_cards_from_profile(self):
        return self.get_page_element(By.XPATH, "removeAllCardsFromProfile")

    def get_confirm_remove_cards(self):
        return self.get_page_element(By.XPATH, "confirmRemovingCards")

    def get_primary_credit_card(self):
        return self.get_page_element(By.XPATH, "primaryCreditCardText")

