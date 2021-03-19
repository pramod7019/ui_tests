import re
import time

from uitests.src.PageObjects.PageElements.CheckoutPageSummarySectionElements import CheckoutPageSummarySectionElements


class CheckoutSummaryPage:

    def __init__(self):
        self.__summary_page = CheckoutPageSummarySectionElements()

    def apply_Taxes(self, postal_code):
        self.__summary_page.get_estimate_taxes_button().click()
        self.__summary_page.get_postal_code_div().click()
        self.__summary_page.get_enter_postal_code_field().set_text(postal_code)
        self.__summary_page.get_apply_button().click()
        time.sleep(5)

    def apply_promo(self, promo_code):
        self.__summary_page.get_enter_promo_button().click()
        self.__summary_page.get_promocode_overlay().click()
        self.__summary_page.get_enter_promo_field().set_text(promo_code)
        self.__summary_page.get_apply_button().click()
        time.sleep(5)

    def get_total_tax_amount(self):
        tax = self.__summary_page.get_tax_amount().get_text()
        return float(self.remove_chars_from_given_string(tax))

    def get_total_cart_amount(self):
        cart_total = self.__summary_page.get_cart_total().get_text()
        return float(self.remove_chars_from_given_string(cart_total))

    def get_subtotal_checkout_amount(self):
        cart_sub_total = self.__summary_page.get_cart_sub_total().get_text()
        return float(self.remove_chars_from_given_string(cart_sub_total))

    def get_promo_checkout_amount(self):
        promo_total = self.__summary_page.get_promo_code_total_div_text().get_text()
        return float(self.remove_chars_from_given_string(promo_total))

    def get_ship_checkout_amount(self):
        shipping_amount = self.__summary_page.get_shipdiv_text().get_text()
        return float(self.remove_chars_from_given_string(shipping_amount))

    def remove_chars_from_given_string(self, str):
        return re.sub("\$", '', str)
