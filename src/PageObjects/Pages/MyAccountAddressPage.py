from uitests.src.PageObjects.PageElements.MyAccountPageAddressSectionElements import MyAccountPageAddressSectionElements


class MyAccountAddressSectionPage:

    def __init__(self):
        self.__address_section_page_elements = MyAccountPageAddressSectionElements()
        #self.__wait_for_address_section_page()

    def __wait_for_address_section_page(self):
        self.__address_section_page_elements.get_addressbook_title().wait_to_appear()
        self.__address_section_page_elements.get_add_new_address().wait_to_appear()

    def click_on_add_new_address(self):
        self.__address_section_page_elements.get_add_new_address().click()

    def enter_first_name(self, first_name):
        self.__address_section_page_elements.get_first_name().set_text(first_name)

    def enter_last_name(self, last_name):
        self.__address_section_page_elements.get_last_name().set_text(last_name)

    def enter_street(self, number_street):
        self.__address_section_page_elements.get_street_address().set_text(number_street)

    def __select_street_address(self, i):
        self.__address_section_page_elements.get_street_address_suggestion().click_child_element(i)

    #This function does teo actions on same field
    def fill_street_select_address(self, street):
        self.enter_street(street)
        self.__select_street_address(0)

    def enter_apartment_suite(self, suite):
        self.__address_section_page_elements.get_apartment_suite().set_text(suite)

    def enter_city(self, city):
        self.__address_section_page_elements.get_city().set_text(city)

    def select_province(self, province):
        self.__address_section_page_elements.get_province().select_drop_drown_value(province)

    def enter_postal_code(self, postal_code):
        self.__address_section_page_elements.get_postal_code().set_text(postal_code)

    def enter_phone_number(self, phone):
        self.__address_section_page_elements.get_phone().set_text(phone)

    def enter_phone_extension(self, phone_extension):
        self.__address_section_page_elements.get_phone_ext().set_text(phone_extension)

    def click_on_primary_address_checkbox(self):
        self.__address_section_page_elements.get_set_primary_address_checkbox().click()

    def click_on_add_new_address_button(self):
        self.__address_section_page_elements.get_add_new_address_button().click()

    def close_address_suggestion_popup(self):
        address_suggestion = self.__address_section_page_elements.get_address_pop_up_button()
        if address_suggestion.exists() & address_suggestion.displayed():
            address_suggestion.click()

    def click_cancel_address_button(self):
        self.__address_section_page_elements.get_cancel_button().click()

    def click_edit_address(self):
        self.__address_section_page_elements.get_edit_saved_address().click()

    def click_update_address(self):
        self.__address_section_page_elements.get_update_saved_address().click()

    def click_remove_address(self):
        self.__address_section_page_elements.get_remove_saved_address().click()

    def is_first_name_validation_displayed(self):
        return self.__address_section_page_elements.get_first_name_validation_text().displayed()

    def is_last_name_validation_displayed(self):
        return self.__address_section_page_elements.et_last_name_validation_text().displayed()

    def is_street_validation_displayed(self):
        return self.__address_section_page_elements.get_street_address_validation_text().displayed()

    def is_city_validation_displayed(self):
        return self.__address_section_page_elements.get_city_validation_text().displayed()

    def is_province_validation_displayed(self):
        return self.__address_section_page_elements.get_province_validation_text().displayed()

    def is_postal_code_validation_displayed(self):
        return self.__address_section_page_elements.get_postal_code_validation_text().displayed()

    def is_phone_number_validation_displayed(self):
        return self.__address_section_page_elements.get_phoneno_validation_text().displayed()
