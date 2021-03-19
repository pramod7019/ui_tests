from ..PageElements.MyAccountPageElements import MyAccountPageElements


class MyAccountPage:

    def __init__(self):
        self.__my_account_page_elements = MyAccountPageElements()
        self.__wait_for_my_account_page()

    def click_sign_out(self):
        self.__my_account_page_elements.get_sign_out_button().get_visible_element()[0].click()

    def __wait_for_my_account_page(self):
        self.__my_account_page_elements.get_over_view_link().wait_to_appear()
        self.__my_account_page_elements.get_page_heading().wait_to_appear()

    def get_crew_coupon_code(self):
        promo_link = self.__my_account_page_elements.get_promo_link()
        promo_link.click()
        coupon = self.__my_account_page_elements.get_coupon_code().get_text()
        promo_link.click()
        return coupon

    def click_redeem_offer(self):
        self.__my_account_page_elements.get_redeem_offer_button().click()

    def click_on_my_info_link(self):
        self.__my_account_page_elements.get_my_info_link().click()

    def click_on_payment_link(self):
        self.__my_account_page_elements.get_payment_link().click()

