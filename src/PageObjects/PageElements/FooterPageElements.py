from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class FooterPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "FooterPageLocators")

    def get_footer_link(self, text_to_replace):
        return self.get_page_element(By.XPATH, "footerLink", text_to_replace)

    def get_appointments(self):
        return self.get_page_element(By.XPATH, "appointments")

    def get_store_locators(self):
        return self.get_page_element(By.XPATH, "storeLocator")

    def get_gift_cards(self):
        return self.get_page_element(By.XPATH, "giftCards")

    def get_track_order(self):
        return self.get_page_element(By.ID, "trackOrder")

    def get_contactus(self):
        return self.get_page_element(By.XPATH, "contactUs")

    def get_return_policy(self):
        return self.get_page_element(By.ID, "returnPolicy")

    def get_help_center(self):
        return self.get_page_element(By.XPATH, "helpCenter")

    def get_about_us(self):
        return self.get_page_element(By.XPATH, "aboutUs")

    def get_careers(self):
        return self.get_page_element(By.XPATH, "careers")

    def get_aldo_group(self):
        return self.get_page_element(By.XPATH, "group")

    def get_kindaf(self):
        return self.get_page_element(By.XPATH, "kindaf")

    def get_responsibility(self):
        return self.get_page_element(By.XPATH, "responsibility")

    def get_shipping(self):
        return self.get_page_element(By.XPATH, "shipping")

    def get_pop_up_close_button(self):
        return self.get_page_element(By.XPATH, "popUp")

    def get_all_countries_link(self):
        return self.get_page_element(By.XPATH, "allCountriesLink")

    def get_north_america_link(self):
        return self.get_page_element(By.XPATH, "northAmericaLink")

    def get_usa_link(self):
        return self.get_page_element(By.XPATH, "usaLink")

    def get_find_stores(self):
        return self.get_page_element(By.CSS_SELECTOR, "findstores")

    def get_stores(self):
        return self.get_page_element(By.CSS_SELECTOR, "stores")

    def get_map(self):
        return self.get_page_element(By.CSS_SELECTOR, "map")

