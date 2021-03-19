import re
import time
from _decimal import Decimal
from sqlite3 import Error

from ...PageObjects.PageElements.AllPageElements import AllPageElements


class PLPPage:

    def __init__(self):
        self.__plp_page_elements = AllPageElements.PLP_PAGE_ELEMENTS
        # self.__close_pdp_pop_up()

    def is_plp_open(self):
        plp_title = self.__plp_page_elements.get_plp_page()
        plp_title.wait_to_appear()
        assert plp_title.exists()

    def select_product_by_index(self, i):
        products = self.get_plp_products()
        if len(products) >i:
            products[i].click()
        else:
            raise AssertionError("products found on pdp {} but the selected index {}".format(len(products), i))

    def get_plp_products(self):
        return self.__plp_page_elements.get_plp_products().get_all_elements()

    def get_plp_products_names(self):
        return self.__plp_page_elements.get_product_names().get_text_of_child_elements()

    def get_plp_product_prices(self):
        return self.__plp_page_elements.get_product_prices().get_text_of_child_elements()

    def are_product_labels_displayed(self):
        product_labels = self.__plp_page_elements.get_product_labels()
        return self.__are_product_attributes_displayed_on_plp(product_labels)

    def are_product_tags_displayed(self):
        product_tags = self.__plp_page_elements.get_product_tags()
        return self.__are_product_attributes_displayed_on_plp(product_tags)

    @staticmethod
    def __are_product_attributes_displayed_on_plp(product_attributes):
        if product_attributes.exists():
            try:
                return product_attributes.child_elements_displayed()
            except Exception as error:
                raise error
        else:
            print("No {} were found on the plp page".format(product_attributes))
            return False

    def wait_for_plp_page(self):
        self.__plp_page_elements.get_item_count().wait_to_appear()
        self.__plp_page_elements.get_sort_drop_down().wait_to_appear()

    def __close_pdp_pop_up(self):
        pop_up = self.__plp_page_elements.get_pop_up_close_button()
        if pop_up.exists():
            pop_up.click()

    def click_open_filter_button(self):
        self.__plp_page_elements.get_filter_button().click()

    def get_no_of_filters_applied(self):
        return self.__plp_page_elements.get_filter_button().get_attribute("aria-label")

    def get_cis_landing_header_text(self):
        return self.__plp_page_elements.get_cis_landing_header().get_text()

    def get_applied_filters_text(self):
        applied_filters = self.__plp_page_elements.get_applied_filters().get_visible_element()
        applied_filters_text = []
        for filters in applied_filters:
            applied_filters_text.append(filters.text)
        return applied_filters_text

    def get_plp_final_product_prices(self):
        final_prices = []
        for price in self.get_plp_product_prices():
            if '\n' in price:
                sale_price = price.split('\n')[1]
                final_prices.append(Decimal(re.sub(r'[^\d.]', '', sale_price)))
            elif price == "Sold out":
                continue
            else:
                final_prices.append(Decimal(re.sub(r'[^\d.]', '', price)))
        return final_prices

    @staticmethod
    def lower_price_filter(price_range):
        lower_price = price_range.split('-')[0]
        return Decimal(re.sub(r'[^\d.]', '', lower_price))

    @staticmethod
    def upper_price_filter(price_range):
        upper_price = price_range.split('-')[1]
        return Decimal(re.sub(r'[^\d.]', '', upper_price))

    def check_if_product_prices_are_in_applied_filter_range(self, price_range):
        is_price_with_in_range = []
        for price in self.get_plp_final_product_prices():
            is_price_with_in_range.append(self.lower_price_filter(price_range) <= price <=
                                          self.upper_price_filter(price_range))
        return is_price_with_in_range

    def select_drop_down_value(self, sort_option):
        self.__plp_page_elements.get_sort_drop_down().select_drop_drown_value(sort_option)

    def check_if_product_prices_are_sorted_accordingly(self):
        product_prices = self.get_plp_final_product_prices()
        if len(product_prices) == 1:
            print("Only one product exists in the PLP")
        elif len(product_prices) >= 1:
            for i in range(len(product_prices) - 1):
                if not product_prices[i] <= product_prices[i+1]:
                    return Error("product prices are not sorted and earlier price:{} is > next price:{}"
                                .format(product_prices[i], product_prices[i+1]))
        return True

    def click_favourite_icon(self, idx):
        self.__plp_page_elements.get_favourites_btn_unselected().click_child_element(idx)

    def verify_if_pop_up_is_displayed(self):
        return self.__plp_page_elements.get_pop_up_close_button().displayed()

    def click_view_all_and_verify_product_count(self):
        load_more = self.__plp_page_elements.get_view_all_button()
        if load_more.exists():
            products_before = len(self.get_plp_products())
            load_more.click()
            self.__plp_page_elements.get_loading_button().wait_to_disappear()
            products_after = len(self.get_plp_products())
            return products_after > products_before
        else:
            return True
