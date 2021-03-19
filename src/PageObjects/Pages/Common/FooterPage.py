from uitests.src.Helpers.Browser import Browser
from ....PageObjects.PageElements.FooterPageElements import FooterPageElements


class FooterPage():
    def __init__(self):
        self.__footer_page_elements = FooterPageElements()

    def verify_footers_generalise(self, page_element, link_text, url):
        self.__footer_page_elements.get_footer_link(link_text).wait_to_appear()
        self.__footer_page_elements.get_footer_link(link_text).click()
        pop_up = self.__footer_page_elements.get_pop_up_close_button()
        if pop_up.exists():
            pop_up.click()
        page_element.wait_to_appear()
        assert Browser.get_current_url().find(url)

    def verify_footers_generalise_new_window(self, page_element, link_text, url):
        self.__footer_page_elements.get_footer_link(link_text).wait_to_appear()
        self.__footer_page_elements.get_footer_link(link_text).click()
        Browser.switch_to_latest_active_window()
        page_element.wait_to_appear()
        assert Browser.get_current_url().find(url)
        Browser.close_current_active_window()

    def verify_footers_aldo(self, link_text, urls):
        self.verify_footers_generalise(self.__footer_page_elements.get_appointments(), link_text.appointments,
                                       urls.appointments)
        self.verify_footers_generalise(self.__footer_page_elements.get_store_locators(), link_text.store_locator,
                                       urls.store_locator)
        self.verify_footers_generalise(self.__footer_page_elements.get_track_order(), link_text.track_order,
                                       urls.track_order)
        self.verify_footers_generalise(self.__footer_page_elements.get_contactus(), link_text.contact_us,
                                       urls.contact_us)
        self.verify_footers_generalise(self.__footer_page_elements.get_return_policy(), link_text.returns,
                                       urls.returns)
        self.verify_footers_generalise(self.__footer_page_elements.get_help_center(), link_text.customer_service,
                                       urls.customer_service)
        self.verify_footers_generalise_new_window(self.__footer_page_elements.get_careers(), link_text.opportunities,
                                                  urls.opportunities)
        self.verify_footers_generalise_new_window(self.__footer_page_elements.get_aldo_group(), link_text.aldo_group,
                                                  urls.aldo_group)
        self.verify_footers_generalise(self.__footer_page_elements.get_gift_cards(), link_text.gift_cards,
                                       urls.gift_cards)
        self.verify_footers_generalise(self.__footer_page_elements.get_about_us(), link_text.about_us,
                                       urls.about_us)

    def verify_footers_cis(self, link_text, urls):
        self.verify_footers_generalise(self.__footer_page_elements.get_help_center(), link_text.customer_service,
                                       urls.customer_service)
        self.verify_footers_generalise(self.__footer_page_elements.get_gift_cards(), link_text.gift_cards,
                                       urls.gift_cards)
        self.verify_footers_generalise(self.__footer_page_elements.get_store_locators(), link_text.store_locator,
                                       urls.store_locator)
        self.verify_footers_generalise(self.__footer_page_elements.get_appointments(), link_text.contact_us,
                                       urls.contact_us)
        self.verify_footers_generalise(self.__footer_page_elements.get_track_order(), link_text.track_order,
                                       urls.track_order)
        self.verify_footers_generalise(self.__footer_page_elements.get_return_policy(), link_text.returns,
                                       urls.returns)
        self.verify_footers_generalise(self.__footer_page_elements.get_kindaf(), link_text.kindaf,
                                       urls.kindaf)
        self.verify_footers_generalise_new_window(self.__footer_page_elements.get_responsibility(), link_text.aldo_group,
                                                  urls.aldo_group)
        self.verify_footers_generalise_new_window(self.__footer_page_elements.get_about_us(), link_text.about_us,
                                                  urls.about_us)
        self.verify_footers_generalise_new_window(self.__footer_page_elements.get_careers(), link_text.opportunities,
                                                  urls.opportunities)
        self.verify_footers_generalise(self.__footer_page_elements.get_shipping(), link_text.appointments,
                                       urls.appointments)

    def verify_footers_globo(self, link_text, urls):
        self.verify_footers_generalise(self.__footer_page_elements.get_help_center(), link_text.customer_service,
                                       urls.customer_service)
        self.verify_footers_generalise(self.__footer_page_elements.get_shipping(), link_text.appointments,
                                       urls.appointments)
        self.verify_footers_generalise(self.__footer_page_elements.get_store_locators(), link_text.store_locator,
                                       urls.store_locator)
        self.verify_footers_generalise(self.__footer_page_elements.get_track_order(), link_text.track_order,
                                       urls.track_order)
        self.verify_footers_generalise(self.__footer_page_elements.get_return_policy(), link_text.returns,
                                       urls.returns)
        self.verify_footers_generalise_new_window(self.__footer_page_elements.get_gift_cards(), link_text.gift_cards,
                                                  urls.gift_cards)
        self.verify_footers_generalise_new_window(self.__footer_page_elements.get_contactus(), link_text.contact_us,
                                                  urls.contact_us)
        self.verify_footers_generalise_new_window(self.__footer_page_elements.get_aldo_group(), link_text.aldo_group,
                                                  urls.aldo_group)
        self.verify_footers_generalise_new_window(self.__footer_page_elements.get_about_us(), link_text.about_us,
                                                  urls.about_us)
        self.verify_footers_generalise_new_window(self.__footer_page_elements.get_careers(), link_text.opportunities,
                                                  urls.opportunities)

    def click_all_countries_link(self):
        self.__footer_page_elements.get_all_countries_link().get_visible_element()[0].click()

    def change_country_link(self):
        self.__footer_page_elements.get_all_countries_link().get_visible_element()[0].click()
        self.__footer_page_elements.get_north_america_link().click()
        self.__footer_page_elements.get_usa_link().click()

    def verify_if_north_america_tab_is_displayed(self):
        return self.__footer_page_elements.get_north_america_link().displayed()
