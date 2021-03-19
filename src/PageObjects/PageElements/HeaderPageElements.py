from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class HeaderPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "HeaderPageLocators")

    def get_my_account_button(self):
        return self.get_page_element(By.XPATH, "myAccountButton")

    def get_search_button(self):
        return self.get_page_element(By.XPATH, "searchButton")

    def get_favourites_icon(self):
        return self.get_page_element(By.XPATH, "favouritesIcon")

    def get_favourites_label(self):
        return self.get_page_element(By.XPATH, "favouritesLabel")

    def get_cart_button(self):
        return self.get_page_element(By.XPATH, "cartButton")

    def get_cart_item_label(self):
        return self.get_page_element(By.XPATH, "cartItemLabel")

    def get_country_drop_down(self):
        return self.get_page_element(By.XPATH, "countryDropDown")

    def get_language_link(self):
        return self.get_page_element(By.XPATH, "languageLink")

    def get_learn_more_link(self):
        return self.get_page_element(By.XPATH, "learnMoreLink")

    def get_promo_banner(self):
        return self.get_page_element(By.ID, "promoBanner")

    def get_promo_banner_close_button(self):
        return self.get_page_element(By.XPATH, "promoBannerCloseButton")

    def get_user_account_button(self):
        return self.get_page_element(By.XPATH, "userAccountButton")

    def get_header_nav_categories(self):
        return self.get_page_element(By.XPATH, "navigationCategories")

    def get_home_page_nav_for(self, category):
        nav_locator = (self.get_locator_for_page_element("navigationByCategory")).format(category, category)
        return self.get_ui_element(By.XPATH, nav_locator)

    def get_main_nav_button_mobile(self):
        return self.get_page_element(By.XPATH, "mobileMainNav")

    def get_mobile_my_account_button(self):
        return self.get_page_element(By.XPATH, "mobileMyAccountButton")

    def get_globo_store_locator_button(self):
        return self.get_page_element(By.XPATH, "globoStoreLocatorButton")

    def get_globo_rewards_button(self):
        return self.get_page_element(By.XPATH, "globoRewardsButton")

    def get_globo_track_order_button(self):
        return self.get_page_element(By.XPATH, "globoTrackOrderButton")

    def get_search_field(self):
        return self.get_page_element(By.XPATH, "searchField")

    def get_search_suggestion(self):
        return self.get_page_element(By.XPATH, "searchSuggestion")

    def get_promotional_message(self):
        return self.get_page_element(By.XPATH, "promotionalMessage")

    def get_header_message(self):
        return self.get_page_element(By.XPATH, "headerMessage")

    def get_wish_list_items_label(self):
        return self.get_page_element(By.XPATH, "wishListItemsLabel")

    def get_mobile_menu_category(self, category):
        nav_locator = (self.get_locator_for_page_element("mobileMenuCategory")).format(category, category)
        return self.get_ui_element(By.XPATH, nav_locator)

    def get_menu_category_level1(self, category_level1):
        nav_locator = (self.get_locator_for_page_element("mobileMenuLevel1")).format(category_level1)
        return self.get_ui_element(By.XPATH, nav_locator)

    def get_menu_category_level2(self, category_level2):
        nav_locator = (self.get_locator_for_page_element("mobileMenuLevel2")).format(category_level2)
        return self.get_ui_element(By.XPATH, nav_locator)

    def main_nav_button_mobile(self):
        return self.get_page_element(By.XPATH, "mobileMainNav")

    def get_mobile_search_field(self):
        return self.get_page_element(By.XPATH, "mobileSearchField")

    def get_mobile_favourites_icon(self):
        return self.get_page_element(By.XPATH, "mobileFavouritesIcon")

    def get_mobile_cart_button(self):
        return self.get_page_element(By.XPATH, "mobileCartButton")

    def get_mobile_user_account_button(self):
        return self.get_page_element(By.XPATH, "mobileUserAccountButton")

    def get_mobile_language_link(self):
        return self.get_page_element(By.XPATH, "mobileLanguageLink")

