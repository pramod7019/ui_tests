from ..PageElements.SignUpPageElements import SignUpPageElements
import random


class SignUpPage:

    def __init__(self):
        self.__sign_up_page_elements = SignUpPageElements()
        self.__wait_for_sign_up_page()

    def enter_email_address(self, email, new=True):
        self.__sign_up_page_elements.get_email_field().set_text(self.__generate_email(email, new))

    def enter_first_name(self, first_name):
        self.__sign_up_page_elements.get_first_name_field().set_text(first_name)

    def enter_last_name(self, last_name):
        self.__sign_up_page_elements.get_last_name_field().set_text(last_name)

    def enter_password(self, password):
        self.__sign_up_page_elements.get_password_field().set_text(password)

    def enter_confirm_password(self, password):
        self.__sign_up_page_elements.get_confirm_password_field().set_text(password)

    def click_create_account(self):
        self.__sign_up_page_elements.get_create_account_button().click()

    def click_show_password(self):
        self.__sign_up_page_elements.get_show_password_button().click()

    def click_sign_in_with_email(self):
        self.__sign_up_page_elements.get_sign_in_button().click()

    def click_sign_in_with_fb(self):
        self.__sign_up_page_elements.get_join_fb_button().click()

    def enter_phone_number(self, phone_number):
        self.__sign_up_page_elements.get_phone_number_field().set_text(phone_number)

    def enter_postal_code(self, postal_code):
        self.__sign_up_page_elements.get_postal_code_field().set_text(postal_code)

    def click_womens_gender(self):
        self.__sign_up_page_elements.get_female_radio_button().click(wait_for_clickable=False)

    def click_mens_gender(self):
        self.__sign_up_page_elements.get_male_radio_button().click(wait_for_clickable=False)

    def select_dob_date(self, date):
        self.__sign_up_page_elements.get_dob_day().select_drop_drown_value(date)

    def select_dob_month(self, month):
        self.__sign_up_page_elements.get_dob_month().select_drop_drown_value(month)

    def select_dob_year(self, year):
        self.__sign_up_page_elements.get_dob_year().select_drop_drown_value(year)

    def is_thank_you_sign_up_message_bar_displayed(self):
        return self.__sign_up_page_elements.get_sign_up_message_bar().displayed()

    def __random_int(self):
        return random.randint(0, 1000)

    def is_email_error_validation_message_displayed(self):
        return self.__sign_up_page_elements.get_email_error_validation().displayed()

    def is_first_name_error_validation_message_displayed(self):
        return self.__sign_up_page_elements.get_first_name_error_validation().displayed()

    def is_last_name_error_validation_message_displayed(self):
        return self.__sign_up_page_elements.get_last_name_error_validation().displayed()

    def is_phone_number_error_validation_message_displayed(self):
        return self.__sign_up_page_elements.get_phone_number_error_validation().displayed()

    def is_postal_code_error_validation_message_displayed(self):
        return self.__sign_up_page_elements.get_postal_code_error_validation().displayed()

    def is_password_error_validation_message_displayed(self):
        return self.__sign_up_page_elements.get_password_error_validation().displayed()

    def is_confirm_password_error_validation_message_displayed(self):
        return self.__sign_up_page_elements.get_confirm_password_error_validation().displayed()

    def click_cis_sign_up_news_letter(self):
        self.__sign_up_page_elements.get_cis_sign_up_alist_checkbox().click(wait_for_clickable=False)

    def __generate_email(self, email, new):
      if new:
        seperated_email = email.split('@')
        return seperated_email[0] + "+" + str(self.__random_int()) + "@" + seperated_email[1]
      else:
        return email

    def __wait_for_sign_up_page(self):
        self.__sign_up_page_elements.get_sign_in_button().wait_to_appear()
        self.__sign_up_page_elements.get_email_field().wait_to_appear()
        self.__sign_up_page_elements.get_first_name_field().wait_to_appear()

    def is_legal_disclaimer_displayed(self):
        return self.__sign_up_page_elements.get_legal_disclaimer().displayed()

