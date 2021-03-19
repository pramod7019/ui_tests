import pytest

from uitests.src.Tests.Desktop.conftest import aldo, globo_cis, aldo_us


@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestMyAccountPayments:

    @aldo
    @aldo_us
    def test_add_new_credit_card_from_my_account_EE20_1791(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.my_account_page.click_on_my_info_link()
        site.my_account_payment_page.remove_all_payment_cards_from_account_profile()
        site.my_account_payment_page.click_on_add_new_credit_card()
        site.transaction_flow.credit_card_payment(data.creditcard[0], action="save payments")
        site.transaction_flow.fill_billing_details(data.shipping)
        site.my_account_payment_page.click_on_add_card_button()
        assert "1111" in site.my_account_payment_page.primary_credit_card_text()

    @globo_cis
    def test_add_new_credit_card_from_my_account(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.my_account_page.click_on_payment_link()
        site.my_account_payment_page.remove_all_payment_cards_from_account_profile()
        site.my_account_payment_page.click_on_add_new_credit_card()
        site.transaction_flow.credit_card_payment(data.creditcard[0], action="save payments")
        site.transaction_flow.fill_billing_details(data.shipping)
        site.my_account_payment_page.click_on_add_card_button()
        assert "1111" in site.my_account_payment_page.primary_credit_card_text()

    @aldo
    @aldo_us
    def test_remove_payment_cards_from_my_account_profile_EE20_1835(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.my_account_page.click_on_my_info_link()
        site.my_account_payment_page.remove_all_payment_cards_from_account_profile()
        assert site.my_account_payment_page.is_edit_card_button_displayed()
        site.my_account_payment_page.click_on_add_new_credit_card()
        site.transaction_flow.credit_card_payment(data.creditcard[0], action="save payments")
        site.transaction_flow.fill_billing_details(data.shipping)
        site.my_account_payment_page.click_on_add_card_button()
        site.my_account_payment_page.remove_all_payment_cards_from_account_profile()
        assert site.my_account_payment_page.is_edit_card_button_displayed()

    @globo_cis
    def test_remove_payment_card_from_my_account_profile(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.my_account_page.click_on_payment_link()
        site.my_account_payment_page.remove_all_payment_cards_from_account_profile()
        assert site.my_account_payment_page.is_edit_card_button_displayed()
        site.my_account_payment_page.click_on_add_new_credit_card()
        site.transaction_flow.credit_card_payment(data.creditcard[0], action="save payments")
        site.transaction_flow.fill_billing_details(data.shipping)
        site.my_account_payment_page.click_on_add_card_button()
        site.my_account_payment_page.remove_all_payment_cards_from_account_profile()
        assert site.my_account_payment_page.is_edit_card_button_displayed()

    @aldo
    @aldo_us
    def test_edit_payment_from_my_account_EE20_1839(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.my_account_page.click_on_my_info_link()
        site.my_account_payment_page.select_edit_card_button_by_index(0, data.creditcard[0], data.shipping)
        site.transaction_flow.credit_card_payment(data.creditcard[1], action="save payments")
        site.my_account_payment_page.click_update_card()
        assert "1113" in site.my_account_payment_page.primary_credit_card_text()

    @globo_cis
    def test_edit_payment_from_my_account(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.my_account_page.click_on_payment_link()
        site.my_account_payment_page.select_edit_card_button_by_index(0, data.creditcard[0], data.shipping)
        site.transaction_flow.credit_card_payment(data.creditcard[1], action="save payments")
        site.my_account_payment_page.click_update_card()
        assert "1113" in site.my_account_payment_page.primary_credit_card_text()

    @aldo
    @aldo_us
    def test_remove_payment_for_each_saved_card_EE20_1840(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.my_account_page.click_on_my_info_link()
        site.my_account_payment_page.remove_payments_for_each_saved_card()
        assert site.my_account_payment_page.is_edit_card_button_displayed()
        site.my_account_payment_page.click_on_add_new_credit_card()
        site.transaction_flow.credit_card_payment(data.creditcard[0], action="save payments")
        site.transaction_flow.fill_billing_details(data.shipping)
        site.my_account_payment_page.click_on_add_card_button()
        site.my_account_payment_page.remove_payments_for_each_saved_card()
        assert site.my_account_payment_page.is_edit_card_button_displayed()

    @globo_cis
    def test_remove_payment_for_each_saved_card(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.my_account_page.click_on_payment_link()
        site.my_account_payment_page.remove_payments_for_each_saved_card()
        assert site.my_account_payment_page.is_edit_card_button_displayed()
        site.my_account_payment_page.click_on_add_new_credit_card()
        site.transaction_flow.credit_card_payment(data.creditcard[0], action="save payments")
        site.transaction_flow.fill_billing_details(data.shipping)
        site.my_account_payment_page.click_on_add_card_button()
        site.my_account_payment_page.remove_payments_for_each_saved_card()
        assert site.my_account_payment_page.is_edit_card_button_displayed()

    @aldo
    @aldo_us
    def test_make_payment_card_as_primary_EE20_1841(self, data, site):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.my_account_page.click_on_my_info_link()
        site.my_account_payment_page.remove_all_payment_cards_from_account_profile()
        site.my_account_payment_page.click_on_add_new_credit_card()
        site.transaction_flow.credit_card_payment(data.creditcard[0], action="save payments")
        site.transaction_flow.fill_billing_details(data.shipping)
        site.my_account_payment_page.click_on_add_card_button()
        site.my_account_payment_page.click_on_add_new_credit_card()
        site.transaction_flow.credit_card_payment(data.creditcard[1], action="save payments")
        site.my_account_payment_page.select_country(data.shipping.country)
        site.transaction_flow.fill_billing_details(data.shipping)
        site.my_account_payment_page.click_on_add_card_button()
        assert "1113" in site.my_account_payment_page.verify_primary_credit_card_text()

    @globo_cis
    def test_make_payment_card_as_primary(self, data, site):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.my_account_page.click_on_payment_link()
        site.my_account_payment_page.remove_all_payment_cards_from_account_profile()
        site.my_account_payment_page.click_on_add_new_credit_card()
        site.transaction_flow.credit_card_payment(data.creditcard[0], action="save payments")
        site.transaction_flow.fill_billing_details(data.shipping)
        site.my_account_payment_page.click_on_add_card_button()
        site.my_account_payment_page.click_on_add_new_credit_card()
        site.transaction_flow.credit_card_payment(data.creditcard[1], action="save payments")
        site.transaction_flow.fill_billing_details(data.shipping)
        site.my_account_payment_page.click_on_add_card_button()
        assert "1113" in site.my_account_payment_page.verify_primary_credit_card_text()
