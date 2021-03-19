import pytest, time


@pytest.mark.flaky(max_runs=1, min_passes=1)
@pytest.mark.usefixtures('setup', 'data')
class TestAddToBag:

    def test_add_to_bag(self, site, data):
        site.transaction_flow.add_product_to_cart_from_home_search(data.categories[0], 0)
        assert site.page_title(data.cart_page_title)
        site.cart_page.click_on_start_checkout()
        assert site.page_title(data.checkout_page_title)
        site.transaction_flow.fill_shipping_for_guest(0, data.shipping)
        site.shipping_page.click_on_continue_payment_button()
        site.transaction_flow.credit_card_payment(data.creditcard[0])
        site.payment_page.click_review_order()
        site.review_page.click_on_place_order("credit card")
        assert site.confirmation_page.is_cart_id_displayed()




