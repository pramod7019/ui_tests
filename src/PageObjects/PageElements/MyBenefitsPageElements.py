import self as self
from selenium.webdriver.common.by import By
from...Helpers.LocatorDatabase.Locators import Locators

class MyBenefitsPageElements(Locators):

  def __init__(self)
   Locators.__init__(self,"MyBenefitsPageLocators")

  def get_aldo_crew_welcome_coupon(self):
    return self.get_page_element(By.XPATH,"aldoCrewWelcomeCoupon")
