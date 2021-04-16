import time
import pytest

from uitests.src.Helpers.Browser import Browser
from uitests.src.Tests.Desktop.conftest import aldo, aldo_globo, cis, skip_for_prod, globo_cis, globo


@pytest.mark.mobile
@pytest.mark.regression
@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestSmoke:

    def test_if_promotion_message_is_displayed_on_home_page_header(self, site):
        assert site.header_page.is_promotion_message_displayed()

    def test_if_product_name_is_displayed_on_pdp(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_menu_mobile(data.categories[1], 0, data.level1_categories[0],
                                                              data.footwear_categories[0])
        assert site.pdp_page.get_product_name()

    def test_selecting_size_on_pdp(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_menu_mobile(data.categories[1], 0, data.level1_categories[0],
                                                              data.footwear_categories[0])
        size_to_select = site.pdp_page.select_size(0)
        size_selected = site.pdp_page.size_selected()
        assert size_to_select == size_selected

    def test_if_product_prices_displayed_on_pdp(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_menu_mobile(data.categories[1], 0, data.level1_categories[0],
                                                              data.footwear_categories[0])
        prices = site.pdp_page.get_displayed_prices()
        for price in prices:
            assert price.startswith(data.currency)

    def test_if_reassurance_links_displayed_on_pdp(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_menu_mobile(data.categories[1], 0, data.level1_categories[0],
                                                              data.footwear_categories[0])
        assert site.pdp_page.get_reassurance_links()

    def test_selecting_colour_on_pdp(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_menu_mobile(data.categories[1], 0, data.level1_categories[0],
                                                              data.footwear_categories[0])
        colour_to_select = site.pdp_page.select_colour(0)
        colour_selected = site.pdp_page.colour_selected()
        assert colour_to_select == colour_selected

    def test_empty_shopping_bag(self, site, data):
        site.header_page.click_shopping_bag_mobile()
        assert site.cart_page.is_cart_title_displayed()
        assert site.page_title(data.cart_page_title)

    def test_if_all_product_names_are_present_on_plp_page(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation_mobile(data.categories[1], data.level1_categories[0],
                                                                              data.footwear_categories[0])
        products = site.plp_page.get_plp_products()
        product_names = site.plp_page.get_plp_products_names()
        assert len(products) == len(product_names)

    def test_if_all_product_prices_are_present_on_plp_page(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation_mobile(data.categories[1], data.level1_categories[0],
                                                                              data.footwear_categories[0])
        products = site.plp_page.get_plp_products()
        product_prices = site.plp_page.get_plp_product_prices()
        assert len(products) == len(product_prices)

    def test_if_currency_symbol_is_present_in_product_prices_on_plp(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation_mobile(data.categories[1], data.level1_categories[0],
                                                                              data.footwear_categories[0])
        product_prices = site.plp_page.get_plp_product_prices()
        for price in product_prices:
            assert price.startswith(data.currency) or price == "Sold out"

    @aldo
    def test_if_product_tags_are_displayed_on_plp_page(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation_mobile(data.categories[1], data.level1_categories[0],
                                                                              data.footwear_categories[0])
        assert site.plp_page.are_product_tags_displayed()

    @aldo
    def test_if_product_labels_are_displayed_on_plp_page(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation_mobile(data.categories[1], data.level1_categories[0],
                                                                              data.footwear_categories[0])
        assert site.plp_page.are_product_labels_displayed()

    def test_if_cart_id_displayed_in_cart(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code, mobile=True)
        assert site.cart_page.is_cart_id_displayed()

    def test_remove_product_from_cart(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code, mobile=True)
        assert site.page_title(data.cart_page_title)
        site.cart_page.remove_product_from_cart(0)
        assert site.cart_page.is_empty_cart_title_displayed()

    def test_edit_size_in_cart(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code, mobile=True)
        site.cart_page.click_on_edit_product(0)
        size_to_select = site.cart_page.select_product_size(1)
        site.cart_page.click_on_save_edits()
        size_selected = site.cart_page.get_displayed_size()
        assert size_to_select in size_selected

    def test_edit_colour_in_the_cart(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code, mobile=True)
        edited_colour = site.transaction_flow.edit_item_colour_in_cart(0, 0)
        displayed_colour = site.cart_page.get_displayed_product_colour_in_cart()
        assert displayed_colour in edited_colour

    def test_load_more_products_on_plp(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation_mobile(data.categories[1], data.level1_categories[0],
                                                                              data.footwear_categories[0])
        site.plp_page.is_plp_open()
        assert site.plp_page.click_view_all_and_verify_product_count()

    def test_edit_cart_qty(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code, mobile=True)
        site.transaction_flow.edit_item_quantity_in_cart(0, "2")
        assert "2" in site.cart_page.get_title_text()

    @aldo_globo
    def test_favourites_icon_on_home_page_header(self, site):
        site.header_page.click_favourites_icon_mobile()
        assert "favourites" in site.current_url()

    @cis
    def test_favourites_icon_on_home_page_header_cis(self, site):
        site.header_page.click_on_main_nav_mobile()
        site.header_page.click_favourites_icon_mobile()
        assert "favourites" in site.current_url()

    def test_search_on_home_page_header(self, site, data):
        site.header_page.click_search_button()
        site.header_page.enter_search_keyword_mobile(data.search_keyword)
        site.header_page.select_from_search_suggestion()
        assert site.page_title(data.search_page_title)
        assert site.plp_page.get_plp_products_names()

    def test_user_login(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.header_page.click_on_main_nav_mobile()
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.header_page.click_on_main_nav_mobile()
        assert "account" in site.header_page.mobile_user_account_href()
        site.transaction_flow.user_logout()
        assert data.logged_out_message in site.header_page.get_header_message_bar_text()

    @skip_for_prod
    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_guest_checkout_order_credit_card(self, site, data, shipping_method):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code, mobile=True)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_for_guest(shipping_method, data.shipping)
        site.shipping_page.click_on_continue_payment_button()
        site.transaction_flow.credit_card_payment(data.creditcard[0])
        site.payment_page.click_review_order()
        site.review_page.click_on_place_order("credit card")
        assert site.confirmation_page.verify_confirmation_heading()

    def test_if_user_can_change_the_country_language(self, site):
        url_before_change = site.current_url()
        site.header_page.click_on_main_nav_mobile()
        site.header_page.change_country_language()
        assert url_before_change != site.current_url()

    @skip_for_prod
    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_sign_in_user_in_checkout(self, site, data, shipping_method):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.header_page.click_on_main_nav_mobile()
        site.transaction_flow.user_login(data.user_email, data.user_password)
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code, mobile=True)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        site.transaction_flow.fill_shipping_for_sign_in_user(shipping_method, data.shipping,Browser.get_current_url())
        site.shipping_page.click_on_continue_payment_button()
        site.payment_page.select_credit_card_payment()
        site.transaction_flow.credit_card_payment(data.creditcard[0])
        site.payment_page.click_review_order()
        site.review_page.click_on_place_order("credit card")
        assert site.confirmation_page.verify_confirmation_heading()
        site.header_page.click_on_main_nav_mobile()
        site.transaction_flow.user_logout()
        assert data.logged_out_message in site.header_page.get_header_message_bar_text()

    def test_if_all_links_are_displayed_on_sign_in_overlay(self, site):
        site.header_page.click_on_main_nav_mobile()
        site.header_page.click_on_my_account()
        assert site.sign_in_page.is_show_password_button_displayed()


