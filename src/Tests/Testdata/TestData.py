import os
import json
from collections import namedtuple
import datetime


class TestDataJSONObj:
  def __init__(self, banner, environment):
    self.__banner = banner
    self.__environment = environment

  def __load_file(self):
    data_file = os.path.dirname(os.path.abspath(__file__))
    env_dir = os.path.join(data_file, self.__environment)
    file_path = os.path.join(env_dir, self.__banner + '.json')
    return file_path

  def data(self):
    with open(self.__load_file()) as f:
      data = json.load(f)
    return data


def json_to_obj(d):
  for k, v in d.items():
    if isinstance(v, dict):
      d[k] = json_to_obj(v)
  return namedtuple('object', d.keys())(*d.values())


class TestData:
  def __init__(self, data_obj):
    self._data = data_obj
    self.product_url = self._data.ProductUrl
    self.user_email = self._data.Login_User.Email
    self.user_password = self._data.Login_User.Password
    self.logged_out_message = self._data.Login_User.LogoutMessage
    self.sign_up_message = self._data.Login_User.SignUpMessage
    self.shipping = Shipping(data_obj.Shipping)
    self.categories = self._data.Categories
    self.level1_categories = self._data.CategoriesLevel1
    self.footwear_categories = self._data.FootwearCategoriesLevel2
    self.creditcard = self._data.Payment.Creditcard
    self.home_page_title = self._data.PageTitle.HomePage
    self.cart_page_title = self._data.PageTitle.CartPage
    self.checkout_page_title = self._data.PageTitle.CheckoutPage
    self.search_page_title = self._data.PageTitle.SearchPage
    self.search_keyword = self._data.SearchKeyword
    self.style_code = self._data.StyleCode
    self.currency = self._data.Currency
    self.user_details = UserDetails()
    self.filters = FiltersData()
    self.feature_toggle = FeatureToggle()
    self.paypal = self._data.Payment.Paypal
    if getattr(self._data.Payment, "PaypalCredit",0) != 0:
        self.paypal_credit = self._data.Payment.PaypalCredit
    self.visa_checkout = self._data.Payment.Visacheckout
    self.promo_code = self._data.PromoCode
    self.uat_login = LoginData()
    self.urls = Urls(data_obj.Urls)
    self.links = LinkText(data_obj.Links)
    self.orderurl = self._data.orderurl


class Shipping:
  def __init__(self, shipping_obj):
    self._shipping = shipping_obj
    self.method = self._shipping.Method
    self.email = self._shipping.Email
    self.first_name = self._shipping.Firstname
    self.last_name = self._shipping.Lastname
    self.street = self._shipping.Street
    self.suite = self._shipping.Suite
    self.city = self._shipping.City
    self.postal_code = self._shipping.Postalcode
    self.phone = self._shipping.Phonenumber
    self.extension = self._shipping.Extension
    self.invalid_postal_code = self._shipping.Invalidpostalcode
    self.standard_charges = self._shipping.Standardcharges
    self.country = self._shipping.Country


class UserDetails:
  def __init__(self):
    date = datetime.datetime.now()
    self.dob_date = date.strftime("%d")
    self.dob_month = date.strftime("%m")
    self.dob_year = str(date.year - 20)


class FiltersData:
  def __init__(self):
    self.applied = "2"
    self.size_option = "6"
    self.colour_option = "Black"
    self.aldo_price_option = "$25 - $49.99"
    self.price_option = "$20 - $39.99"
    self.sort_option = "price-asc"
    self.cis_sort_option = "Price (low to high)"


class FeatureToggle:
  def __init__(self):
    self.deactivate_force_recaptcha = "window.ABTest.deactivateFeature('forceRecaptcha')"
    self.deactivate_verify_recaptcha = "window.ABTest.deactivateFeature('verifyRecaptcha')"
    self.deactivate_disable_paypal_credit = "window.ABTest.deactivateFeature('disablePaypalCredit')"
    self.deactivate_hide_shipping_method = "window.ABTest.deactivateFeature('hideshippingmethod')"

class LoginData:
  def __init__(self):
    self.email_id = "qa.automation.uat@gmail.com"
    self.password = "Aldo1234"


class Urls:
  def __init__(self, urls_obj):
    self._urls = urls_obj
    self.appointments = self._urls.Appointments
    self.store_locator = self._urls.StoreLocator
    self.gift_cards = self._urls.GiftCards
    self.track_order = self._urls.TrackOrder
    self.contact_us = self._urls.ContactUs
    self.returns = self._urls.Returns
    self.customer_service = self._urls.CustomerService
    self.about_us = self._urls.AboutUs
    self.opportunities = self._urls.Opportunities
    self.aldo_group = self._urls.AldoGroup
    self.kindaf = self._urls.KindAf


class LinkText:
  def __init__(self, links_obj):
    self._links = links_obj
    self.appointments = self._links.Appointments
    self.store_locator = self._links.StoreLocator
    self.gift_cards = self._links.GiftCards
    self.track_order = self._links.TrackOrder
    self.contact_us = self._links.ContactUs
    self.returns = self._links.Returns
    self.customer_service = self._links.CustomerService
    self.about_us = self._links.AboutUs
    self.opportunities = self._links.Opportunities
    self.aldo_group = self._links.AldoGroup
    self.kindaf = self._links.KindAf
