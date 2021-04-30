from uitests.src.Helpers.Browser import Browser
from ...PageObjects.PageElements.OrderHistoryPageElements import OrderHistoryPageElements
import time
import re


class OrderHistoryPage:

    def __init__(self):
        self.__order_history_elements = OrderHistoryPageElements()

    def fill_order_number(self, order_number):
        self.__order_history_elements.get_order_number_input_label().set_text(order_number)

    def fill_postal_code(self, postal_code):
        self.__order_history_elements.get_postal_code_input_label().set_text(postal_code)

    def click_track_order(self, track_order):
        self.__order_history_elements.get_track_order().click()

    def click_tool_tip(self, tool_tip):
        self.__order_history_elements.get_order_number_tooltip().click()

    def click_return_here(self, click_here):
        self.__order_history_elements.get_return_click_here().click()

    def click_view_order_details(self):
        self.__order_history_elements.get_view_order_details().click()
        assert self.__order_history_elements.get_order_details().displayed()

    def click_load_more(self):
        self.__order_history_elements.get_order_load_more().click()

    def click_my_history(self):
        self.__order_history_elements.get_my_history().click(wait_for_clickable=False)

    def get_order_number(self):
        order_number_text = self.__order_history_elements.get_order_number().get_text()
        order_number = re.findall(r'\d+', order_number_text)
        return order_number[0]

    def verify_order_detail(self):
        return self.__order_history_elements.get_order_details().displayed()

    def get_order_number_element(self):
        return self.__order_history_elements.get_order_number_input_label()

    def get_orderscount(self):
        return len(self.__order_history_elements.get_orders().get_all_elements())

    def order_detail_find_url(self, url):
        assert Browser.get_current_url().find(url)

    def click_view_orders(self):
        self.__order_history_elements.get_view_orders().click(wait_for_clickable=False)

    def click_my_info(self):
        self.__order_history_elements.get_my_info().click(wait_for_clickable=False)


