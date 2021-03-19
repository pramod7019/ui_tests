import re
import pytest
from uitests.src.Tests.Desktop.conftest import aldo
from .test_signup import TestLoginFlow


@pytest.mark.promoandtaxes
@pytest.mark.regression
@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestPromos:

    def test_apply_promo_in_cart_EE20_1690(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        cart_value_before_promo = site.cart_page.get_cart_sub_total_value()
        site.cart_page.apply_promo(data.promo_code)
        discount = site.cart_page.get_cart_discount_total()
        cart_value_after_promo = site.cart_page.get_cart_total_value()
        assert cart_value_after_promo == round((cart_value_before_promo + discount), 2)

    @aldo
    def test_shipping_method_in_cart_EE20_1691(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        cart_value_with_default_shipping = site.cart_page.get_cart_sub_total_value()
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.shipping_page.select_shipping_method("aldo-mc-free-ship-to-store-net")
        subtotal = site.summary_page.get_subtotal_checkout_amount()
        ship_charge = site.shipping_page.standard_shipping_price_text().get_text().split('\n')[1]
        default_ship_charge = '$0.0' if ship_charge.lower() == "free" else ship_charge
        assert round((cart_value_with_default_shipping - subtotal), 2) == \
               round(float(re.sub("\$", '', default_ship_charge)), 2)

    def test_apply_promo_taxes_in_checkout_EE20_1692(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.summary_page.apply_Taxes(data.shipping.postal_code)
        site.summary_page.apply_promo(data.promo_code)
        subtotal = site.summary_page.get_subtotal_checkout_amount()
        promo = site.summary_page.get_promo_checkout_amount()
        tax = site.summary_page.get_total_tax_amount()
        cart_value_after_tax = site.summary_page.get_total_cart_amount()
        shipping_charge = site.shipping_page.standard_shipping_price_text().get_text().split('\n')[1]
        ship_total = 0.0 if shipping_charge.lower() == "free" else float(re.sub("\$", '', shipping_charge))
        assert cart_value_after_tax == round((subtotal + promo + tax + ship_total), 2)

    @aldo
    def test_apply_aldo_crew_coupon_EE20_1693(self, site, data):
        TestLoginFlow.test_aldo_crew_sign_up_EE20_1682(self, site, data)
        site.transaction_flow.add_product_to_cart_from_home_search(data.style_code)
        assert site.page_title(data.cart_page_title)
        site.cart_page.remove_any_applied_promos()
        site.cart_page.close_cart_page()
        site.header_page.click_user_account()
        site.my_account_page.click_redeem_offer()
        site.header_page.click_shopping_bag()
        site.cart_page.close_cart_page()
        site.transaction_flow.user_logout()
        assert data.logged_out_message in site.header_page.get_header_message_bar_text()

