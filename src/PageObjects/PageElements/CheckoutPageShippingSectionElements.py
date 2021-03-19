from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class CheckoutPageShippingSectionElements(Locators):

    def __init__(self):
        Locators.__init__(self, "CheckoutPageShippingSectionLocators")

    def get_shipping_page_title(self):
        return self.get_page_element(By.XPATH, "shippingTitle")

    def get_shipping_radio(self):
        return self.get_page_element(By.XPATH, "shippingRadio")

    def get_shipping_method_title(self):
        return self.get_page_element(By.XPATH, "shippingMethodTitle")

    def get_shipping_duration_text(self):
        return self.get_page_element(By.XPATH, "shippingDuration")

    def get_shipping_price(self):
        return self.get_page_element(By.XPATH, "shippingPrice")

    def get_standard_shipping_price(self):
        return self.get_page_element(By.XPATH, "standardShippingPrice")

    def get_express_shipping_price(self):
        return self.get_page_element(By.XPATH, "expressShippingPrice")

    def get_sign_in_link(self):
        return self.get_page_element(By.XPATH, "signInLink")

    def get_contact_information_title(self):
        return self.get_page_element(By.XPATH, "contactInformationTitle")

    def get_email_field(self):
        return self.get_page_element(By.ID, "email")

    def get_first_name_field(self):
        return self.get_page_element(By.ID, "firstName")

    def get_last_name_field(self):
        return self.get_page_element(By.ID, "lastName")

    def get_street_address_field(self):
        return self.get_page_element(By.ID, "streetAddress")

    def get_street_address_suggestions(self):
        return self.get_page_element(By.XPATH, "streetAddressSuggestion")

    def get_appartment_suite_field(self):
        return self.get_page_element(By.ID, "appartmentSuite")

    def get_city_field(self):
        return self.get_page_element(By.ID, "city")

    def get_province_field(self):
        return self.get_page_element(By.ID, "province")

    def get_postal_code_field(self):
        return self.get_page_element(By.ID, "postalCode")

    def get_phone_field(self):
        return self.get_page_element(By.ID, "phone")

    def get_phone_extension_field(self):
        return self.get_page_element(By.ID, "phoneExtension")

    def get_email_error_validation_text(self):
        return self.get_page_element(By.XPATH, "emailValidationText")

    def get_first_name_error_validation_text(self):
        return self.get_page_element(By.XPATH, "firstnameValidationText")

    def get_last_name_error_validation_text(self):
        return self.get_page_element(By.XPATH, "lastNameValidationText")

    def get_street_address_error_validation_text(self):
        return self.get_page_element(By.XPATH, "streetAddressValidationText")

    def get_city_error_validation_text(self):
        return self.get_page_element(By.XPATH, "cityValidationText")

    def get_province_error_validation_text(self):
        return self.get_page_element(By.XPATH, "provinceValidationText")

    def get_postal_code_error_validation_text(self):
        return self.get_page_element(By.XPATH, "postalCodeValidationText")

    def get_phone_number_error_validation_text(self):
        return self.get_page_element(By.XPATH, "phoneNumberValidationText")

    def get_saved_address_radio_button(self):
        return self.get_page_element(By.XPATH, "savedAddressRadio")

    def get_saved_address_type_title(self):
        return self.get_page_element(By.XPATH, "savedAddressTypeTitle")

    def get_saved_address_text(self):
        return self.get_page_element(By.XPATH, "savedAddressText")

    def get_saved_address_edit_button(self):
        return self.get_page_element(By.XPATH, "savedAddressEditButton")

    def get_login_header_title(self):
        return self.get_page_element(By.XPATH, "loginHeaderTitle")

    def get_cis_news_letter_checkbox(self):
        return self.get_page_element(By.ID, "cisNewsLetterCheckbox")

    def get_store_selection_radio(self):
        return self.get_page_element(By.XPATH, "storeLocatorRadio")

    def get_store_address_field(self):
        return self.get_page_element(By.XPATH, "storeAddress")

    def get_store_address_suggestion(self):
        return self.get_page_element(By.ID, "storeAddressSuggestion")

    def get_continue_payment_button(self):
        return self.get_page_element(By.XPATH, "continuePayment")

    def get_add_new_address_radio(self):
        return self.get_page_element(By.XPATH, "addNewAddress")

    def get_sign_out_link(self):
        return self.get_page_element(By.XPATH, "signOutLink")

    def get_address_pop_up_button(self):
        return self.get_page_element(By.XPATH, "addressPopUpButton")

    def get_ship_to_store_button(self):
        return self.get_page_element(By.XPATH, "shipToStoreMode")

    def get_user_email(self):
        return self.get_page_element(By.XPATH, "userEmail")

    def get_continue_payment_mobile(self):
        return self.get_page_element(By.XPATH, "continuePaymentMobile")
