import re
from ...PageObjects.PageElements.AllPageElements import ShoppingBagPageElements
import time
from selenium.common.exceptions import ElementNotInteractableException


class CartPage:

    def __init__(self):
        self.__cart_page_elements = ShoppingBagPageElements()
        self.__wait_for_cart_page()

    def click_on_start_checkout(self):
        time.sleep(5)
        self.__cart_page_elements.get_start_checkout_button().click()

    def close_cart_page(self):
        self.__cart_page_elements.get_close_shopping_bag().click()

    def click_on_cancel_edits(self):
        self.__cart_page_elements.get_cancel_edits_button().click()

    def click_on_save_edits(self):
        save_edit_button = self.__cart_page_elements.get_save_edits_button()
        if not save_edit_button.exists():
            self.select_product_size(0)
        save_edit_button.click()
        self.__cart_page_elements.get_available_size_options().wait_to_disappear()

    def click_on_edit_product(self, index):
        for i in range(0, 4):
            while self.__cart_page_elements.get_product_size().exists():
                try:
                    self.__cart_page_elements.get_edit_button().click_child_element(index)
                except:
                    continue
                break

    def click_on_move_to_favourites(self):
        self.__cart_page_elements.get_move_to_favourites_button().click()

    def click_on_cancel_button(self):
        self.__cart_page_elements.get_cancel_button().click()

    def click_on_cancel_edit_product_button(self, index):
        self.__cart_page_elements.get_cancel_edits_button().click_child_element(index)

    def select_product_quantity(self, value):
        self.__cart_page_elements.get_edit_quantity_drop_down().select_drop_drown_value(value)

    def select_product_size(self, index):
        sizes = self.__cart_page_elements.get_available_size_options()
        edited_size = sizes.get_text_of_child_elements()[index]
        sizes.click_child_element(index)
        return edited_size

    def select_product_colour(self, index):
        colours = self.__cart_page_elements.get_colour_options()
        edited_colour = colours.get_attribute_of_child_elements("title")[index]
        colours.click_child_element(index)
        start = time.time()
        while (time.time() - start) < 5:
            if edited_colour == self.get_displayed_colour_in_edit():
                break
        return edited_colour

    def select_shipping_method(self, shipping_method):
        shipping = 0 if shipping_method == "Standard" else 1
        for k in range(0, 2):
            shipping_elements = self.__cart_page_elements.get_shipping_mode().get_all_elements()
            if not shipping_elements[shipping].is_selected():
                self.__click_shipping_method(shipping)

    def __click_shipping_method(self, i):
        try:
            self.__cart_page_elements.get_shipping_mode().click_child_element(i)
        except:
            self.wait_for_shipping_method_details()
            self.__cart_page_elements.get_shipping_mode().click_child_element(i)
        self.__wait_for_shipping_method_details(i)

    def __wait_for_shipping_method_details(self, i):
        self.__cart_page_elements.get_shipping_description().wait_to_appear()
        self.__cart_page_elements.get_shipping_duration().wait_to_appear()
        self.__cart_page_elements.get_cart_sub_total().wait_to_appear()
        self.__cart_page_elements.get_paypal_checkout_button().wait_to_appear() if i == 0 else \
            self.__cart_page_elements.get_paypal_checkout_button().wait_to_disappear()


    def get_displayed_colour_in_edit(self):
        return self.__cart_page_elements.get_selected_colour_label().get_text()

    def get_displayed_size(self):
        return self.__cart_page_elements.get_product_size().get_text()

    def __wait_for_cart_page(self):
        self.__cart_page_elements.get_close_shopping_bag().wait_to_appear()
        self.__cart_page_elements.get_header_title().wait_to_appear()
        # self.__cart_page_elements.get_cart_id().wait_to_appear()
        # self.__cart_page_elements.get_product_thumbnail().displayed()

    def remove_product_from_cart(self, i):
        remove_buttons = self.__cart_page_elements.get_remove_button()
        if remove_buttons.exists():
            for k in range(0, 25):
                try:
                    remove_buttons.get_all_elements()[i].click()
                except ElementNotInteractableException:
                   pass
                else:
                  break
        else:
            raise AssertionError("products does not exist in the cart")

    def is_empty_cart_title_displayed(self):
        return self.__cart_page_elements.get_empty_shopping_title().displayed()

    def get_product_names(self):
        return self.__cart_page_elements.get_product_name().get_text_of_child_elements()

    def get_product_sizes(self):
        return self.__cart_page_elements.get_product_size().get_text_of_child_elements()

    def get_product_quantities(self):
        return self.__cart_page_elements.get_product_quantity().get_text_of_child_elements()

    def get_product_final_prices(self):
        return self.__cart_page_elements.get_product_final_price().get_text_of_child_elements()

    def get_product_original_prices(self):
        return self.__cart_page_elements.get_product_original_price().get_text_of_child_elements()

    def get_product_sale_prices(self):
        return self.__cart_page_elements.get_product_sale_price().get_text_of_child_elements()

    def get_total_tax_amount(self):
        tax = self.__cart_page_elements.get_tax_amount().get_text()
        return float(self.remove_chars_from_given_string(tax))

    def get_cart_sub_total_value(self):
        time.sleep(5)
        total = self.__cart_page_elements.get_cart_sub_total().get_text()
        return float(self.remove_chars_from_given_string(total))

    def is_cart_total_value_displayed(self):
        return self.__cart_page_elements.get_cart_total().displayed()

    def is_cart_id_displayed(self):
        return self.__cart_page_elements.get_cart_id().displayed()

    def click_enter_promo_code(self):
        self.__cart_page_elements.get_enter_promo_button().click()

    def enter_promo_code(self, promo_code):
        self.__cart_page_elements.get_enter_promo_field().set_text(promo_code)

    def click_on_apply(self):
        self.__cart_page_elements.get_apply_button().click()

    def click_on_estimate_taxes(self):
        self.__cart_page_elements.get_edit_taxes_button().click()

    def enter_postal_code(self, postal_code):
        self.__cart_page_elements.get_enter_postal_code_field().set_text(postal_code)

    def click_on_expand_taxes(self):
        self.__cart_page_elements.get_expand_taxes_button().click()

    def get_tax_item_amounts(self):
        self.__cart_page_elements.get_tax_item_amount().get_text_of_child_elements()

    def get_title_text(self):
        return self.__cart_page_elements.get_header_title().get_text()

    def is_cart_title_displayed(self):
        return self.__cart_page_elements.get_header_title().displayed()

    def get_displayed_product_colour_in_cart(self):
        return self.__cart_page_elements.get_product_colour().get_text()

    def get_cart_total_value(self):
        total = self.__cart_page_elements.get_cart_total().get_text()
        return float(self.remove_chars_from_given_string(total))

    def get_cart_discount_total(self):
        total = self.__cart_page_elements.get_cart_discount_total().get_text()
        return float(self.remove_chars_from_given_string(total))

    def apply_promo(self, promo_code):
        self.__cart_page_elements.get_enter_promo_button().click()
        self.__cart_page_elements.get_enter_promo_field().set_text(promo_code)
        self.__cart_page_elements.get_apply_button().click()

    def remove_chars_from_given_string(self, str):
        return re.sub("\$", '', str)

    def get_applied_promo_code_text(self):
        promo_code = self.__cart_page_elements.get_applied_promo_code()
        if promo_code.exists:
            return promo_code.get_text()

    def remove_any_applied_promos(self):
        if self.__cart_page_elements.get_remove_promo_button().exists():
            self.__cart_page_elements.get_remove_promo_button().click()









