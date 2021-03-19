from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class FavPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "FavPageLocators")

    def get_primary_add_cart(self):
        return self.get_page_element(By.XPATH, "primaryAddToCart")

    def get_secondary_add_cart(self):
        return self.get_page_element(By.XPATH, "secondaryAddToCart")

    def get_size(self):
        return self.get_page_element(By.XPATH, "size")

    def get_remove(self):
        return self.get_page_element(By.XPATH, "remove")

    def get_fav_empty(self):
        return self.get_page_element(By.XPATH, "emptyFav")

    def get_product_thumbnail(self):
        return self.get_page_element(By.XPATH, "productThumbnail")

    def get_pop_up_close_button(self):
        return self.get_page_element(By.XPATH, "popupCloseButton")

