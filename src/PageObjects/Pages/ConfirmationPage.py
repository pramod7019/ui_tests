import re
from ..PageElements.ConfirmationPageElements import ConfirmationPageElements


class ConfirmationPage:

    def __init__(self):
        self.__confirmation_page_elements = ConfirmationPageElements()
        self.__wait_for_confirmation_page()

    def __wait_for_confirmation_page(self):
        self.__confirmation_page_elements.get_confirmation_heading().wait_to_appear()
        self.__confirmation_page_elements.get_confirmation_sub_heading().wait_to_appear()
        self.__confirmation_page_elements.get_cart_id().wait_to_appear()

    def verify_confirmation_heading(self):
        return self.__confirmation_page_elements.get_confirmation_heading().displayed()

    def get_confirmation_subheading(self):
        return self.__confirmation_page_elements.get_confirmation_sub_heading().get_text()

    def get_order_number(self):
        subheading_numbers_list = [int(s) for s in re.findall(r'\b\d+\b', self.get_confirmation_subheading())]
        return max(subheading_numbers_list)

    def is_cart_id_displayed(self):
        return self.__confirmation_page_elements.get_cart_id().displayed()

    def get_shipping_address(self):
        return self.__confirmation_page_elements.get_shipping_address().get_text()

    def get_shipping_method(self):
        return self.__confirmation_page_elements.get_shipping_method().get_text()

    def get_payment_method(self):
        return self.__confirmation_page_elements.get_payment_method().get_text()

    def get_billing_address(self):
        return self.__confirmation_page_elements.get_billing_address().get_text()

    def get_card_expiration_date(self):
        return self.__confirmation_page_elements.get_card_expiration_date().get_text()

    def get_cart_total(self):
        return self.__confirmation_page_elements.get_cart_total().get_text()

    def is_sub_total_displayed(self):
        return self.__confirmation_page_elements.get_cart_sub_total().displayed()

    def is_tax_amount_displayed(self):
        return self.__confirmation_page_elements.get_tax_amount().displayed()

    def is_product_image_displayed(self):
        product_images = self.__confirmation_page_elements.get_product_thumbnail().get_all_elements()
        for image in product_images:
          if not image.is_displayed():
            raise AssertionError("product images are not displayed")

    def are_product_names_displayed(self):
        return self.__confirmation_page_elements.get_product_name().child_elements_displayed()

    def are_product_final_prices_displayed(self):
        return self.__confirmation_page_elements.get_product_final_price().child_elements_displayed()

    def are_product_original_prices_displayed(self):
        return self.__confirmation_page_elements.get_product_original_price().child_elements_displayed()

    def are_product_quantities_displayed(self):
        return self.__confirmation_page_elements.get_product_quantity().child_elements_displayed()

    def are_product_sizes_displayed(self):
        return self.__confirmation_page_elements.get_product_size().child_elements_displayed()

    def are_product_colours_displayed(self):
        return self.__confirmation_page_elements.get_product_colour().child_elements_displayed()

    def click_aldo_learn_more(self):
        return self.__confirmation_page_elements.get_aldo_learn_more_link().click()






