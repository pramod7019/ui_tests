
from operator import index

from selenium.common.exceptions import StaleElementReferenceException
from ..PageElements.FiltersPageElements import FiltersPageElements


class FilterPage():

    def __init__(self):
        self.__filter_page_elements = FiltersPageElements()
        self.__wait_for_filters_page()

    def __wait_for_filters_page(self):
        self.__filter_page_elements.get_size_filters_group().wait_to_appear()

    def click_apply_filters_button(self):
        self.__filter_page_elements.get_apply_filter_button().click()

    def click_clear_filters_button(self):
        self.__filter_page_elements.get_clear_filters_button().click()

    def select_size_filter(self, size):
        size_options = self.__filter_page_elements.get_size_filter_options()
        size_options.click_child_element_for_condition("aria-label", size)

    def select_colour_filter(self, colour):
        colour_options = self.__filter_page_elements.get_colour_filter_options()
        colour_options.click_child_element_for_condition("aria-label", colour)

    @staticmethod
    def __select_filter_option(filter_options, given_option, attribute):
        try:
            for option in filter_options:
                filter_option = option.get_attribute(attribute)
                if filter_option == given_option:
                    option.click()
        except StaleElementReferenceException:
            pass

    def select_price_filter(self, price_range):
        price_options = self.__filter_page_elements.get_price_filter_options()
        price_options.click_child_element_for_condition("title", price_range)

    def select_cis_sort_option(self, sort_option):
        sort_options = self.__filter_page_elements.get_cis_sort_filter_options()
        sort_options.click_child_element_for_condition("title", sort_option)

    def get_apply_filter_button_text(self):
        return self.__filter_page_elements.get_apply_filter_button_text().get_text()

    def click_close_filters_overlay(self):
        self.__filter_page_elements.get_close_filter_overlay_button().click()

    def click_more_colours_button(self):
        self.__filter_page_elements.get_more_colours_button().click()

    def get_no_of_colour_options(self):
        return len(self.__filter_page_elements.get_colour_filter_options().get_visible_element())

    def click_hide_button(self):
        self.__filter_page_elements.get_hide_button().click()





