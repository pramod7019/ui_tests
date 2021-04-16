import pytest

from uitests.src.Helpers.Browser import Browser
from .conftest import skip_for_prod, aldo, globo_cis


@pytest.mark.flaky(max_runs=3, min_passes=1)
@pytest.mark.usefixtures('setup', 'data')
class TestSmoke:

    @skip_for_prod
    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_guest_checkout_order_creditcard_EE20_904 (self, site, data, shipping_method):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_for_guest(shipping_method, data.shipping)
        site.shipping_page.click_on_continue_payment_button()
        site.transaction_flow.credit_card_payment(data.creditcard[0])
        site.payment_page.click_review_order()
        site.review_page.click_on_place_order("credit card")
        assert site.confirmation_page.is_cart_id_displayed()

    def test_if_product_name_is_displayed_on_pdp_EE20_924(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_menu(data.categories[0], 0)
        assert site.pdp_page.get_product_name()

    def test_selecting_size_on_pdp_EE20_923(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_menu(data.categories[0], 1)
        size_to_select = site.pdp_page.select_size(0)
        size_selected = site.pdp_page.size_selected()
        assert size_to_select == size_selected

    def test_selecting_colour_on_pdp_EE20_922(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_search(data.style_code)
        colour_to_select = site.pdp_page.select_colour(0)
        colour_selected = site.pdp_page.colour_selected()
        assert colour_to_select == colour_selected

    def test_if_product_prices_displayed_on_pdp_EE20_925(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_menu(data.categories[0], 0)
        prices = site.pdp_page.get_displayed_prices()
        for price in prices:
            assert price.startswith(data.currency)

    def test_if_reassurance_links_displayed_on_pdp_EE20_926(self, site, data):
        site.transaction_flow.go_to_pdp_from_home_menu(data.categories[0], 0)
        assert site.pdp_page.get_reassurance_links()

    def test_remove_product_from_cart_EE20_927(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.remove_product_from_cart(0)
        assert site.cart_page.is_empty_cart_title_displayed()

    def test_edit_size_in_cart_EE20_928(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        site.cart_page.click_on_edit_product(0)
        size_to_select = site.cart_page.select_product_size(1)
        site.cart_page.click_on_save_edits()
        size_selected = site.cart_page.get_displayed_size()
        assert size_to_select in size_selected

    def test_if_cart_id_displayed_in_cart_EE20_931(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.cart_page.is_cart_id_displayed()

    def test_edit_cart_qty_EE20_929(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        site.transaction_flow.edit_item_quantity_in_cart(0, "2")
        assert "2" in site.cart_page.get_title_text()

    @skip_for_prod
    def test_user_login_EE20_902(self, site, data):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        site.transaction_flow.user_logout()
        assert data.logged_out_message in site.header_page.get_header_message_bar_text()

    def test_if_all_links_are_displayed_on_sign_in_overlay_EE20_903(self, site):
        site.header_page.click_on_my_account()
        assert site.sign_in_page.is_show_password_button_displayed()

    @skip_for_prod
    @pytest.mark.parametrize('shipping_method', (["Standard"]))
    def test_sign_in_user_in_checkout_EE20_905(self, site, data, shipping_method):
        site.execute_command(data.feature_toggle.deactivate_force_recaptcha)
        site.transaction_flow.user_login(data.user_email, data.user_password)
        assert "account" in site.header_page.user_account_href()
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        site.transaction_flow.fill_shipping_for_sign_in_user(shipping_method, data.shipping,Browser.get_current_url())
        site.shipping_page.click_on_continue_payment_button()
        site.payment_page.select_credit_card_payment()
        site.transaction_flow.credit_card_payment(data.creditcard[0])
        site.payment_page.click_review_order()
        site.review_page.click_on_place_order("credit card")
        assert site.confirmation_page.is_cart_id_displayed()
        site.transaction_flow.user_logout()
        assert data.logged_out_message in site.header_page.get_header_message_bar_text()

    def test_search_on_home_page_header_EE20_906(self, site, data):
        site.header_page.click_search_button()
        site.header_page.enter_search_keyword(data.search_keyword)
        site.header_page.select_from_search_suggestion()
        assert site.page_title(data.search_page_title)
        assert site.plp_page.get_plp_products_names()

    def test_favourites_icon_on_home_page_header_EE20_908(self, site):
        site.header_page.click_favourites_icon()
        assert "favourites" in site.current_url()

    def test_empty_shopping_bag_EE20_909(self, site, data):
        site.header_page.click_shopping_bag()
        assert site.cart_page.is_cart_title_displayed()
        assert site.page_title(data.cart_page_title)

    @aldo
    @globo_cis
    def test_if_user_can_change_the_country_language_EE20_910(self, site):
        url_before_change = site.current_url()
        site.header_page.change_country_language()
        assert url_before_change != site.current_url()

    def test_if_promotion_message_is_displayed_on_home_page_header_EE20_911(self, site):
        assert site.header_page.is_promotion_message_displayed()

    def test_if_all_product_names_are_present_on_plp_page_EE20_917(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        products = site.plp_page.get_plp_products()
        product_names = site.plp_page.get_plp_products_names()
        assert len(products) == len(product_names)

    def test_if_all_product_prices_are_present_on_plp_page_EE20_918(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        products = site.plp_page.get_plp_products()
        product_prices = site.plp_page.get_plp_product_prices()
        assert len(products) == len(product_prices)

    def test_if_currency_symbol_is_present_in_product_prices_on_plp_EE20_919(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        product_prices = site.plp_page.get_plp_product_prices()
        for price in product_prices:
            assert price.startswith(data.currency) or price == "Sold out"

    @aldo
    def test_if_product_labels_are_displayed_on_plp_page_EE20_921(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        assert site.plp_page.are_product_labels_displayed()

    @aldo
    def test_if_product_tags_are_displayed_on_plp_page_EE20_920(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        assert site.plp_page.are_product_tags_displayed()

    def test_edit_colour_in_the_cart_EE20_930(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        edited_colour = site.transaction_flow.edit_item_colour_in_cart(0, 0)
        displayed_colour = site.cart_page.get_displayed_product_colour_in_cart()
        assert displayed_colour in edited_colour

    def test_load_more_products_on_plp_EE20_1747(self, site, data):
        site.transaction_flow.go_to_plp_page_from_home_page_navigation(data.categories[0])
        site.plp_page.is_plp_open()
        assert site.plp_page.click_view_all_and_verify_product_count()





