import time

from ...PageObjects.PageElements.AllPageElements import AllPageElements


class PDPPage:

    def __init__(self,):
        self.__pdp_page_elements = AllPageElements.PDP_PAGE_ELEMENTS
        self.__close_pdp_pop_up()
        self.__wait_to_appear()

    def select_colour(self, i):
        colours = self.__pdp_page_elements.get_pdp_colours_radio_buttons().get_all_elements()
        colour_to_select = colours[i].get_attribute('title')
        if len(colours) > i:
            if colours[i].is_enabled():
                colours[i].click()
                return colour_to_select
        elif len(colours) == 1:
            colours[0].click()
            return colours[0].get_attribute('title')
        else:
            print(["No Colours found on PDP"])

    def get_displayed_prices(self):
        prices_elements = self.__pdp_page_elements.get_pdp_price_block().get_all_elements()
        prices = []
        if prices_elements:
            for price in prices_elements:
                prices.append(price.text)
        return prices

    def get_reassurance_links(self):
        links = []
        link_elements = self.__pdp_page_elements.get_pdp_reassurance_links().get_all_elements()
        if link_elements:
            for link in link_elements:
                links.append(link.text)
        return links

    def select_size(self, i):
        sizes = self.__pdp_page_elements.get_pdp_sizes().get_all_elements()
        if len(sizes) > i:
            if sizes[i].is_enabled():
                sizes[i].click()
                return sizes[i].text
        elif len(sizes) == 1:
            sizes[0].click()
            return sizes[0].text
        else:
            print(["No Colours found on PDP"])

    def get_product_name(self):
        return self.__pdp_page_elements.get_pdp_product_name().get_text()

    def click_on_add_to_bag(self):
        self.__pdp_page_elements.get_pdp_add_to_bag_button().click()

    def size_selected(self):
        return self.__pdp_page_elements.get_pdp_selected_size_label().get_visible_element()[0].text

    def colour_selected(self):
        return self.__pdp_page_elements.get_pdp_selected_colour_label().get_text()

    def __wait_to_appear(self):
        self.__pdp_page_elements.get_pdp_product_name().wait_to_appear()
        self.__pdp_page_elements.get_pdp_price_block().wait_to_appear()


    def __close_pdp_pop_up(self):
        pop_up = self.__pdp_page_elements.get_pop_up_close_button()
        if pop_up.exists():
            pop_up.click()

    # def close_banner(self):
    #     banner =self.__pdp_page_elements.pdp_banner_close()
    #     if banner.exists():
    #         banner.click()

    def click_on_favourite_icon(self):
        self.__pdp_page_elements.get_favourites_button_un_selected().get_visible_element()[0].click()
        time.sleep(2)

    def click_on_size_chart(self):
        self.__pdp_page_elements.get_size_chart_button().click()

    def actions_in_size_chart(self, id):
        self.__pdp_page_elements.get_men_women_tabs().get_visible_element()[id].click()

    def get_selected_tab(self, id):
        return self.__pdp_page_elements.get_men_women_tabs().get_visible_element()[id].get_attribute("aria-selected")

    def size_chart_flow(self):
        results = []
        self.__pdp_page_elements.get_size_chart_button().click()
        if not self.__pdp_page_elements.get_men_women_tabs().exists():
            self.__pdp_page_elements.get_size_chart_button().click()
        self.actions_in_size_chart(1)
        results.append(self.get_selected_tab(0))
        results.append(self.get_selected_tab(1))
        self.actions_in_size_chart(0)
        results.append(self.get_selected_tab(0))
        results.append(self.get_selected_tab(1))
        return results

    def click_on_find_store(self):
        self.__pdp_page_elements.get_globo_find_in_store_button().click()

    def fill_store_with_data(self, data):
        self.click_on_find_store()
        self.__pdp_page_elements.get_location().set_text(data.postal_code)
        self.__pdp_page_elements.get_store_results().click()
        if self.__pdp_page_elements.get_map().exists() or self.__pdp_page_elements.get_out_stock():
            return True
        return False

    def click_and_verify_selected_thumbnail(self):
        product_thumbnails = self.__pdp_page_elements.get_thumbnails()
        if product_thumbnails.exists():
            for index, element in enumerate(product_thumbnails.get_all_elements()):
                element.click()
                assert self.__pdp_page_elements.get_selected_thumbnail(str(index)).exists()
                index = index+1
        else:
            return

    def click_bread_crumb(self, index):
        self.__pdp_page_elements.get_bread_crumb_links().click_child_element(index)

    def bread_crumb_text(self, index):
        texts = self.__pdp_page_elements.get_bread_crumb_links().get_text_of_child_elements()
        return texts[index].lower()

    def click_on_preview(self):
        self.__pdp_page_elements.get_zoom_button().click()

    def click_zoom_preview_btn(self):
        self.__pdp_page_elements.get_image_full_screen_button().click()

    def verify_if_image_close_button_is_displayed(self):
        return self.__pdp_page_elements.get_image_close_button().displayed()

    def verify_if_arrow_controls_are_displayed(self):
        return self.__pdp_page_elements.get_next_image_arrow_button().get_visible_element()[0].is_displayed()

    def verify_if_carousel_indicators_are_displayed(self):
        return self.__pdp_page_elements.get_carousel_indicators().displayed()

    def verify_if_paypal_credit_message_is_displayed(self):
        return self.__pdp_page_elements.get_paypal_credit_message().displayed()

    def verify_if_size_chart_link_is_displayed(self):
        return self.__pdp_page_elements.get_size_chart_button().displayed()
