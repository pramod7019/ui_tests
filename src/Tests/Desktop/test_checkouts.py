import pytest

from uitests.src.Tests.Desktop.conftest import aldo_us


@pytest.mark.checkouts
@pytest.mark.regression
@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestCheckouts:

    def test_guest_checkout_ship_to_store_creditcard_EE20_1705(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_to_store_for_guest(data.shipping)
        site.shipping_page.click_on_continue_payment_button_with_no_suggestion()
        site.transaction_flow.credit_card_payment(data.creditcard[0])
        site.transaction_flow.fill_billing_details(data.shipping)
        site.payment_page.click_review_order()
        site.review_page.click_on_place_order("credit card")
        assert site.confirmation_page.is_cart_id_displayed()

    def test_sign_in_user_checkout_ship_to_store_creditcard_EE20_1706(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_to_store_sign_in_user(data.shipping)
        site.shipping_page.click_on_continue_payment_button()
        site.payment_page.select_credit_card_payment()
        site.transaction_flow.credit_card_payment(data.creditcard[0])
        site.transaction_flow.fill_billing_details(data.shipping)
        site.payment_page.click_review_order()
        site.review_page.click_on_place_order("credit card")
        assert site.confirmation_page.is_cart_id_displayed()
        site.transaction_flow.user_logout()
        assert data.logged_out_message in site.header_page.get_header_message_bar_text()

    def test_guest_checkout_ship_to_store_paypal_EE20_1711(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_to_store_for_guest(data.shipping)
        site.shipping_page.click_on_continue_payment_button_with_no_suggestion()
        site.payment_page.select_paypal_payment()
        site.transaction_flow.fill_billing_details(data.shipping)
        site.transaction_flow.click_and_do_paypal_payment(data.paypal, "paypal")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_guest_user_paypal_in_checkout_EE20_1701(self, site, data, shipping_method):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_for_guest(shipping_method, data.shipping)
        site.shipping_page.click_on_continue_payment_button()
        site.payment_page.select_paypal_payment()
        site.transaction_flow.click_and_do_paypal_payment(data.paypal, "paypal")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_guest_user_express_paypal_checkout_EE20_1703(self, site, data, shipping_method):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.transaction_flow.click_and_do_paypal_payment(data.paypal, "paypal")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    @aldo_us
    def test_guest_checkout_express_paypal_credit_EE20_1711(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.transaction_flow.click_and_do_paypal_payment(data.paypal_credit, "credit")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    @aldo_us
    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_guest_standard_checkout_paypal_credit_EE20_1713(self, site, data, shipping_method):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_for_guest(shipping_method, data.shipping)
        site.shipping_page.click_on_continue_payment_button()
        site.payment_page.select_paypal_payment()
        site.transaction_flow.click_and_do_paypal_payment(data.paypal_credit, "credit")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal credit")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    def test_signin_user_express_paypal_checkout_EE20_1752(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.transaction_flow.click_and_do_paypal_payment(data.paypal, "paypal")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_signin_user_paypal_standard_checkout_EE20_1754(self, site, data, shipping_method):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_for_sign_in_user(shipping_method, data.shipping)
        site.shipping_page.click_on_continue_payment_button()
        site.payment_page.select_paypal_payment()
        site.transaction_flow.click_and_do_paypal_payment(data.paypal, "paypal")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    def test_signin_user_paypal_ship_to_store_checkout_EE20_1753(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_to_store_sign_in_user(data.shipping)
        site.shipping_page.click_on_continue_payment_button_with_no_suggestion()
        site.payment_page.select_paypal_payment()
        site.transaction_flow.fill_billing_details(data.shipping)
        site.transaction_flow.click_and_do_paypal_payment(data.paypal, "paypal")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    @aldo_us
    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_signin_user_express_paypal_credit_checkout_EE20_1805(self, site, data, shipping_method):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.execute_command(data.feature_toggle.deactivate_hide_shipping_method)
        site.execute_command(data.feature_toggle.deactivate_disable_paypal_credit)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.select_shipping_method(shipping_method)
        site.transaction_flow.click_and_do_paypal_payment(data.paypal_credit, "credit")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal credit")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    @aldo_us
    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_signin_user_regular_paypal_credit_standard_checkout_EE20_1803(self, site, data, shipping_method):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_for_sign_in_user(shipping_method, data.shipping)
        site.shipping_page.click_on_continue_payment_button()
        site.payment_page.select_paypal_payment()
        site.transaction_flow.click_and_do_paypal_payment(data.paypal_credit, "credit")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal credit")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    @aldo_us
    def test_signin_user_regular_paypal_credit_ship_to_store_checkout_EE20_1785(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_to_store_sign_in_user(data.shipping)
        site.shipping_page.click_on_continue_payment_button_with_no_suggestion()
        site.payment_page.select_paypal_payment()
        site.transaction_flow.fill_billing_details(data.shipping)
        site.transaction_flow.click_and_do_paypal_payment(data.paypal_credit, "credit")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal credit")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    @aldo_us
    def test_guest_ship_to_store_checkout_paypal_credit_EE20_1785(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_to_store_for_guest(data.shipping)
        site.shipping_page.click_on_continue_payment_button_with_no_suggestion()
        site.payment_page.select_paypal_payment()
        site.transaction_flow.fill_billing_details(data.shipping)
        site.transaction_flow.click_and_do_paypal_payment(data.paypal_credit, "credit")
        site.switch_to_latest_active_window()
        site.review_page.click_on_place_order("paypal credit")
        if site.error_modal.get_modal_title().exists():
            site.error_modal.click_on_close_button()
        else:
            assert site.confirmation_page.is_cart_id_displayed()

    def test_guest_checkout_ship_to_store_visa_EE20_1710(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_to_store_for_guest(data.shipping)
        site.shipping_page.click_on_continue_payment_button_with_no_suggestion()
        site.payment_page.select_visa_checkout_payment()
        site.transaction_flow.click_and_do_visa_checkout(data.visa_checkout)
        site.payment_page.click_review_order()

    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_guest_user_express_visa_checkout_EE20_1704(self, site, data, shipping_method):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.transaction_flow.click_and_do_visa_checkout(data.visa_checkout)
        site.review_page.click_on_place_order("visa")
        assert site.confirmation_page.is_cart_id_displayed()

    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_guest_user_visa_in_checkout_EE20_1702(self, site, data, shipping_method):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_for_guest(shipping_method, data.shipping)
        site.shipping_page.click_on_continue_payment_button()
        site.payment_page.select_visa_checkout_payment()
        site.transaction_flow.click_and_do_visa_checkout(data.visa_checkout)
        # site.payment_page.click_review_order()
        site.review_page.click_on_place_order("visa")
        assert site.confirmation_page.is_cart_id_displayed()

    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_after_pay_checkout(self, site, data, shipping_method):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_for_guest(shipping_method, data.shipping)
        site.shipping_page.click_on_continue_payment_button()
        site.payment_page.select_after_pay_payment()
        site.payment_page.enter_after_pay_information(data.user_email, "Aldo@1234")
        site.switch_to_latest_active_window()
        site.payment_page.click_review_order()
        site.review_page.click_on_place_order()
        assert site.confirmation_page.is_cart_id_displayed()
