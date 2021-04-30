import threading
import time

from ..Helpers.Browser import Browser
from .TestFlows import TransactionFlow
from .Pages import PDPPage, PLPPage, CartPage, SignInPage, CheckoutShippingPage, OrderHistoryPage, CheckoutPaymentPage, ConfirmationPage, \
  CheckoutReviewPage, MyAccountPage, SignUpPage, FilterPage, CheckoutSummaryPage, FavPage, ErrorPage, MyAccountPaymentPage, MyAccountInfoSectionPage
from .Pages.Common import HeaderPage, FooterPage
from ..Tests.CommonConfig import CommonConfig


class Page(CommonConfig):

    def __init__(self,
                 banner='ALDO-CAEN',
                 browser='chrome',
                 environment='UAT',
                 url=None):
        CommonConfig.__init__(self, banner_local=banner, browser=browser, environment=environment, purl=url)
        threading.Thread(target=self.__start_driver())

    def __start_driver(self):
        Browser().create_new_driver(self.get_browser())

    def open(self):
        Browser.get_driver().get(self.get_site_url())

    def current_url(self):
        return Browser.get_current_url()

    @property
    def header_page(self):
        return HeaderPage.HeaderPage()

    @property
    def pdp_page(self):
        return PDPPage.PDPPage()

    @property
    def plp_page(self):
        return PLPPage.PLPPage()

    @property
    def cart_page(self):
        return CartPage.CartPage()

    @property
    def sign_in_page(self):
        return SignInPage.SignInPage()

    @property
    def shipping_page(self):
        return CheckoutShippingPage.CheckoutShippingPage()

    @property
    def payment_page(self):
        return CheckoutPaymentPage.CheckoutPaymentPage()

    @property
    def review_page(self):
        return CheckoutReviewPage.CheckoutReviewPage()

    @property
    def transaction_flow(self):
        return TransactionFlow.TransactionFlow()

    @property
    def confirmation_page(self):
        return ConfirmationPage.ConfirmationPage()

    @property
    def my_account_page(self):
        return MyAccountPage.MyAccountPage()

    @property
    def sign_up_page(self):
        return SignUpPage.SignUpPage()

    @property
    def filters_page(self):
        return FilterPage.FilterPage()

    @property
    def summary_page(self):
        return CheckoutSummaryPage.CheckoutSummaryPage()

    @property
    def fav_page(self):
        return FavPage.FavPage()

    @property
    def order_history_page(self):
        return OrderHistoryPage.OrderHistoryPage()

    @property
    def footerpage(self):
        return FooterPage.FooterPage()

    @property
    def error_modal(self):
        return ErrorPage.ErrorPage()

    @property
    def my_account_payment_page(self):
        return MyAccountPaymentPage.MyAccountPaymentSectionPage()

    def close(self):
        Browser.shutdown()

    def page_refresh(self):
        Browser.get_driver().refresh()

    def page_title(self, title):
        return Browser.wait_for_page_title(title)

    def get_screen_shot(self, test_name):
        return Browser.take_screenshot(test_name)

    def switch_to_latest_window_and_get_url(self):
        return Browser.switch_to_new_window_and_get_url()

    def execute_command(self, command):
        Browser.get_driver().execute_script(command)

    def switch_to_latest_active_window(self):
        return Browser.switch_to_latest_active_window()

    @property
    def my_account_edit_page(self):
        return MyAccountInfoSectionPage.MyAccountInfoSectionPage()
