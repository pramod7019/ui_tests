import pytest
from .conftest import globo_cis, aldo, aldo_cis, cis, aldo_globo, globo


@pytest.mark.filters
@pytest.mark.regression
@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestFilters:

    # applied size and colour filters
    @cis
    def test_cis_multiple_filters_EE20_1694(self, site, data):
        site.transaction_flow.open_filters_overlay(data.categories[0])
        site.filters_page.select_size_filter(data.filters.size_option)
        site.filters_page.select_colour_filter(data.filters.colour_option)
        site.filters_page.click_apply_filters_button()
        assert data.filters.applied in site.plp_page.get_no_of_filters_applied()
        assert data.filters.size_option and data.filters.colour_option in site.plp_page.get_cis_landing_header_text()

    # applied size and colour filters
    @aldo
    def test_aldo_multiple_filters_EE20_1694(self, site, data):
        site.transaction_flow.open_filters_overlay(data.categories[0])
        site.filters_page.select_size_filter(data.filters.size_option)
        site.filters_page.select_colour_filter(data.filters.colour_option)
        site.filters_page.click_hide_button()
        assert data.filters.applied in site.plp_page.get_no_of_filters_applied()
        assert data.filters.size_option and data.filters.colour_option in site.plp_page.get_applied_filters_text()

    # applied size and colour filters
    @globo
    def test_globo_multiple_filters_EE20_1694(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        site.filters_page.select_size_filter(data.filters.size_option)
        site.filters_page.select_colour_filter(data.filters.colour_option)
        assert data.filters.size_option and data.filters.colour_option in site.plp_page.get_applied_filters_text()

    @aldo
    def test_aldo_price_filter_EE20_1695(self, site, data):
        site.transaction_flow.open_filters_overlay(data.categories[0])
        site.filters_page.select_price_filter(data.filters.aldo_price_option)
        site.filters_page.click_hide_button()
        price_range = site.plp_page.get_applied_filters_text()[0]
        assert "1" in site.plp_page.get_no_of_filters_applied()
        assert site.plp_page.check_if_product_prices_are_in_applied_filter_range(price_range)

    @globo
    def test_globo_price_filter_EE20_1695(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        site.filters_page.select_price_filter(data.filters.price_option)
        price_range = site.plp_page.get_applied_filters_text()[0]
        assert site.plp_page.check_if_product_prices_are_in_applied_filter_range(price_range)

    @cis
    def test_cis_price_filter_EE20_1695(self, site, data):
        site.transaction_flow.open_filters_overlay(data.categories[0])
        site.filters_page.select_price_filter(data.filters.price_option)
        site.filters_page.click_apply_filters_button()
        assert "1" in site.plp_page.get_no_of_filters_applied()
        assert site.plp_page.check_if_product_prices_are_in_applied_filter_range(data.filters.price_option)

    @aldo_globo
    def test_sort_option_EE20_1696(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        site.plp_page.select_drop_down_value(data.filters.sort_option)
        site.plp_page.wait_for_plp_page()
        assert site.plp_page.check_if_product_prices_are_sorted_accordingly()

    @cis
    def test_cis_sort_filter_EE20_1696(self, site, data):
        site.transaction_flow.open_filters_overlay(data.categories[0])
        site.filters_page.select_cis_sort_option(data.filters.cis_sort_option)
        site.filters_page.click_apply_filters_button()
        assert site.plp_page.check_if_product_prices_are_sorted_accordingly()

    @cis
    def test_clear_filters_EE20_1697(self, site, data):
        site.transaction_flow.open_filters_overlay(data.categories[0])
        site.filters_page.select_colour_filter(data.filters.colour_option)
        applied_filters_text = site.filters_page.get_apply_filter_button_text()
        site.filters_page.click_clear_filters_button()
        cleared_filters_text = site.filters_page.get_apply_filter_button_text()
        assert applied_filters_text != cleared_filters_text

    @aldo_cis
    def test_close_filters_overlay_EE20_1698(self, site, data):
        site.transaction_flow.open_filters_overlay(data.categories[0])
        site.filters_page.click_close_filters_overlay()
        site.plp_page.is_plp_open()

    @aldo_cis
    def test_more_filter_options_EE20_1699(self, site, data):
        site.transaction_flow.open_filters_overlay(data.categories[0])
        before_clicking_more = site.filters_page.get_no_of_colour_options()
        site.filters_page.click_more_colours_button()
        after_clicking_more = site.filters_page.get_no_of_colour_options()
        assert after_clicking_more >= before_clicking_more


