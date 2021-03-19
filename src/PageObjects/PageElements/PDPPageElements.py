from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class PDPPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "PDPPageLocators")

    def get_pdp_sizes(self):
        return self.get_page_element(By.XPATH, "sizes")

    def get_pdp_selected_size_label(self):
        return self.get_page_element(By.XPATH, "sizeSelectedLabel")

    def get_pdp_add_to_bag_button(self):
        return self.get_page_element(By.XPATH, "addToBagButton")

    def get_pdp_select_size_warning_button(self):
        return self.get_page_element(By.XPATH, "selectSizeWarningButton")

    def get_pdp_product_name(self):
        return self.get_page_element(By.XPATH, "productName")

    def get_pdp_colours_radio_buttons(self):
        return self.get_page_element(By.XPATH, "colourSwatches")

    def get_pdp_selected_colour_label(self):
        return self.get_page_element(By.XPATH, "colourSelectedLabel")

    def get_pdp_price_block(self):
        return self.get_page_element(By.XPATH, "priceBlock")

    def get_pdp_reassurance_links(self):
        return self.get_page_element(By.XPATH, "reassuranceLinks")

    def get_size_chart_button(self):
        return self.get_page_element(By.XPATH, "sizeChartButton")

    def get_globo_find_in_store_button(self):
        return self.get_page_element(By.XPATH, "globoFindInStoreButton")

    def get_bread_crumb_links(self):
        return self.get_page_element(By.XPATH, "breadCrumbLinks")

    def get_favourites_button_un_selected(self):
        return self.get_page_element(By.XPATH, "favouritesButtonUnSelected")

    def get_favourites_button_selected(self):
        return self.get_page_element(By.XPATH, "favouritesButtonUnSelected")

    def get_product_carousel_images(self):
        return self.get_page_element(By.XPATH, "productCarouselImages")

    def get_zoom_button(self):
        return self.get_page_element(By.XPATH, "zoomButton")

    def get_image_close_button(self):
        return self.get_page_element(By.XPATH, "imageCloseButton")

    def get_image_full_screen_button(self):
        return self.get_page_element(By.XPATH, "imageFullScreenButton")

    def get_next_image_arrow_button(self):
        return self.get_page_element(By.XPATH, "nextImageArrowButton")

    def get_previous_image_arrow_button(self):
        return self.get_page_element(By.XPATH, "previousImageArrowButton")

    def get_product_info_panel(self):
        return self.get_page_element(By.XPATH, "productInfo")

    def get_globo_accordian_icon(self):
        return self.get_page_element(By.XPATH, "globoAccordianIcon")

    def get_size_chart_overlay_box(self):
        return self.get_page_element(By.XPATH, "sizeChartOverLayBox")

    def get_size_chart_overlay_close_button(self):
        return self.get_page_element(By.XPATH, "sizeChartOverLayCloseButton")

    def get_pop_up_close_button(self):
        return self.get_page_element(By.XPATH, "popupCloseButton")

    def get_men_women_tabs(self):
        return self.get_page_element(By.XPATH, "menwomentabs")

    def get_location(self):
        return self.get_page_element(By.XPATH, "location")

    def get_store_results(self):
        return self.get_page_element(By.XPATH, "storeresults")

    def get_map(self):
        return self.get_page_element(By.XPATH, "cmap")

    def get_out_stock(self):
        return self.get_page_element(By.XPATH, "outstock")

    def get_thumbnails(self):
        return self.get_page_element(By.CSS_SELECTOR, "thumbnails")

    def get_selected_thumbnail(self, text_to_replace):
        return self.get_page_element(By.CSS_SELECTOR, "selectedThumbnail", text_to_replace)

    def get_carousel_indicators(self):
        return self.get_page_element(By.XPATH, "carouselIndicators")

    def get_paypal_credit_message(self):
        return self.get_page_element(By.XPATH, "paypalCreditMessage")
