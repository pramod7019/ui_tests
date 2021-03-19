import pytest
from .conftest import globo_cis, aldo, aldo_cis, cis, aldo_globo, globo, aldo_us


@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestOrderHistory:

    @aldo
    @aldo_us
    def test_user_order_details_aldo(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.order_history_page.click_my_history()
        verify_order_number = site.order_history_page.get_order_number()
        site.order_history_page.click_view_order_details()
        assert verify_order_number in site.current_url()

    @globo_cis
    def test_user_order_details(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_user_account()
        site.order_history_page.click_my_history()
        assert site.order_history_page.verify_order_detail()


