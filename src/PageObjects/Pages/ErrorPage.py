
from uitests.src.PageObjects.PageElements.ErrorPageElements import ErrorPageElements
import time


class ErrorPage:

    def __init__(self):
        self.__error_page_elements = ErrorPageElements()

    def click_on_close_button(self):
        self.__error_page_elements.get_close_button().click()

    def get_modal_title(self):
        return self.__error_page_elements.get_error_modal_title()

    def get_error_message(self):
        return self.__error_page_elements.get_error_message()

    def get_error_code(self):
        return self.__error_page_elements.get_error_code()

    def click_on_let_us_chat_button(self):
        self.__error_page_elements.get_chat_button().click()

    def click_on_continue_button(self):
        self.__error_page_elements.get_continue_button().click()
