from ..PageElements.SignInPageElements import SignInPageElements


class SignInPage:

    def __init__(self):
        self.__sign_in_page_elements = SignInPageElements()
        self.__wait_for_sign_in_page()

    def enter_user_name(self, user_name):
        print("[SignInPage]: Entering username,  {}".format(user_name))
        self.__sign_in_page_elements.get_user_name_field().set_text(user_name)

    def enter_password(self, pwd):
        print("[SignInPage]: Entering password,  {}".format(pwd))
        self.__sign_in_page_elements.get_password_field().set_text(pwd)

    def click_on_sign_in_button(self):
        self.__sign_in_page_elements.get_sign_in_button().click()

    def wait_for_sign_page_to_disappear(self):
        self.__sign_in_page_elements.get_page_title_text().wait_to_disappear()

    def is_invalid_error_message_displayed(self):
        return self.__sign_in_page_elements.get_sign_in_error_text().displayed()

    def __wait_for_sign_in_page(self):
        self.__sign_in_page_elements.get_page_title_text().wait_to_appear()
        self.__sign_in_page_elements.get_user_name_field().wait_to_appear()
        self.__sign_in_page_elements.get_password_field().wait_to_appear()

    def click_on_register(self):
        self.__sign_in_page_elements.get_register_button().click()

    def click_on_sign_in_with_fb(self):
        self.__sign_in_page_elements.get_sign_in_with_facebook_button().click()

    def click_on_forgot_password(self):
        self.__sign_in_page_elements.get_forgot_password_button().click()

    def is_show_password_button_displayed(self):
        return self.__sign_in_page_elements.get_show_password_button().displayed()

    def is_user_name_validation_displayed(self):
        return self.__sign_in_page_elements.get_user_name_error_validation_text().displayed()

    def is_password_validation_displayed(self):
        return self.__sign_in_page_elements.get_password_error_validation_text().displayed()

    def close_sign_in_overlay(self):
        self.__sign_in_page_elements.get_sign_in_overlay_close_button().click()
