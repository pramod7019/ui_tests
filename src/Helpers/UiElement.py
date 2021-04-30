import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from ..Helpers.Browser import Browser


class UiElement:

    def __init__(self, by, locators):

        self.by = by
        self.locator = locators

    def get_element(self, wait=20):

        self.wait_to_appear(wait)
        return Browser.get_driver().find_element(self.by, self.locator)

    def get_all_elements(self, wait=30):

        self.wait_to_appear(wait)
        return Browser.get_driver().find_elements(self.by, self.locator)

    def get_locator(self):

        return self.locator

    def get_text(self, encoding=None):

        text = self.get_element().text
        return text.encode(encoding) if encoding else text

    def get_attribute(self, value):

        return self.get_element().get_attribute(value)

    def is_selected(self):

        return self.get_element().is_selected()

    def displayed(self):

        self.wait_to_appear()
        try:
            WebDriverWait(Browser.get_driver(), 1).until(EC.visibility_of_element_located((self.by, self.locator)))
            return True
        except:
            return False

    def is_checked(self):

        return Browser.get_driver().execute_script("return arguments[0].checked;", self.get_element())

    def exists(self):

        try:
            WebDriverWait(Browser.get_driver(), 5).until(EC.presence_of_element_located((self.by, self.locator)))
            return True
        except:
            return False

    def is_clickable(self):

        def is_clickable(by, locator):
            try:
                WebDriverWait(Browser.get_driver(), 1).until(EC.element_to_be_clickable((by, locator)))
                return True
            except:
                return False

        return self.exists() and is_clickable(self.by, self.locator)

    def wait_to_be_clickable(self, seconds=15, ignore_error=False):

        start = time.time()
        while (time.time() - start) < seconds:
            if self.is_clickable():
                return self
            time.sleep(1)
        if not ignore_error:
            if self.exists():
                raise AssertionError("Locator in the DOM: {} but did not become click-able in {} seconds"
                                     .format(self.locator, seconds))
            raise AssertionError("Locator is not in the DOM and so not click-able: {}".format(self.locator))
        else:
            return self

    def wait_to_appear(self, seconds=30, ignore_error=False):

        start = time.time()
        while (time.time() - start) < seconds:
            if self.exists():
                return self
        if not ignore_error:
            raise AssertionError("Locator: {} did not appear in {} seconds!".format(self.locator, seconds))
        else:
            return self

    def wait_to_disappear(self, seconds=15, ignore_error=False):

        start = time.time()
        while (time.time() - start) < seconds:
            try:
                WebDriverWait(Browser.get_driver(), seconds).until(EC.invisibility_of_element_located((self.by, self.locator)))
            except Exception as error:
                if not ignore_error:
                    raise AssertionError("Locator: {} did not disappear in {} seconds! Error: {}"
                                         .format(self.locator, seconds, error))
        return self

    def click(self, wait=20, wait_for_clickable=True, use_action_chains=False):

        if wait_for_clickable:
            self.wait_to_be_clickable(wait)
        initial_handles = Browser.get_driver().window_handles

        if use_action_chains:
            ui_object = self.get_element()
            ActionChains(Browser.get_driver()).move_to_element(ui_object).click().perform()
        else:
            try:
                self.get_element().click()
            except Exception as error:
                # if "Other element would receive the click" in error:
                try:
                    self.scrollIntoCenter()
                    self.get_element().click()
                except:
                    raise error

        if len(Browser.get_driver().window_handles) > len(initial_handles):
            Browser.switch_to_latest_active_window()
        return self

    def set_text(self, value, loose_focus=False):

        self.get_element().clear()
        self.get_element().send_keys(str(value))
        if loose_focus:
            self.press_key(Keys.TAB)
        return self

    def scrollIntoCenter(self):

        scrollElementIntoMiddle = "var viewPortHeight = Math.max(document.documentElement.clientHeight, " \
                                  "window.innerHeight || 0); var elementTop = arguments[0].getBoundingClientRect().top;"\
                                  "window.scrollBy(0, elementTop-(viewPortHeight/2));"

        Browser.get_driver().execute_script(scrollElementIntoMiddle, self.get_element())

    def scrollIntoView(self):

        Browser.get_driver().execute_script("arguments[0].scrollIntoView()", self.get_element())
        return self

    def type_text(self, value):

        self.get_element().send_keys(value)
        return self

    def press_key(self, key, use_action_chains=False):

        if not use_action_chains:
            self.get_element().send_keys(key)
        else:
            chains = ActionChains(driver=Browser.get_driver())
            chains.send_keys(key).perform()
        return self

    def mouse_over(self):

        ui_object = self.get_element()
        ActionChains(Browser.get_driver()).move_to_element(ui_object).perform()
        return self

    def mouse_over_by_text(self, text):

        ui_objects = self.get_all_elements()
        for obj in ui_objects:
            if obj.text == text:
                ActionChains(Browser.get_driver()).move_to_element(obj).perform()
        return self

    def mobile_swipe_up(self):
        Browser.get_driver().execute_script("mobile: swipe", {"direction": "up"})
        return self

    def get_visible_element(self):
        self.wait_to_appear(seconds=15)
        ui_objects = self.get_all_elements()
        objects = []
        for obj in ui_objects:
            size = obj.size
            if size['height'] and size['width'] > 0:
                enabled = obj.is_enabled
                displayed = obj.is_displayed()
                if enabled and displayed:
                    objects.append(obj)
        return objects

    def select_drop_drown_value(self, value):
        Select(self.get_element()).select_by_value(value)

    def get_child_element(self, index):
        WebDriverWait(Browser.get_driver(), 5).until(EC.presence_of_all_elements_located((self.by, self.locator)))
        elements = self.get_all_elements()
        if len(elements) > index:
            return elements[index]
        else:
            raise AssertionError("size of elements is less than sent value {}".format(index))

    def click_child_element(self, index):
        try:
            self.wait_to_appear()
            self.get_child_element(index).click()
        except Exception as error:
            raise AssertionError("click action not performed because of {}".format(error))

    def get_text_of_child_elements(self):
        return [element.text for element in self.get_all_elements()]

    def get_attribute_of_child_elements(self, attribute):
        return [element.get_attribute(attribute) for element in self.get_all_elements()]

    def click_child_element_for_condition(self, attribute, given_option):
        for element in self.get_all_elements():
            if element.get_attribute(attribute) == given_option:
                Browser.get_driver().execute_script("arguments[0].click();", element)
                return self

    def child_elements_displayed(self):
        return [element.is_displayed() for element in self.get_all_elements()]

    def switch_to_iframe(self):
        self.wait_to_appear(seconds=20)
        Browser.switch_to_frame(Browser.get_driver().find_element(self.by, self.locator))

    @staticmethod
    def switch_to_default():
        Browser.switch_to_default()

    def switch_to_window(self):
        Browser.switch_to_latest_active_window()
        return self

    def js_click(self):
        Browser.get_driver().execute_script("arguments[0].click();", self.get_element())
        return self

    def set_text1(self, value, loose_focus=False):

        self.get_element().clear()
        self.get_element().send_keys(Keys.CONTROL + "a")
        self.get_element().send_keys(Keys.DELETE)
        self.get_element().send_keys(str(value))
        if loose_focus:
            self.press_key(Keys.TAB)
        return self

    def get_selected_option(self):
        return Select(self.get_element()).first_selected_option.text

    def get_all_options(self):
        return [element.get_attribute("value") for element in Select(self.get_element()).options]



