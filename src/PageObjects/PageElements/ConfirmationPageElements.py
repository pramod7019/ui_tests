from ...Helpers.LocatorDatabase.Locators import Locators
from selenium.webdriver.common.by import By


class ConfirmationPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "ConfirmationPageLocators")

    def get_confirmation_heading(self):
        return self.get_page_element(By.XPATH, "confirmationHeading")

    def get_confirmation_sub_heading(self):
        return self.get_page_element(By.XPATH, "confirmationSubHeading")

    def get_aldo_learn_more_link(self):
        return self.get_page_element(By.XPATH, "aldoLearnMoreLink")

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

    def get_tax_code(self):
        return self.get_page_element(By.XPATH, "taxCode")

    def get_expand_taxes_button(self):
        return self.get_page_element(By.CLASS_NAME, "expandTaxesButton")

    def get_tax_amount(self):
        return self.get_page_element(By.XPATH, "taxAmount")

    def get_tax_item_amount(self):
        return self.get_page_element(By.XPATH, "taxItemAmount")

    def get_shipping_address(self):
        return self.get_page_element(By.XPATH, "shippingAddress")

    def get_shipping_method(self):
        return self.get_page_element(By.XPATH, "shippingMethod")

    def get_delivery_estimate_date(self):
        return self.get_page_element(By.XPATH, "deliveryEstimateDate")

    def get_payment_method(self):
        return self.get_page_element(By.XPATH, "paymentMethod")

    def get_card_expiration_date(self):
        return self.get_page_element(By.XPATH, "cardExpirationDate")

    def get_billing_address(self):
        return self.get_page_element(By.XPATH, "billingAddress")

    def get_delivery_location(self):
        return self.get_page_element(By.XPATH, "deliveryLocation")
