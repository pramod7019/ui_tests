from selenium.webdriver.common.by import By
from ...Helpers.LocatorDatabase.Locators import Locators


class CheckoutPagePaymentSectionElements(Locators):

    def __init__(self):
        Locators.__init__(self, "CheckoutPagePaymentSectionLocators")

    def get_creditcard_number_field(self):
        return self.get_page_element(By.XPATH, "creditCardNumber")

    def get_creditcard_iframe(self):
        return self.get_page_element(By.XPATH, "creditCardIframe")

    def get_creditcard_expiry_field(self):
        return self.get_page_element(By.ID, "creditCardExpiry")

    def get_creditcard_cvc_field(self):
        return self.get_page_element(By.ID, "creditCardCVC")

    def get_billing_same_as_shipping_checkbox(self):
        return self.get_page_element(By.XPATH, "billingSameAsShipping")

    def get_credit_card_payment(self):
        return self.get_page_element(By.XPATH, "creditCardPayment")

    def get_paypal_payment(self):
        return self.get_page_element(By.XPATH, "paypalPayment")

    def get_interac_payment(self):
        return self.get_page_element(By.XPATH, "interacPayment")

    def get_visa_checkout_payment(self):
        return self.get_page_element(By.XPATH, "visaCheckoutPayment")

    def get_saved_payment(self):
        return self.get_page_element(By.XPATH, "savedPayment")

    def get_review_order_button(self):
        return self.get_page_element(By.XPATH, "reviewOrder")

    def get_payment_title(self):
        return self.get_page_element(By.XPATH, "paymentTitle")

    def get_paypal_iframe(self):
        return self.get_page_element(By.CSS_SELECTOR, "paypaliframe")

    def get_paypal_next_button(self):
        return self.get_page_element(By.XPATH, "paypalPaymentButton")

    def get_paypal_credit_button(self):
        return self.get_page_element(By.XPATH, "paypalCreditButton")

    def get_visa_returning_customer(self):
        return self.get_page_element(By.XPATH, "visaReturningCustomer")

    def get_visa_email(self):
        return self.get_page_element(By.XPATH, "visaEmail")

    def get_visa_password(self):
        return self.get_page_element(By.XPATH, "visaPassword")

    def get_visa_login_button(self):
        return self.get_page_element(By.XPATH, "visaLogin")

    def get_visa_next_button(self):
        return self.get_page_element(By.XPATH, "visaNextButton")

    def get_visa_confirm_button(self):
        return self.get_page_element(By.XPATH, "visaConfirm")

    def get_visa_iframe(self):
        return self.get_page_element(By.XPATH, "visaCheckoutiframe")

    def get_paypal_emailid(self):
        return self.get_page_element(By.XPATH, "paypalLogin")

    def get_paypal_button(self):
        return self.get_page_element(By.XPATH, "paypalPayment_next1")

    def get_paypal_password(self):
        return self.get_page_element(By.XPATH, "paypalPassword")

    def get_paypal_login_button(self):
        return self.get_page_element(By.XPATH, "paypalLoginButton")

    def get_paypal_continue_button(self):
        return self.get_page_element(By.XPATH, "paypalContinueButton")

    def get_paypal_credit_radio_button(self):
        return self.get_page_element(By.XPATH, "paypalCreditRadioButton")

    def get_paypal_credit_continue_button(self):
        return self.get_page_element(By.XPATH, "paypalCreditContinueButton")

    def get_next_button_in_paypal_window(self):
        return self.get_page_element(By.XPATH, "paypalNextButton")

    def get_after_pay_payment(self):
        return self.get_page_element(By.XPATH, "afterpayPayment")

    def get_after_pay_payment_button(self):
        return self.get_page_element(By.XPATH, "afterpayPaymentButton")

    def get_after_pay_email_field(self):
        return self.get_page_element(By.XPATH, "afterpayEmailField")

    def get_after_pay_continue_button(self):
        return self.get_page_element(By.XPATH, "afterpayContinueButton")

    def get_after_pay_password_field(self):
        return self.get_page_element(By.XPATH, "afterpayPasswordField")

    def get_after_pay_got_it_button(self):
        return self.get_page_element(By.XPATH, "afterpayGotItButton")

    def get_after_pay_agree_checkbox(self):
        return self.get_page_element(By.XPATH, "afterpayAgreeCheckbox")

    def get_after_pay_confirm_button(self):
        return self.get_page_element(By.XPATH, "afterpayConfirmButton")

    def get_review_order_mobile(self):
        return self.get_page_element(By.XPATH, "reviewOrderMobile")

