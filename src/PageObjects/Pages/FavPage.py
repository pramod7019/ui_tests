import time
from ...PageObjects.PageElements.AllPageElements import AllPageElements


class FavPage:

    def __init__(self,):
        self.__fav_page_elements= AllPageElements.FAV_PAGE_ELEMENTS
        self.__wait_to_appear()
        self.__close_pop_up()

    def __wait_to_appear(self):
        self.__fav_page_elements.get_primary_add_cart().wait_to_appear(10, True)

    def select_size(self, i):
        sizes = self.__fav_page_elements.get_size().get_all_elements()
        if len(sizes) > i:
            if sizes[i].is_enabled():
                sizes[i].click()
                return sizes[i].text
        elif len(sizes) == 1:
            sizes[0].click()
            return sizes[0].text
        else:
            print(["No Sizes found on Favourites"])

    def click_on_primary(self):
        self.__fav_page_elements.get_primary_add_cart().click()

    def click_on_secondary(self):
        self.__fav_page_elements.get_secondary_add_cart().click()

    def remove_from_favourites(self, site):
        count = site.header_page.get_wishlist_count()
        if count > 0:
            site.header_page.click_wishlist()
            for remove_fav in self.__fav_page_elements.get_remove().get_all_elements():
                remove_fav.click()
                time.sleep(2)
            self.__fav_page_elements.get_fav_empty().wait_to_appear()

    def remove_from_favourites_aldo(self, site):
        count = site.header_page.get_wishlist_count_aldo()
        if count > 0:
            site.header_page.click_wishlist()
            for remove_fav in self.__fav_page_elements.get_remove().get_all_elements():
                remove_fav.click()
                time.sleep(2)
            self.__fav_page_elements.get_fav_empty().wait_to_appear()

    def verify_product_thumbnail_is_displayed(self):
        return self.__fav_page_elements.get_product_thumbnail().displayed()

    def click_product_thumbnail(self):
        self.__fav_page_elements.get_product_thumbnail().click()

    def __close_pop_up(self):
        pop_up = self.__fav_page_elements.get_pop_up_close_button()
        if pop_up.exists():
            pop_up.click()
