import time

from uitests.src.PageObjects.PageElements.MyAccountPageInfoSectionElements import MyAccountPageInfoSectionElements
import random, string

class MyAccountInfoSectionPage:

    def __init__(self):
        self.__info_section_elements = MyAccountPageInfoSectionElements()

    def click_on_edit_info_button(self):
        self.__info_section_elements.get_edit_info_button().click()

    def edit_first_name(self, first_name):
        self.__info_section_elements.get_first_name().set_text(first_name)

    def edit_last_name(self, last_name):
        self.__info_section_elements.get_last_name().set_text(last_name)

    def edit_email(self, email):
        self.__info_section_elements.get_email().set_text(email)

    def click_on_change_password_button(self):
        self.__info_section_elements.get_change_password().click()

    def wait_for_forgot_password_modal(self):
        self.__info_section_elements.get_forgot_password_modal_title().wait_to_appear()
        self.__info_section_elements.get_sign_in_link_on_forgot_password_modal().wait_to_appear()
        self.__info_section_elements.get_email_on_forgot_password_modal().wait_to_appear()

    def enter_email_on_forgot_password_modal(self, email):
        self.__info_section_elements.get_email_on_forgot_password_modal().set_text(email)

    def is_reset_password_email_validation_text_displayed(self):
        return self.__info_section_elements.get_reset_password_email_validation_text().displayed()

    def click_on_reset_password_button(self):
        self.__info_section_elements.get_reset_password_button().click()

    def is_reset_password_green_banner_text_displayed(self):
        return self.__info_section_elements.get_reset_password_green_banner_text().displayed()

    def click_on_green_banner_close_button(self):
        self.__info_section_elements.get_reset_password_green_banner_close_button().click()

    def click_on_close_forgot_password_modal(self):
        self.__info_section_elements.get_close_forgot_password_modal().click()

    def edit_phone_number(self, phone_number):
        self.__info_section_elements.get_phone().set_text(phone_number)

    def edit_phone_extension(self, phone_extension):
        self.__info_section_elements.get_phone_extension().set_text(phone_extension)

    def edit_dob_day(self, dob_day):
        self.__info_section_elements.get_dob_day().select_drop_drown_value(dob_day)

    def edit_dob_month(self, dob_month):
        self.__info_section_elements.get_dob_month().select_drop_drown_value(dob_month)

    def edit_dob_year(self, dob_year):
        self.__info_section_elements.get_dob_year().select_drop_drown_value(dob_year)

    def edit_size(self, size):
        self.__info_section_elements.get_size().select_drop_drown_value(size)

    def click_on_update_button(self):
        self.__info_section_elements.get_update_button().click()

    def click_on_cancel_button(self):
        self.__info_section_elements.get_cancel_button().click()

    def click_on_edit_password_button(self):
        self.__info_section_elements.get_edit_password_button().click()

    def enter_old_password(self, old_password):
        self.__info_section_elements.get_old_password().set_text(old_password)

    def enter_new_password(self, new_password):
        self.__info_section_elements.get_new_password().set_text(new_password)

    def reenter_new_password(self, new_password):
        self.__info_section_elements.get_confirm_password().set_text(new_password)

    def click_on_show_password(self):
        self.__info_section_elements.get_show_password().click()

    def edit_account(self):
        randomstring = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        fname = 'Fname'+randomstring
        lname = 'Lname'+randomstring
        self.__info_section_elements.get_edit_btn().get_visible_element()[0].click()
        self.__info_section_elements.get_first_name().wait_to_appear()
        self.__info_section_elements.get_first_name().set_text1(fname)
        self.__info_section_elements.get_last_name().set_text1(lname)
        alloptions = MyAccountPageInfoSectionElements().get_size().get_all_options()
        alloptions.remove(self.__info_section_elements.get_size().get_selected_option())
        self.edit_size(alloptions[-1])
        self.__info_section_elements.get_save_btn().wait_to_appear()
        self.__info_section_elements.get_save_btn().click()
        time.sleep(5)#it was needed in my machine
        assert (alloptions[-1] in self.__info_section_elements.get_size_p().get_text())
        assert ((fname+' '+lname) == self.__info_section_elements.get_fn_ln().get_text())

    def edit_account_cis_globo(self,data):
        randomstring = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        fname = 'Fname'+randomstring
        lname = 'Lname'+randomstring
        self.__info_section_elements.get_edit_btn().get_visible_element()[0].click()
        self.__info_section_elements.get_first_name().wait_to_appear()
        self.__info_section_elements.get_first_name().set_text1(fname)
        self.__info_section_elements.get_last_name().set_text1(lname)
        self.__info_section_elements.get_current_password().set_text(data.user_password)
        self.__info_section_elements.get_save_btn().wait_to_appear()
        self.__info_section_elements.get_save_btn().click()
        time.sleep(5)#it was needed in my machine
        assert ((fname+' '+lname) in self.__info_section_elements.get_fn_ln_cis().get_text())