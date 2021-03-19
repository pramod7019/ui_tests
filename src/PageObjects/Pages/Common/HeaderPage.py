import time

from ....PageObjects.PageElements.AllPageElements import AllPageElements
from selenium.webdriver.common.keys import Keys

class HeaderPage:
    def __init__(self):
      self.__header_page_elements = AllPageElements.HEADER_PAGE_ELEMENTS
      self.wait_for_header_page()

    def click_on_my_account(self):
        my_account = self.__header_page_elements.get_my_account_button()
        if not my_account.is_clickable():
            mobile_myaccount = self.__header_page_elements.get_mobile_my_account_button().get_visible_element()[0]
            mobile_myaccount.click()
        else:
            my_account.js_click()

    def hover_on_header_nav_categories(self, category):
        self.__header_page_elements.get_header_nav_categories().mouse_over_by_text(category)

    def click_on_main_nav_mobile(self):
        self.__header_page_elements.main_nav_button_mobile().click()

    def close_footer_banner(self):
        banner = self.__header_page_elements.footer_notice_banner_ok_button()
        if banner.exists():
            banner.click()

    def click_on_navigation_category(self, category):
        main_nav = self.__header_page_elements.get_home_page_nav_for(category.lower())
        main_nav.click(wait_for_clickable=False)

    def category_href(self, category, sub_category):
      #return self.__header_page_elements.get_home_page_nav_for(category.lower(), sub_category.lower()).get_attribute("href")
        return "/{}/{}".format(category, sub_category)

    def user_account_href(self):
        return self.__header_page_elements.get_user_account_button().get_attribute("href")

    def wait_for_header_page(self):
        self.__header_page_elements.get_favourites_icon().wait_to_appear()
        self.__header_page_elements.get_search_button().wait_to_appear()
        self.__header_page_elements.get_cart_button().wait_to_appear()

    def click_search_button(self):
        self.__header_page_elements.get_search_button().js_click()

    def enter_search_keyword(self, keyword):
        self.__header_page_elements.get_search_field().set_text(keyword)

    def select_from_search_suggestion(self):
        self.__header_page_elements.get_search_suggestion().get_visible_element()[0].click()

    def click_favourites_icon(self):
        self.__header_page_elements.get_favourites_icon().click()

    def click_shopping_bag(self):
        self.__header_page_elements.get_cart_button().click()

    def change_country_language(self):
        language_link = self.__header_page_elements.get_language_link()
        if not language_link.is_clickable():
            self.__header_page_elements.get_mobile_language_link().get_visible_element()[0].click()
        else:
            language_link.click()

    def is_promotion_message_displayed(self):
        return self.__header_page_elements.get_promotional_message().get_visible_element()[0].is_displayed()

    def click_search_field_by_key(self):
        self.__header_page_elements.get_search_field().press_key(Keys.ENTER)

    def click_user_account(self):
        user_account = self.__header_page_elements.get_user_account_button()
        if not user_account.is_clickable():
            self.__header_page_elements.get_mobile_user_account_button().get_visible_element()[0].click()
        else:
            user_account.click()

    def get_header_message_bar_text(self, wait_time=10):
        header_message_element = self.__header_page_elements.get_header_message()
        start = time.time()
        header_message = header_message_element.get_text()
        while (time.time() - start) < wait_time:
          if header_message != "":
            break
          else:
            header_message = header_message_element.get_text()
        return header_message

    def get_wishlist_count_aldo(self):
        # self.__header_page_elements.get_wish_list_items_label().get_visible_element()
        if not self.__header_page_elements.get_favourites_label().exists():
            return 0
        return int(self.__header_page_elements.get_favourites_label().get_text())

    def get_wishlist_count(self):
        # self.__header_page_elements.get_wish_list_items_label().get_visible_element()
        if not self.__header_page_elements.get_favourites_label().exists():
            return 0
        count_str = str(self.__header_page_elements.get_favourites_label().get_text())
        return int(str(count_str))

    def click_wishlist(self):
        self.__header_page_elements.get_favourites_label().click()

    def click_on_header_cross(self):
        self.__header_page_elements.get_promo_banner_close_button().js_click()

    def click_on_navigation_category_mobile(self, category):
        main_nav = self.__header_page_elements.get_mobile_menu_category(category.lower())
        main_nav.click()

    def click_sub_category(self, menu_level1, menu_level2):
        self.__header_page_elements.get_menu_category_level1(menu_level1).get_visible_element()[0].click()
        self.__header_page_elements.get_menu_category_level2(menu_level2).get_visible_element()[0].click()

    def enter_search_keyword_mobile(self, keyword):
        search_field = self.__header_page_elements.get_mobile_search_field()
        search_field.wait_to_appear()
        search_field.set_text(keyword)
        search_field.press_key(Keys.ENTER)

    def click_favourites_icon_mobile(self):
        self.__header_page_elements.get_mobile_favourites_icon().click()

    def click_shopping_bag_mobile(self):
        self.__header_page_elements.get_mobile_cart_button().click()

    def mobile_user_account_href(self):
        return self.__header_page_elements.get_mobile_user_account_button().get_visible_element()[0].get_attribute("href")
