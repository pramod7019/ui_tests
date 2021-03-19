import time

from uitests.src.PageObjects.PageElements.MyAccountPagePaymentSectionElements import MyAccountPagePaymentSectionElements


class MyAccountPaymentSectionPage:

    def __init__(self):
        self.__payment_section_page_elements = MyAccountPagePaymentSectionElements()

    def __wait_for_payment_section_page(self):
        self.__payment_section_page_elements.get_add_new_card().wait_to_appear()

    def click_on_add_new_credit_card(self):
        self.__payment_section_page_elements.get_add_new_card().click()

    def enter_credit_card_number(self, card_number):
        self.__payment_section_page_elements.get_credit_card_iframe().switch_to_iframe()
        self.__payment_section_page_elements.get_credit_card_number().set_text(card_number)
        self.__payment_section_page_elements.get_credit_card_iframe().switch_to_default()

    def enter_card_expiry(self, card_expiry):
        self.__payment_section_page_elements.get_credit_card_expiry().set_text(card_expiry)

    def enter_cvc(self, cvv):
        self.__payment_section_page_elements.get_credit_card_cvc().set_text(cvv)

    def select_country(self, country):
        self.__payment_section_page_elements.get_select_country().select_drop_drown_value(country)

    def enter_street(self, number_street):
        self.__payment_section_page_elements.get_street_address().set_text(number_street)

    def __select_street_address(self, i):
        time.sleep(3)
        self.__payment_section_page_elements.get_street_address_suggestion().get_visible_element()[0].click()

    # This function does teo actions on same field
    def fill_street_select_address(self, street):
        self.enter_street(street)
        self.__select_street_address(0)

    def enter_apartment_suite(self, suite):
        self.__payment_section_page_elements.get_appartment().set_text(suite)

    def enter_city(self, city):
        self.__payment_section_page_elements.get_city().set_text(city)

    def select_province(self, province):
        self.__payment_section_page_elements.get_province().select_drop_drown_value(province)

    def enter_postal_code(self, postal_code):
        self.__payment_section_page_elements.get_postal_code().set_text(postal_code)

    def enter_phone_number(self, phone):
        self.__payment_section_page_elements.get_phone().set_text(phone)

    def enter_phone_extension(self, phone_extension):
        self.__payment_section_page_elements.get_phone_ext().set_text(phone_extension)

    def click_on_make_card_primary_checkbox(self):
        self.__payment_section_page_elements.get_primary_card_checkbox().click()

    def click_on_add_card_button(self):
        for i in range(0, 2):
            if self.__payment_section_page_elements.get_add_card_button().displayed():
                self.__payment_section_page_elements.get_add_card_button().click()

    def click_cancel_card_button(self):
        self.__payment_section_page_elements.get_cancel_button().click()

    def click_on_edit_card_button(self):
        self.__payment_section_page_elements.get_edit_card_button().click()

    def is_edit_card_button_displayed(self):
        edit_button = self.__payment_section_page_elements.get_edit_card_button()
        if edit_button.exists():
            return edit_button.displayed()
        else:
            return True

    def click_update_card(self):
        self.__payment_section_page_elements.get_update_saved_card().click()

    def click_remove_card(self):
        self.__payment_section_page_elements.get_remove_saved_card().click()

    def is_credit_card_validation_displayed(self):
        return self.__payment_section_page_elements.get_credit_card_validation_text().displayed()

    def is_credit_card_expiry_validation_displayed(self):
        return self.__payment_section_page_elements.get_credit_card_expiry_validation_text().displayed()

    def is_credit_card_cvc_validation_displayed(self):
        return self.__payment_section_page_elements.get_credit_card_cvc_validation_text().displayed()

    def is_street_address_validation_displayed(self):
        return self.__payment_section_page_elements.get_street_address_validation_text().displayed()

    def is_apartment_suite_validation_displayed(self):
        return self.__payment_section_page_elements.get_apartment_suite_validation_text().displayed()

    def is_city_validation_displayed(self):
        return self.__payment_section_page_elements.get_city_validation_text().displayed()

    def is_province_validation_displayed(self):
        return self.__payment_section_page_elements.get_province_validation_text().displayed()

    def is_phone_number_validation_displayed(self):
        return self.__payment_section_page_elements.get_phone_number_validation_text().displayed()

    def click_remove_primary_card_from_profile(self):
        self.__payment_section_page_elements.get_remove_primary_card_from_profile().click()

    def click_remove_secondary_card_from_profile(self):
        self.__payment_section_page_elements.get_remove_secondary_card_from_profile().click()

    def click_make_card_primary_from_profile(self):
        self.__payment_section_page_elements.get_make_card_primary_from_profile().click()

    def remove_all_payment_cards_from_account_profile(self):
        remove_cards = self.__payment_section_page_elements.get_remove_all_cards_from_profile()
        while remove_cards.exists():
            try:
                remove_cards.click()
                self.__payment_section_page_elements.get_confirm_remove_cards().click()
            except:
                break

    def remove_payments_for_each_saved_card(self):
        edit_cards = self.__payment_section_page_elements.get_edit_card_button()
        while edit_cards.exists():
            try:
                edit_cards.click()
                self.__payment_section_page_elements.get_remove_saved_card().click()
            except:
                break

    def primary_credit_card_text(self):
        return self.__payment_section_page_elements.get_primary_credit_card().get_text()

    def verify_primary_credit_card_text(self, wait_time=20):
        primary_card = self.__payment_section_page_elements.get_primary_credit_card()
        before_click = primary_card.get_text()
        self.click_make_card_primary_from_profile()
        start = time.time()
        while (time.time() - start) < wait_time:
            if before_click != primary_card.get_text():
                break
        return primary_card.get_text()

    def select_edit_card_button_by_index(self, i, creditcard, shipping):
        edit_cards = self.__payment_section_page_elements.get_edit_card_button()
        if edit_cards.exists():
            if len(edit_cards.get_all_elements()) == 1:
                edit_cards.click()
            else:
                edit_cards.get_all_elements()[i].click()
        else:
            self.click_on_add_new_credit_card()
            self.enter_credit_card_number(creditcard['Cardnumber'])
            self.enter_card_expiry(creditcard['Date'])
            self.enter_cvc(creditcard['Cvv'])
            self.fill_street_select_address(shipping.street)
            self.enter_phone_number(shipping.phone)
            self.click_on_add_card_button()
            self.click_on_edit_card_button()
