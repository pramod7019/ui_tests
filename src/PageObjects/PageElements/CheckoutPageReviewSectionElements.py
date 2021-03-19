from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class CheckoutPageReviewSectionElements(Locators):

    def __init__(self):
        Locators.__init__(self, "CheckoutPageReviewSectionLocators")

    def get_review_sub_title(self):
        return self.get_page_element(By.XPATH, "reviewSubTitle")

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

    def get_product_colour(self):
        return self.get_page_element(By.XPATH, "productColour")

    def get_product_size(self):
        return self.get_page_element(By.XPATH, "productSize")

    def get_product_quantity(self):
        return self.get_page_element(By.XPATH, "productQuantity")

    def get_product_final_price(self):
        return self.get_page_element(By.XPATH, "productFinalPrice")

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
        return self.get_page_element(By.XPATH, "cancelButton")

    def get_tax_code(self):
        return self.get_page_element(By.XPATH, "taxCode")

    def get_expand_taxes_button(self):
        return self.get_page_element(By.XPATH, "expandTaxesButton")

    def get_tax_amount(self):
        return self.get_page_element(By.XPATH, "taxAmount")

    def get_tax_item_amount(self):
        return self.get_page_element(By.XPATH, "taxItemAmount")

    def get_save_information_checkbox(self):
        return self.get_page_element(By.XPATH, "saveInformationCheckBox")

    def get_password_field(self):
        return self.get_page_element(By.XPATH, "passwordField")

    def get_aldo_crew_postal_code_field(self):
        return self.get_page_element(By.XPATH, "aldoCrewPostalCodeField")

    def get_aldo_crew_female_radio_button(self):
        return self.get_page_element(By.XPATH, "aldoCrewFemaleRadioButton")

    def get_aldo_crew_male_radio_button(self):
        return self.get_page_element(By.XPATH, "aldoCrewMaleRadioButton")

    def get_password_show_button(self):
        return self.get_page_element(By.XPATH, "passwordShowButton")

    def get_create_account_form(self):
        return self.get_page_element(By.XPATH, "createAccountForm")

    def get_place_order_button(self):
        return self.get_page_element(By.XPATH, "placeOrderButton")

    def get_total_currency_code(self):
        return self.get_page_element(By.XPATH, "totalCurrencyCode")
