import pytest
from .conftest import globo, aldo, cis, aldo_cis


@pytest.mark.footer
@pytest.mark.regression
@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestFooters:

    @aldo
    def test_footers_aldo_EE20_1757(self, site, data):
        site.header_page.wait_for_header_page()
        site.footerpage.verify_footers_aldo(data.links, data.urls)

    @cis
    def test_footers_cis_EE20_1757(self, site, data):
        site.header_page.wait_for_header_page()
        site.footerpage.verify_footers_cis(data.links, data.urls)

    @globo
    def test_footers_globo_EE20_1757(self, site, data):
        site.header_page.wait_for_header_page()
        site.footerpage.verify_footers_globo(data.links, data.urls)

    @aldo_cis
    def test_if_user_can_navigate_to_international_page_EE20_1760(self, site):
        site.header_page.wait_for_header_page()
        site.footerpage.click_all_countries_link()
        assert "international" in site.current_url()
        assert site.footerpage.verify_if_north_america_tab_is_displayed()

    @aldo_cis
    def test_if_user_can_navigate_to_country_EE20_1761(self, site):
        url_before_change = site.current_url()
        site.footerpage.change_country_link()
        assert url_before_change != site.current_url()
