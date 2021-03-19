from ..PageElements.CheckoutPageReviewSectionElements import CheckoutPageReviewSectionElements


class CheckoutReviewPage:

    def __init__(self):
        self.__checkout_review_page = CheckoutPageReviewSectionElements()
        self.__wait_for_review_section()

    def __wait_for_review_section(self):
        self.__checkout_review_page.get_cart_id().wait_to_appear()
        self.__checkout_review_page.get_place_order_button().wait_to_appear()
        self.__checkout_review_page.get_cart_total().wait_to_appear()

    def click_on_place_order(self, checkout_type):
        place_order_button = self.__checkout_review_page.get_place_order_button()
        place_order_button.click()
        if "paypal" in checkout_type.lower():
            try:
                place_order_button.wait_to_disappear()
            except AssertionError:
                pass
        else:
            place_order_button.wait_to_disappear()

    def get_product_names(self):
        return self.__checkout_review_page.get_product_name().get_text_of_child_elements()

    def is_product_name_displayed(self):
        return self.__checkout_review_page.get_product_name().is_child_element_displayed()

    def get_sub_total(self):
        return self.__checkout_review_page.get_cart_sub_total().get_text()

    def is_sub_total_displayed(self):
        return self.__checkout_review_page.get_cart_sub_total().displayed()

    def get_total(self):
        return self.__checkout_review_page.get_cart_total().get_text()

    def is_total_displayed(self):
        return self.__checkout_review_page.get_cart_total().displayed()

    def get_product_colour(self):
        return self.__checkout_review_page.get_product_colour().get_attribute_of_child_elements("title")

    def is_product_colour_displayed(self):
        return self.__checkout_review_page.get_product_colour().is_child_element_displayed()

    def get_product_size(self):
        return self.__checkout_review_page.get_product_size().get_text_of_child_elements()

    def is_product_size_displayed(self):
        return self.__checkout_review_page.get_product_size().is_child_element_displayed()

    def get_product_quantity(self):
        return self.__checkout_review_page.get_product_quantity().get_text_of_child_elements()

    def is_product_quantity_displayed(self):
        return self.__checkout_review_page.get_product_quantity().is_child_element_displayed()

    def get_product_final_price(self):
        return self.__checkout_review_page.get_product_final_price().get_text_of_child_elements()

    def is_product_final_price_displayed(self):
        return self.__checkout_review_page.get_product_final_price().is_child_element_displayed()

    def get_product_original_price(self):
        return self.__checkout_review_page.get_product_original_price().get_text_of_child_elements()

    def is_product_original_price_displayed(self):
        return self.__checkout_review_page.get_product_original_price().is_child_element_displayed()

    def get_tax_amount(self):
        return self.__checkout_review_page.get_tax_amount().get_text()

    def is_tax_amount_displayed(self):
        return self.__checkout_review_page.get_tax_amount().displayed()

    def click_expand_taxes(self):
        return self.__checkout_review_page.get_expand_taxes_button().click()

    def is_tax_items_displayed(self):
        return self.__checkout_review_page.get_tax_item_amount().is_child_element_displayed()

    def get_total_currency_code(self):
        return self.__checkout_review_page.get_total_currency_code().get_text()

    def click_promo_code(self):
        self.__checkout_review_page.get_enter_promo_button().click()

    def enter_promo_code(self, promo_code):
        self.__checkout_review_page.get_enter_promo_field().set_text(promo_code)

    def click_apply_promo(self):
        self.__checkout_review_page.get_apply_button().click()

    def click_cancel_promo(self):
        self.__checkout_review_page.get_cancel_button().click()

