from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class PLPPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "PLPPageLocators")

    def get_plp_page(self):
        return self.get_page_element(By.XPATH, "plpPage")

    def get_plp_products(self):
        return self.get_page_element(By.XPATH, "plpProducts")

    def get_view_all_button(self):
        return self.get_page_element(By.XPATH, "viewAllButton")

    def get_plp_page_header_title(self):
        return self.get_page_element(By.XPATH, "plpPageHeaderTitle")

    def get_plp_category_link_list(self):
        return self.get_page_element(By.XPATH, "plpCategoryLinkList")

    def get_bread_crumb_list(self):
        return self.get_page_element(By.XPATH, "breadcrumbList")

    def get_plp_product_count(self):
        return self.get_page_element(By.XPATH, "plpProductCount")

    def get_product_tags(self):
        return self.get_page_element(By.XPATH, "productTag")

    def get_favourites_button_unselected(self):
        return self.get_page_element(By.XPATH, "favouritesButtonUnSelected")

    def get_favourites_button_selected(self):
        return self.get_page_element(By.XPATH, "favouritesButtonSelected")

    def get_product_labels(self):
        return self.get_page_element(By.XPATH, "productLabels")

    def get_product_names(self):
        return self.get_page_element(By.XPATH, "productNames")

    def get_product_prices(self):
        return self.get_page_element(By.XPATH, "productPrices")

    def get_item_count(self):
        return self.get_page_element(By.XPATH, "itemCount")

    def get_sort_drop_down(self):
        return self.get_page_element(By.XPATH, "sortDropDown")

    def get_pop_up_close_button(self):
        return self.get_page_element(By.XPATH, "popupCloseButton")

    def get_filter_button(self):
        return self.get_page_element(By.XPATH, "filterButton")

    def get_applied_filters(self):
        return self.get_page_element(By.XPATH, "appliedFilters")

    def get_cis_landing_header(self):
        return self.get_page_element(By.XPATH, "cisLandingHeader")

    def get_favourites_btn_unselected(self):
        return self.get_page_element(By.XPATH, "favouritesBtnUnSelected")

    def get_fav_btn_non_aldo(self):
        return self.get_page_element(By.CSS_SELECTOR, "favnonAldo")

    def get_loading_button(self):
        return self.get_page_element(By.XPATH, "loadingButton")
