import pytest


@pytest.mark.general
@pytest.mark.regression
@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestGeneral:

    def test_to_verify_items_in_cart_are_moved_from_guest_to_sign_in_EE20_1836(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        site.cart_page.close_cart_page()
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_shopping_bag()
        assert site.page_title(data.cart_page_title)
        assert data.style_code in site.current_url()
