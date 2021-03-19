from uitests.src.Helpers.Browser import Browser
from ...PageObjects.PageElements.CheckoutPagePaymentSectionElements import CheckoutPagePaymentSectionElements
import time

class CheckoutPaymentPage:

    def __init__(self, **kwargs):
        self.__payment_elements = CheckoutPagePaymentSectionElements()
        if len(kwargs) == 0:
            self.__wait_for_payment_page()
        else:
            self.papal_args = kwargs
            if "payType" in kwargs:
                self.__paypal_paytype = self.papal_args["payType"]

    def select_credit_card_payment(self):
        self.__payment_elements.get_credit_card_payment().click()

    def fill_credit_card_number(self, card_number):
        self.__payment_elements.get_creditcard_iframe().switch_to_iframe()
        self.__payment_elements.get_creditcard_number_field().set_text(card_number)
        self.__payment_elements.get_creditcard_iframe().switch_to_default()

    def fill_cvc(self, cvv):
        self.__payment_elements.get_creditcard_cvc_field().set_text(cvv)

    def fill_card_expiry(self, cvv):
        self.__payment_elements.get_creditcard_expiry_field().set_text(cvv, loose_focus=True)

    def click_review_order(self):
        review_order = self.__payment_elements.get_review_order_button()
        if not review_order.is_clickable():
            review_order_mobile = self.__payment_elements.get_review_order_mobile()
            review_order_mobile.click()
            review_order_mobile.wait_to_disappear()
        else:
            review_order.click()
            review_order.wait_to_disappear()

    def select_paypal_payment(self):
        self.__payment_elements.get_paypal_payment().click()

    def select_interac_payment(self):
        self.__payment_elements.get_interac_payment().click()

    def select_visa_checkout_payment(self):
        self.__payment_elements.get_visa_checkout_payment().click()

    def click_billing_as_payment_check_box(self):
        self.__payment_elements.get_billing_same_as_shipping_checkbox().click(wait_for_clickable=False)

    def __wait_for_payment_page(self):
        self.__payment_elements.get_payment_title().wait_to_appear()
        self.__payment_elements.get_credit_card_payment().wait_to_appear()
        self.__payment_elements.get_paypal_payment().wait_to_appear()
        self.__payment_elements.get_visa_checkout_payment().wait_to_appear()

    def fill_paypal_login(self, paypalemailid):
        self.__payment_elements.get_paypal_emailid().set_text(paypalemailid)

    def fill_paypal_password(self, paypalpassword):
        self.__payment_elements.get_paypal_password().set_text(paypalpassword)

    def click_paypal_login(self):
        self.__payment_elements.get_paypal_login_button().click()

    def click_paypal_continue_button(self):
        self.__payment_elements.get_paypal_continue_button().click()

    def click_paypal_credit_continue_button(self):
        credit_continue_button_element = self.__payment_elements.get_paypal_credit_continue_button()
        if credit_continue_button_element.exists():
            credit_continue_button_element.js_click()

    def click_next_button_in_paypal_window(self):
        next_button = self.__payment_elements.get_next_button_in_paypal_window()
        if next_button.exists():
            next_button.js_click()
            next_button.wait_to_disappear()
        return

    def select_paypal_next_button(self):
        time.sleep(3)
        self.__payment_elements.get_paypal_iframe().switch_to_iframe()
        self.__click_paypal_button()

    def login_to_do_paypal_payment(self, paypal):
        if self.__paypal_paytype.lower() == "credit":
            self.select_paypal_credit_button()
        else:
            self.select_paypal_next_button()
        self.fill_paypal_login(paypal.username)
        self.click_next_button_in_paypal_window()
        self.fill_paypal_password(paypal.password)
        self.click_paypal_login()
        if self.__paypal_paytype.lower() == "credit":
            self.select_paypal_credit_radio_button()
            self.click_paypal_credit_continue_button()
        else:
            self.click_paypal_continue_button()

    def select_paypal_credit_button(self):
        time.sleep(3)
        self.__payment_elements.get_paypal_iframe().switch_to_iframe()
        self.__click_paypal_credit_button()

    def select_paypal_credit_radio_button(self):
        paypal_credit_radio_button_element = self.__payment_elements.get_paypal_credit_radio_button()
        if not paypal_credit_radio_button_element.is_checked():
            paypal_credit_radio_button_element.click()

    def provide_visa_login_details(self, visa):
        time.sleep(5)
        self.__payment_elements.get_visa_iframe().switch_to_iframe()
        self.__payment_elements.get_visa_email().type_text(visa.username)
        self.__payment_elements.get_visa_password().type_text(visa.password)
        self.__payment_elements.get_visa_login_button().click()
        self.__payment_elements.get_visa_confirm_button().click()

    def select_visa_next_button(self):
        self.__payment_elements.get_visa_next_button().click()

    def __click_paypal_button(self):
        self.__payment_elements.get_paypal_next_button().click()
        for k in range(0, 2):
          if not self.__payment_elements.get_paypal_emailid().displayed():
            self.__payment_elements.get_paypal_next_button().click()

    def __click_paypal_credit_button(self):
        self.__payment_elements.get_paypal_credit_button().click()

    def select_after_pay_payment(self):
        self.__payment_elements.get_after_pay_payment().click()
        self.__payment_elements.get_after_pay_payment_button().click()

    def enter_after_pay_information(self, email, password):
        Browser.switch_to_latest_active_window()
        self.__payment_elements.get_after_pay_email_field().set_text(email)
        self.__payment_elements.get_after_pay_continue_button().click()
        self.__payment_elements.get_after_pay_password_field().set_text(password)
        self.__payment_elements.get_after_pay_confirm_button().click()
        self.__payment_elements.get_after_pay_got_it_button().click()
        self.__payment_elements.get_after_pay_agree_checkbox().click()
        self.__payment_elements.get_after_pay_confirm_button().click()

