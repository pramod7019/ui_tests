from ...Helpers.LocatorDatabase.Locators import Locators
from selenium.webdriver.common.by import By


class ShoppingBagPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "ShoppingBagPageLocators")

    def get_close_shopping_bag(self):
        return self.get_page_element(By.XPATH, "closeCartButton")

    def get_start_checkout_button(self):
        return self.get_page_element(By.XPATH, "startCheckoutButton")

    def get_header_title(self):
        return self.get_page_element(By.XPATH, "cartTitle")

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
        return self.get_page_element(By.CSS_SELECTOR, "enterPromoButton")

    def get_enter_promo_field(self):
        return self.get_page_element(By.CSS_SELECTOR, "enterPromoField")

    def get_apply_button(self):
        return self.get_page_element(By.CSS_SELECTOR, "applyButton")

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

    def get_edit_taxes_button(self):
        return self.get_page_element(By.XPATH, "editTaxesButton")

    def get_edit_button(self):
        return self.get_page_element(By.XPATH, "editButton")

    def get_remove_button(self):
        return self.get_page_element(By.XPATH, "removeButton")

    def get_move_to_favourites_button(self):
        return self.get_page_element(By.XPATH, "moveToFavouritesButton")

    def get_colour_options(self):
        return self.get_page_element(By.XPATH, "colourOptions")

    def get_available_size_options(self):
        return self.get_page_element(By.XPATH, "availableSizeOptions")

    def get_selected_size_option(self):
        return self.get_page_element(By.XPATH, "selectedSizeOption")

    def get_edit_quantity_drop_down(self):
        return self.get_page_element(By.XPATH, "editQuantityDropDown")

    def get_save_edits_button(self):
        return self.get_page_element(By.XPATH, "saveEditsButton")

    def get_cancel_edits_button(self):
        return self.get_page_element(By.XPATH, "cancelEditsButton")

    def get_paypal_checkout_button(self):
        return self.get_page_element(By.XPATH, "paypalCheckoutButton")

    def get_visa_checkout_button(self):
        return self.get_page_element(By.ID, "visaCheckoutButton")

    def get_selected_colour_label(self):
        return self.get_page_element(By.XPATH, "selectedColourLabel")

    def get_empty_shopping_title(self):
        return self.get_page_element(By.XPATH, "emptyShoppingBagTitle")

    def get_cart_discount_total(self):
        return self.get_page_element(By.CSS_SELECTOR, "cartDiscountPrice")

    def get_shipping_mode(self):
        return self.get_page_element(By.XPATH, "shippingMode")

    def get_shipping_description(self):
        return self.get_page_element(By.XPATH, "shippingDescription")

    def get_shipping_duration(self):
        return self.get_page_element(By.XPATH, "shippingDuration")

    def get_applied_promo_code(self):
        return self.get_page_element(By.XPATH, "appliedPromoCode")

    def get_remove_promo_button(self):
        return self.get_page_element(By.XPATH, "removePromo")
