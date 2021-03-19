import pytest
from .conftest import globo_cis, aldo


@pytest.mark.wishlist
@pytest.mark.regression
@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestWishList:

    @aldo
    def test_add_to_wish_list_from_plp_page_aldo_EE20_1668(self,site,data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        site.plp_page.click_favourite_icon(1)
        assert site.header_page.get_wishlist_count_aldo() == 1

    @globo_cis
    def test_add_to_wish_list_from_plp_page_globo_cis_EE20_1668(self,site,data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        site.plp_page.click_favourite_icon(1)
        assert site.header_page.get_wishlist_count() == 1

    @aldo
    def test_add_to_wish_list_from_pdp_page_aldo_EE20_1669(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        site.pdp_page.click_on_favourite_icon()
        assert site.header_page.get_wishlist_count_aldo() == 1

    @globo_cis
    def test_add_to_wish_list_pdp_page_globo_cis_EE20_1669(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        site.pdp_page.click_on_favourite_icon()
        assert site.header_page.get_wishlist_count() == 1

    def test_add_to_bag_from_wish_list_EE20_1671(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        site.pdp_page.click_on_favourite_icon()
        site.header_page.click_wishlist()
        site.fav_page.click_on_primary()
        site.fav_page.select_size(1)
        site.fav_page.click_on_secondary()
        assert site.page_title(data.cart_page_title)

    def test_move_to_wish_list_from_cart_EE20_1672(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_move_to_favourites()
        site.cart_page.close_cart_page()
        site.header_page.click_wishlist()
        assert site.fav_page.verify_product_thumbnail_is_displayed()

    def test_if_pop_up_is_displayed_for_guest_user_EE20_1675(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        site.plp_page.click_favourite_icon(1)
        site.plp_page.click_favourite_icon(2)
        assert site.plp_page.verify_if_pop_up_is_displayed()

    @aldo
    def test_sign_in_user_favourites_aldo_EE20_1674(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        site.fav_page.remove_from_favourites_aldo(site)
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        site.pdp_page.click_on_favourite_icon()
        site.transaction_flow.user_logout()
        assert data.logged_out_message in site.header_page.get_header_message_bar_text()
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        assert site.header_page.get_wishlist_count_aldo() == 1

    @globo_cis
    def test_sign_in_user_favourites_globo_cis_EE20_1676(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        site.fav_page.remove_from_favourites(site)
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        site.pdp_page.click_on_favourite_icon()
        site.transaction_flow.user_logout()
        assert data.logged_out_message in site.header_page.get_header_message_bar_text()
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        assert site.header_page.get_wishlist_count() == 1

    def test_clicking_on_product_tile_redirects_to_PDP_EE20_1714(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        site.plp_page.click_favourite_icon(1)
        site.header_page.click_favourites_icon()
        site.fav_page.click_product_thumbnail()
        assert site.pdp_page.verify_if_size_chart_link_is_displayed()




