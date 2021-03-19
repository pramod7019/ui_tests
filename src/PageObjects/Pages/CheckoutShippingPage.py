import time

from ...PageObjects.PageElements.CheckoutPageShippingSectionElements import CheckoutPageShippingSectionElements


class CheckoutShippingPage:

    def __init__(self):
        self.__shipping_elements = CheckoutPageShippingSectionElements()

    def wait_for_shipping_method_details(self):
        self.__shipping_elements.get_shipping_page_title().wait_to_appear()
        self.__shipping_elements.get_shipping_method_title().wait_to_appear()
        self.__shipping_elements.get_shipping_duration_text().wait_to_appear()
        self.__shipping_elements.get_shipping_price().wait_to_appear()

    def fill_email_address(self, email):
        self.__shipping_elements.get_email_field().set_text(email)

    def fill_first_name(self, first_name):
        self.__shipping_elements.get_first_name_field().set_text(first_name)

    # This function does two actions on the same field
    def fill_street_select_address(self, street):
        self.fill_street(street)
        self.__select_address_from_street_field(0)

    def fill_apartment_suite(self, suite):
        self.__shipping_elements.get_appartment_suite_field().set_text(suite)

    def fill_phone_extension(self, phone_extension):
        self.__shipping_elements.get_phone_extension_field().set_text(phone_extension)

    def fill_last_name(self, last_name):
        self.__shipping_elements.get_last_name_field().set_text(last_name)

    def fill_street(self, number_street):
        street_field = self.__shipping_elements.get_street_address_field().get_visible_element()[0]
        street_field.send_keys(number_street)

    def fill_city(self, city):
        city_field = self.__shipping_elements.get_city_field().get_visible_element()[0]
        city_field.send_keys(city)

    def fill_postal_code(self, code):
        self.__shipping_elements.get_postal_code_field().set_text(code)

    def __select_address_from_street_field(self, i):
        self.__shipping_elements.get_street_address_suggestions().get_visible_element()[0].click()

    def fill_phone_number(self, phone):
        phone_number_field = self.__shipping_elements.get_phone_field().get_visible_element()[0]
        phone_number_field.send_keys(phone)

    def select_address_from_default_address(self, i):
        self.__shipping_elements.get_saved_address_radio_button().click_child_element(i)

    def get_default_address_edit_button(self):
        address_element = self.__shipping_elements.get_saved_address_edit_button()
        return len(address_element.get_text_of_child_elements()) if address_element.exists() else 0

    def get_login_header_title(self):
        return self.__shipping_elements.get_login_header_title()

    def select_shipping_method(self, shipping_method):
        shipping_methods_count = len(self.__shipping_elements.get_shipping_radio().get_all_elements())
        shipping = 1 if shipping_method == "Standard" and shipping_methods_count > 1 else 0
        for k in range(0, 2):
            if not self.__shipping_elements.get_shipping_radio().get_all_elements()[shipping].is_selected():
                self.__click_shipping_method(shipping)

    def __click_shipping_method(self, i):
        try:
            self.__shipping_elements.get_shipping_radio().click_child_element(i)
        except:
            self.wait_for_shipping_method_details()
            self.__shipping_elements.get_shipping_radio().click_child_element(i)
        self.wait_for_shipping_method_details()

    def select_province(self, province_code):
        self.__shipping_elements.get_province_field().select_drop_drown_value(province_code)

    # This function does two actions on the same field
    def fill_store_address_select_suggestion(self, street_or_zip):
        store_address_field = self.__shipping_elements.get_store_address_field()
        store_address_field.scrollIntoCenter()
        store_address_field.set_text(street_or_zip)
        self.__shipping_elements.get_street_address_suggestions().click_child_element(0)

    def select_store(self, i):
        self.__shipping_elements.get_store_selection_radio().click_child_element(i)

    def is_first_name_validation_displayed(self):
        return self.__shipping_elements.get_first_name_error_validation_text().displayed()

    def is_last_name_validation_displayed(self):
        return self.__shipping_elements.get_last_name_error_validation_text().displayed()

    def is_street_validation_displayed(self):
        return self.__shipping_elements.get_street_address_error_validation_text().displayed()

    def is_city_validation_displayed(self):
        return self.__shipping_elements.get_city_error_validation_text().displayed()

    def is_province_validation_displayed(self):
        return self.__shipping_elements.get_province_error_validation_text().displayed()

    def is_postal_code_validation_displayed(self):
        return self.__shipping_elements.get_postal_code_error_validation_text().displayed()

    def is_phone_validation_displayed(self):
        return self.__shipping_elements.get_phone_number_error_validation_text().displayed()

    def shipping_price_text(self):
        return self.__shipping_elements.get_shipping_price().get_text_of_child_elements()

    def standard_shipping_price_text(self):
        return self.__shipping_elements.get_standard_shipping_price()

    def express_shipping_price_text(self):
        return self.__shipping_elements.get_express_shipping_price()

    def shipping_duration_text(self):
        return self.__shipping_elements.get_shipping_duration_text().get_text_of_child_elements()

    def is_contact_info_title_displayed(self):
        return self.__shipping_elements.get_contact_information_title().dispalyed()

    def click_on_continue_payment_button(self):
         payment_button_web = self.__shipping_elements.get_continue_payment_button()
         if not payment_button_web.is_clickable():
            self.click_continue_payment(self.__shipping_elements.get_continue_payment_mobile())
         else:
            self.click_continue_payment(payment_button_web)

    def click_continue_payment(self, payment_button):
        payment_button.click()
        if "Guest" in self.get_login_header_title().get_text():
          self.close_address_suggestion_popup()
        payment_button.wait_to_disappear()

    def __click_new_address_radio(self):
        new_address_radio = self.__shipping_elements.get_add_new_address_radio()
        try:
            new_address_radio.click(wait_for_clickable=False)
        except:
            new_address_radio.click(wait_for_clickable=False)

    def select_new_address(self):
        self.__click_new_address_radio()
        if not self.__shipping_elements.get_appartment_suite_field().exists():
          self.__click_new_address_radio()

    def get_first_name_in_field(self):
        return self.wait_for_text_in_field(self.__shipping_elements.get_first_name_field())

    def get_last_name_in_field(self):
        return self.wait_for_text_in_field(self.__shipping_elements.get_last_name_field())

    def wait_for_text_in_field(self, object, wait_time=25):
        start = time.time()
        value = object.get_attribute('value')
        while (time.time() - start) < wait_time:
            if value != "":
                break
            else:
                value = object.get_attribute('value')
        return value

    def click_sign_out_link(self):
        self.__shipping_elements.get_sign_out_link().click()

    def close_address_suggestion_popup(self):
        address_suggestion = self.__shipping_elements.get_address_pop_up_button().wait_to_appear()
        if address_suggestion.exists() & address_suggestion.displayed():
            address_suggestion.click()

    def click_ship_to_store_button(self):
        ship_to_store_radio = self.__shipping_elements.get_ship_to_store_button()
        for k in range(0, 2):
            if not ship_to_store_radio.is_selected():
                try:
                    ship_to_store_radio.js_click()
                except:
                    self.__shipping_elements.get_store_address_field().wait_to_appear()
                    ship_to_store_radio.js_click()
        self.__shipping_elements.get_store_address_field().wait_to_appear()

    def click_on_continue_payment_button_with_no_suggestion(self):
        self.__shipping_elements.get_continue_payment_button().click()
        self.__shipping_elements.get_continue_payment_button().wait_to_disappear()

    def click_sign_in_link(self):
        self.__shipping_elements.get_sign_in_link().click()

    def get_user_email_text(self):
        return self.__shipping_elements.get_user_email().get_text()





