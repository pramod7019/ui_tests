from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class FiltersPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "FiltersPageLocators")

    def get_size_filter_options(self):
        return self.get_page_element(By.XPATH, "sizeFilterOptions")

    def get_colour_filter_options(self):
        return self.get_page_element(By.XPATH, "colourFilterOptions")

    def get_price_filter_options(self):
        return self.get_page_element(By.XPATH, "priceFilterOptions")

    def get_apply_filter_button(self):
        return self.get_page_element(By.XPATH, "applyFilterButton")

    def get_clear_filters_button(self):
        return self.get_page_element(By.XPATH, "clearFiltersButton")

    def get_category_filter_options(self):
        return self.get_page_element(By.XPATH, "categoryFilterOptions")

    def get_close_filter_overlay_button(self):
        return self.get_page_element(By.XPATH, "closeFilterOverlayButton")

    def get_cis_sort_filter_options(self):
        return self.get_page_element(By.XPATH, "cisSortFilterOptions")

    def get_sort_drop_down(self):
        return self.get_page_element(By.XPATH, "sortDropDown")

    def get_no_of_filters_applied_text(self):
        return self.get_page_element(By.XPATH, "noOfFiltersAppliedText")

    def get_globo_no_of_filters_applied(self):
        return self.get_page_element(By.XPATH, "globoNoOfFiltersApplied")

    def get_more_price_filters_button(self):
        return self.get_page_element(By.XPATH, "morePriceFiltersButton")

    def get_more_colours_button(self):
        return self.get_page_element(By.XPATH, "moreColoursButton")

    def get_category_filters_group(self):
        return self.get_page_element(By.XPATH, "categoryFiltersGroup")

    def get_size_filters_group(self):
        return self.get_page_element(By.XPATH, "sizeFiltersGroup")

    def get_apply_filter_button_text(self):
        return self.get_page_element(By.XPATH, "applyFilterButtonText")

    def get_hide_button(self):
        return self.get_page_element(By.XPATH, "hideButton")
