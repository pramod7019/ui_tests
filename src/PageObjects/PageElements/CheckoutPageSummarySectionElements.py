from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class CheckoutPageSummarySectionElements(Locators):

    def __init__(self):
        Locators.__init__(self, "CheckoutPageSummarySectionLocators")

    def get_header_title(self):
        return self.get_page_element(By.XPATH, "headerTitle")

    def get_cart_id(self):
        return self.get_page_element(By.XPATH, "cartId")

    def get_product_name(self):
        return self.get_page_element(By.XPATH, "productName")

    def get_product_thumbnail(self):
        return self.get_page_element(By.XPATH, "productThumbnail")

    def get_product_original_price(self):
        return self.get_page_element(By.XPATH, "productOriginalPrice")

    def get_product_sale_price(self):
        return self.get_page_element(By.XPATH, "productSalePrice")

    def get_product_final_price(self):
        return self.get_page_element(By.XPATH, "productFinalPrice")

    def get_product_colour(self):
        return self.get_page_element(By.XPATH, "productColour")

    def get_product_size(self):
        return self.get_page_element(By.XPATH, "productSize")

    def get_product_quantity(self):
        return self.get_page_element(By.XPATH, "productQuantity")

    def get_cart_sub_total(self):
        return self.get_page_element(By.XPATH, "cartSubTotal")

    def get_cart_total(self):
        return self.get_page_element(By.XPATH, "cartTotal")

    def get_enter_promo_button(self):
        return self.get_page_element(By.XPATH, "enterPromoButton")

    def get_enter_promo_field(self):
        return self.get_page_element(By.XPATH, "enterPromoField")

    def get_apply_button(self):
        return self.get_page_element(By.XPATH, "applyButton")

    def get_cancel_button(self):
        return self.get_page_element(By.CSS_SELECTOR, "cancelButton")

    def get_enter_postal_code_field(self):
        return self.get_page_element(By.XPATH, "enterPostalCodeField")

    def get_tax_code(self):
        return self.get_page_element(By.XPATH, "taxCode")

    def get_expand_taxes_button(self):
        return self.get_page_element(By.CLASS_NAME, "expandTaxesButton")

    def get_tax_amount(self):
        return self.get_page_element(By.XPATH, "taxAmount")

    def get_tax_item_amount(self):
        return self.get_page_element(By.XPATH, "taxItemAmount")

    def get_estimate_taxes_button(self):
        return self.get_page_element(By.XPATH, "estimateTaxesButton")

    def get_aldo_accordion_item(self):
        return self.get_page_element(By.XPATH, "aldoAccordionItem")

    def get_aldo_accordion_button(self):
        return self.get_page_element(By.XPATH, "aldoAccordionButton")

    def get_mobile_view_details_button(self):
        return self.get_page_element(By.XPATH, "mobileViewDetailsButton")

    def get_postal_code_div(self):
        return self.get_page_element(By.XPATH, "postalCodeDiv")

    def get_promocode_overlay(self):
        return self.get_page_element(By.XPATH, "promoCodeOverlayDiv")

    def get_promo_code_total_div_text(self):
        return self.get_page_element(By.XPATH, "promoDiv")

    def get_shipdiv_text(self):
        return self.get_page_element(By.XPATH, "shipDiv")

