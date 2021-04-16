import time

from uitests.src.PageObjects.Pages.PDPPage import PDPPage
from uitests.src.PageObjects.Pages.PLPPage import PLPPage
from uitests.src.PageObjects.Pages.SignInPage import SignInPage
from uitests.src.PageObjects.Pages.CartPage import CartPage
from uitests.src.PageObjects.Pages.CheckoutShippingPage import CheckoutShippingPage
from uitests.src.PageObjects.Pages.CheckoutPaymentPage import CheckoutPaymentPage
from uitests.src.PageObjects.Pages.Common.HeaderPage import HeaderPage
from uitests.src.PageObjects.Pages.SignUpPage import SignUpPage
from uitests.src.PageObjects.Pages.MyAccountPage import MyAccountPage


class TransactionFlow:

    # Page flow : Start: Home page header, end page: pdp page
    def go_to_pdp_from_home_menu(self, menu_category, plp_product_index):
        TransactionFlow().go_to_plp_page_from_home_page_navigation(menu_category)
        PLPPage().select_product_by_index(plp_product_index)

    def go_to_pdp_from_home_search(self, product_code):
        self.go_to_plp_page_from_home_page_search(product_code)
        PLPPage().select_product_by_index(0)

    # Page flow : Start: Home page header, end page: cart page
    def add_product_to_cart_from_home_search(self, product_code, mobile=False):
        if mobile:
            self.go_to_plp_page_from_home_page_search_mobile(product_code)
        else:
            self.go_to_plp_page_from_home_page_search(product_code)
        PLPPage().select_product_by_index(0)
        PDPPage().select_size(2)
        PDPPage().click_on_add_to_bag()

    # Page flow : Start: Home page header, end page: cart page
    def add_product_to_cart_from_home_menu(self, category, plp_product_index):
        TransactionFlow.go_to_pdp_from_home_menu(self,category, plp_product_index)
        PDPPage().select_size(0)
        PDPPage().click_on_add_to_bag()

    # Page flow: start: Checkout shipping page, end: Checkout shipping page
    def fill_shipping_for_guest(self, shipping_method, shipping_address):
        CheckoutShippingPage().wait_for_shipping_method_details()
        CheckoutShippingPage().select_shipping_method(shipping_method)
        CheckoutShippingPage().fill_first_name(shipping_address.first_name)
        CheckoutShippingPage().fill_last_name(shipping_address.last_name)
        CheckoutShippingPage().fill_email_address(shipping_address.email)
        CheckoutShippingPage().fill_street_select_address(shipping_address.street)
        CheckoutShippingPage().fill_phone_number(shipping_address.phone)

    # Page flow start: checkout payment, end: checkout payment
    def credit_card_payment(self, creditcard, **action_args):
        if len(action_args) > 0 and "action" in action_args:
            CheckoutPaymentPage(action="save payments").fill_credit_card_number(creditcard['Cardnumber'])
            CheckoutPaymentPage(action="save payments").fill_card_expiry(creditcard['Date'])
            CheckoutPaymentPage(action="save payments").fill_cvc(creditcard['Cvv'])
        else:
            CheckoutPaymentPage().fill_credit_card_number(creditcard['Cardnumber'])
            CheckoutPaymentPage().fill_card_expiry(creditcard['Date'])
            CheckoutPaymentPage().fill_cvc(creditcard['Cvv'])


    # Page flow start: Cart page, end cart page
    def edit_item_quantity_in_cart(self, product_index, qty):
        CartPage().click_on_edit_product(product_index)
        CartPage().select_product_quantity(qty)
        CartPage().click_on_save_edits()

    # Page flow start: Cart page, end cart page
    def edit_item_colour_in_cart(self, product_index, colour_index):
        CartPage().click_on_edit_product(product_index)
        edited_colour = CartPage().select_product_colour(colour_index)
        CartPage().click_on_save_edits()
        return edited_colour

    # Page flow start: Home page, end Home page logged in
    def user_login(self, username, password):
        HeaderPage().click_on_my_account()
        SignInPage().enter_user_name(username)
        SignInPage().enter_password(password)
        SignInPage().click_on_sign_in_button()

    def fill_shipping_for_sign_in_user(self, shipping_method, shipping_address, url):
        CheckoutShippingPage().wait_for_shipping_method_details()
        CheckoutShippingPage().select_shipping_method(shipping_method)
        if "globo" in url:
            CheckoutShippingPage().select_address_from_default_address(0)
            if CheckoutShippingPage().get_default_address_edit_button() < 1:
                CheckoutShippingPage().fill_phone_number(shipping_address.phone)

    def go_to_plp_page_from_home_page_navigation(self, menu_category):
        HeaderPage().hover_on_header_nav_categories(menu_category)
        HeaderPage().click_on_navigation_category(menu_category)
        PLPPage().is_plp_open()

    def go_to_plp_page_from_home_page_search(self, product_code):
        HeaderPage().click_search_button()
        HeaderPage().enter_search_keyword(product_code)
        HeaderPage().click_search_field_by_key()
        PLPPage().wait_for_plp_page()

    # fill common user details for sign up in aldo, cis & aldo
    def fill_user_details_for_sign_up(self, email, user_details, password):
        TransactionFlow().click_register_for_new_user_sign_up()
        SignUpPage().enter_email_address(email)
        SignUpPage().enter_first_name(user_details.first_name)
        SignUpPage().enter_last_name(user_details.last_name)
        SignUpPage().enter_password(password)

    # fill optional details for aldo crew and CIS news letter signup
    def fill_optional_user_details_for_sign_up(self, shipping, user_details):
        SignUpPage().click_womens_gender()
        SignUpPage().enter_postal_code(shipping.postal_code)
        SignUpPage().select_dob_date(user_details.dob_date)
        SignUpPage().select_dob_month(user_details.dob_month)
        SignUpPage().select_dob_year(user_details.dob_year)

    def click_register_for_new_user_sign_up(self):
        HeaderPage().click_on_my_account()
        SignInPage().click_on_register()

    def open_filters_overlay(self, menu_category):
        TransactionFlow().go_to_plp_page_from_home_page_navigation(menu_category)
        PLPPage().click_open_filter_button()

    def user_logout(self):
        HeaderPage().click_user_account()
        MyAccountPage().click_sign_out()

    def click_and_do_paypal_payment(self, paypal, paypal_type):
        CheckoutPaymentPage(payType=paypal_type).login_to_do_paypal_payment(paypal)
        time.sleep(5)

    def click_and_do_visa_checkout(self, visa):
        CheckoutPaymentPage().select_visa_next_button()
        CheckoutPaymentPage().provide_visa_login_details(visa)

    def fill_shipping_to_store_for_guest(self, shipping_address):
        CheckoutShippingPage().click_ship_to_store_button()
        CheckoutShippingPage().fill_first_name(shipping_address.first_name)
        CheckoutShippingPage().fill_last_name(shipping_address.last_name)
        CheckoutShippingPage().fill_email_address(shipping_address.email)
        CheckoutShippingPage().fill_store_address_select_suggestion(shipping_address.postal_code)
        CheckoutShippingPage().select_store(1)

    def fill_shipping_to_store_sign_in_user(self, shipping_address):
        CheckoutShippingPage().click_ship_to_store_button()
        time.sleep(3)
        CheckoutShippingPage().fill_store_address_select_suggestion(shipping_address.postal_code)
        CheckoutShippingPage().select_store(1)

    def fill_billing_details(self, shipping_address):
        CheckoutShippingPage().fill_street_select_address(shipping_address.street)
        CheckoutShippingPage().fill_city(shipping_address.city)
        CheckoutShippingPage().fill_phone_number(shipping_address.phone)

    def go_to_pdp_from_home_menu_mobile(self, menu_category, plp_product_index, level1, level2):
        self.go_to_plp_page_from_home_page_navigation_mobile(menu_category, level1, level2)
        PLPPage().select_product_by_index(plp_product_index)

    def go_to_plp_page_from_home_page_navigation_mobile(self, category, level1, level2):
        HeaderPage().click_on_main_nav_mobile()
        HeaderPage().click_on_navigation_category_mobile(category)
        HeaderPage().click_sub_category(level1, level2)

    def go_to_plp_page_from_home_page_search_mobile(self, product_code):
        HeaderPage().click_search_button()
        time.sleep(5)
        HeaderPage().enter_search_keyword_mobile(product_code)
        PLPPage().wait_for_plp_page()

