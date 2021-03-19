from ...Helpers.LocatorDatabase.Locators import Locators
from selenium.webdriver.common.by import By


class MyAccountPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "MyAccountPageLocators")

    def get_sign_out_button(self):
        return self.get_page_element(By.XPATH, "signOutButton")

    def get_over_view_link(self):
        return self.get_page_element(By.XPATH, "overViewLink")

    def get_page_heading(self):
        return self.get_page_element(By.XPATH, "pageHeading")

    def get_coupon_code(self):
        return self.get_page_element(By.XPATH, "coupon")

    def get_promo_link(self):
        return self.get_page_element(By.XPATH, "showPromoCode")

    def get_redeem_offer_button(self):
        return self.get_page_element(By.XPATH, "redeemOfferButton")

    def get_my_info_link(self):
        return self.get_page_element(By.XPATH, "myInfoLink")

    def get_payment_link(self):
        return self.get_page_element(By.XPATH, "paymentLink")

