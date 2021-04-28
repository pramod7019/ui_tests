from selenium.webdriver.common.by import By
from...Helpers.LocatorDatabase.Locators import Locators


class OrderHistoryPageElements(Locators):

    def __init__(self):
        Locators.__init__(self, "OrderHistoryPageLocators")

    def get_order_number_input_label(self):
        return self.get_page_element(By.XPATH, "orderNumberInputLabel")

    def get_postal_code_input_label(self):
        return self.get_page_element(By.XPATH, "postalCodeInputLabel")

    def get_track_order(self):
        return self.get_page_element(By.XPATH, "trackOrder")

    def get_order_number_tooltip(self):
        return self.get_page_element(By.XPATH, "orderNumberToolTip")

    def get_view_order_details(self):
        return self.get_page_element(By.XPATH, "viewOrderDetails")

    def get_order_load_more(self):
        return self.get_page_element(By.XPATH, "orderLoadMore")

    def get_return_click_here(self):
        return self.get_page_element(By.XPATH, "returnClickHere")

    def get_order_history_empty(self):
        return self.get_page_element(By.XPATH, "orderHistoryEmpty")

    def get_my_history(self):
        return self.get_page_element(By.XPATH, "myHistory")

    def get_order_number(self):
        return self.get_page_element(By.XPATH, "orderNumber")

    def get_order_details(self):
        return self.get_page_element(By.XPATH, "orderDetails")

    def get_orders(self):
        return self.get_page_element(By.CSS_SELECTOR, "orders")

