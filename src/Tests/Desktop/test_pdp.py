import pytest
from .conftest import aldo_cis, aldo_us


@pytest.mark.pdp
@pytest.mark.regression
@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestPDP:

    @aldo_cis
    def test_size_chart_EE20_1709(self, site, data):
        results = ["false", "true", "true", "false"]
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        assert results == site.pdp_page.size_chart_flow()

    def test_find_in_store_EE20_1708(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        site.pdp_page.select_size(1)
        assert site.pdp_page.fill_store_with_data(data.shipping)

    def test_product_carousel_EE20_1741(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        site.pdp_page.click_and_verify_selected_thumbnail()

    def test_if_product_is_zoomed_EE20_1740(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        site.pdp_page.click_on_preview()
        site.pdp_page.click_zoom_preview_btn()
        assert site.pdp_page.verify_if_image_close_button_is_displayed()
        assert site.pdp_page.verify_if_arrow_controls_are_displayed()
        assert site.pdp_page.verify_if_carousel_indicators_are_displayed()

    def test_bread_crumb_EE20_1742(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        bread_crumb_text = site.pdp_page.bread_crumb_text(1)
        site.pdp_page.click_bread_crumb(1)
        assert bread_crumb_text or "trends" in site.current_url()
        site.plp_page.is_plp_open()

    @aldo_us
    def test_paypal_credit_message(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_disable_paypal_credit)
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        assert site.pdp_page.verify_if_paypal_credit_message_is_displayed()
