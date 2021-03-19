
import pytest
from .conftest import globo_cis, aldo, aldo_cis, cis


@pytest.mark.signup
@pytest.mark.regression
@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestLoginFlow:

    @globo_cis
    def test_sign_up_EE20_1677(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_verify_recaptcha)
        site.transaction_flow.fill_user_details_for_sign_up(data.user_email, data.shipping, data.user_password)
        site.sign_up_page.enter_confirm_password(data.user_password)
        site.sign_up_page.click_create_account()
        assert data.sign_up_message == site.header_page.get_header_message_bar_text()

    def test_sign_in_from_sign_up_page_EE20_1678(self, site):
        site.header_page.click_on_my_account()
        site.sign_in_page.click_on_register()
        site.sign_up_page.click_sign_in_with_email()
        assert site.sign_in_page.is_show_password_button_displayed()

    def test_to_verify_if_legal_disclaimer_displayed_EE20_1679(self, site):
        site.header_page.click_on_my_account()
        site.sign_in_page.click_on_register()
        assert site.sign_up_page.is_legal_disclaimer_displayed()

    @aldo_cis
    def test_if_user_can_sign_in_with_facebook_EE20_1680(self, site):
        site.header_page.click_on_my_account()
        site.sign_in_page.click_on_register()
        site.sign_up_page.click_sign_in_with_fb()
        assert "facebook" in site.switch_to_latest_window_and_get_url()

    @cis
    def test_cis_newsletter_signup_EE20_1681(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_verify_recaptcha)
        site.transaction_flow.fill_user_details_for_sign_up(data.user_email, data.shipping, data.user_password)
        site.sign_up_page.enter_confirm_password(data.user_password)
        site.sign_up_page.click_cis_sign_up_news_letter()
        site.transaction_flow.fill_optional_user_details_for_sign_up(data.shipping, data.user_details)
        site.sign_up_page.click_create_account()
        assert data.sign_up_message == site.header_page.get_header_message_bar_text()

    @aldo
    def test_aldo_crew_sign_up_EE20_1682(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_verify_recaptcha)
        site.transaction_flow.fill_user_details_for_sign_up(data.user_email, data.shipping, data.user_password)
        site.transaction_flow.fill_optional_user_details_for_sign_up(data.shipping, data.user_details)
        site.sign_up_page.enter_phone_number(data.shipping.phone)
        site.sign_up_page.click_create_account()
        assert "account" in site.header_page.user_account_href()

    def test_invalid_email_sign_up_EE20_1683(self, site):
        site.transaction_flow.click_register_for_new_user_sign_up()
        site.sign_up_page.enter_email_address("automation", new=False)
        site.sign_up_page.enter_first_name("")
        assert site.sign_up_page.is_email_error_validation_message_displayed()

    def test_invalid_first_name_EE20_1684(self, site):
        site.transaction_flow.click_register_for_new_user_sign_up()
        site.sign_up_page.enter_first_name("qa@1")
        site.sign_up_page.enter_last_name("")
        assert site.sign_up_page.is_first_name_error_validation_message_displayed()

    def test_invalid_last_name_EE20_1685(self, site):
        site.transaction_flow.click_register_for_new_user_sign_up()
        site.sign_up_page.enter_last_name("automation&^")
        site.sign_up_page.enter_first_name("")
        assert site.sign_up_page.is_last_name_error_validation_message_displayed()

    def test_invalid_password_EE20_1686(self, site):
        site.transaction_flow.click_register_for_new_user_sign_up()
        site.sign_up_page.enter_password("invalid_password")
        site.sign_up_page.enter_first_name("")
        assert site.sign_up_page.is_password_error_validation_message_displayed()

    @globo_cis
    def test_passwords_does_not_match_EE20_1687(self, site, data):
        site.transaction_flow.click_register_for_new_user_sign_up()
        site.sign_up_page.enter_confirm_password("invalid_password")
        site.sign_up_page.enter_password(data.user_password)
        assert site.sign_up_page.is_confirm_password_error_validation_message_displayed()

    @aldo
    def test_invalid_postal_code_EE20_1688(self, site, data):
        site.transaction_flow.click_register_for_new_user_sign_up()
        site.sign_up_page.enter_postal_code(data.shipping.invalid_postal_code)
        site.sign_up_page.enter_phone_number("")
        assert site.sign_up_page.is_postal_code_error_validation_message_displayed()

    @aldo
    def test_existing_user_sign_up_EE20_1689(self, site, data):
        site.transaction_flow.click_register_for_new_user_sign_up()
        site.sign_up_page.enter_email_address(data.user_email, new=False)
        site.sign_up_page.enter_first_name("")
        assert site.sign_in_page.is_show_password_button_displayed()

    def test_sign_in_at_checkout_page_EE20_1756(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.shipping_page.click_sign_in_link()
        site.sign_in_page.enter_user_name(data.user_email)
        site.sign_in_page.enter_password(data.user_password)
        site.sign_in_page.click_on_sign_in_button()
        assert data.user_email == site.shipping_page.get_user_email_text()




