import datetime
import threading
import time

from selenium.webdriver.chrome.options import Options as chromeoptions
from selenium import webdriver
from seleniumwire import webdriver as wiredriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from uitests.src.ConfigReader import ConfigReader, Configuration
from appium import webdriver as appiumdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os, sys
from uitests.src.ConfigReader import Configuration
from pathlib import Path


class Browser:

    CHROME = 1
    FF = 2
    SAFARI = 3
    REMOTE = 4
    MOBILE = 5
    ANDROID = 6
    __CONFIGS = Configuration()
    __DRIVER_MAP = {}

    @staticmethod
    def create_new_driver(driver_id):

        thread_object = threading.currentThread()

        def get_driver():
            if Browser.SAFARI == driver_id:
                driver = webdriver.Safari

            elif Browser.CHROME == driver_id:
                driver = wiredriver.Chrome(ChromeDriverManager(version=Browser.__CONFIGS.chrome_version).install(),
                                           seleniumwire_options={'verify_ssl': False})
                driver.header_overrides = {
                  "Aldo-Access": "UAT",
                  "User-Agent": "SOASTA"
                }

            elif Browser.FF == driver_id:
                driver = webdriver.Firefox(GeckoDriverManager().install())


            elif Browser.REMOTE == driver_id:
                driver = webdriver.Remote(command_executor='')

            elif Browser.MOBILE == driver_id:
                driver = wiredriver.Remote(command_executor='http://localhost:4723/wd/hub',
                                           desired_capabilities=Browser.__ios_desired_caps())
                driver.header_overrides = {
                    "Aldo-Access": "UAT"
                }
            elif Browser.ANDROID == driver_id:
                # driver = appiumdriver.Remote(command_executor='http://localhost:4723/wd/hub',
                #                            desired_capabilities=Browser.__android_desired_caps())
                mobile_emulation = {"deviceName": "Pixel 2 XL"}
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
                driver = wiredriver.Chrome(ChromeDriverManager(version=Browser.__CONFIGS.chrome_version).install(),
                                                            desired_capabilities=chrome_options.to_capabilities())
                driver.header_overrides = {
                  "Aldo-Access": "UAT"
                }
            else:
                raise Exception("There is no support for driver_id: {}".format(driver_id))

            if driver_id != Browser.MOBILE:
                print ("driver")
                # driver.delete_all_cookies()
                driver.maximize_window()
            return driver

        Browser.__map(thread_object, get_driver())
        return Browser.get_driver()

    @staticmethod
    def get_driver():
        print ("Getting  driver for thread: {}".format(threading.currentThread()))
        return Browser.__DRIVER_MAP[threading.current_thread()]["driver"]

    @staticmethod
    def shutdown():
        Browser.get_driver().quit()

    @staticmethod
    def __map(thread, driver):
        Browser.__DRIVER_MAP[thread] = {"driver": driver}

    @staticmethod
    def get_driver_map():
        return Browser.__DRIVER_MAP

    @staticmethod
    def back():
        Browser.get_driver().back()

    @staticmethod
    def wait_for_page_title(title):
         return WebDriverWait(Browser.get_driver(), 20).until(EC.title_contains(title))

    @staticmethod
    def forward():
        Browser.get_driver().forward()

    @staticmethod
    def open_new_tab():
        Browser.get_driver().find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

    @staticmethod
    def switch_to_window(window):
        Browser.get_driver().switch_to_window(window)

    @staticmethod
    def switch_to_frame(frame):
        Browser.get_driver().switch_to.frame(frame)

    @staticmethod
    def switch_to_default():
        Browser.get_driver().switch_to.default_content()

    @staticmethod
    def switch_to_latest_active_window():
        windows = Browser.get_driver().window_handles
        if len(windows) == 1:
            Browser.get_driver().switch_to_window(windows[0])
            return
        for index in range(1, len(windows)):
            Browser.get_driver().switch_to_window(windows[-index])
            return

    @staticmethod
    def close_current_active_window():
        windows = Browser.get_driver().window_handles
        if len(windows) == 1:
            return
        for index in range(1, len(windows)):
            Browser.get_driver().close()
            Browser.switch_to_latest_active_window()
            return

    @staticmethod
    def __get_chrome_options():
        chrome_options = chromeoptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--ignore-certificate-errors')
        if Browser.__CONFIGS.get_browser()["headless"]:
            chrome_options.add_argument("--headless")
            # chrome_options.add_argument("window-size=1936,1056")
        return chrome_options

    @staticmethod
    def __ios_desired_caps():
        desired_caps = {
            "platformName":"iOS",
            "platformVersion": Browser.__CONFIGS.ios_capabilities()["version"],
            "automationName":"xcuitest",
            "deviceName":Browser.__CONFIGS.ios_capabilities()["iphone"],
            "browserName":Browser.__CONFIGS.ios_capabilities()["browser"],
            "isHeadless":Browser.__CONFIGS.ios_capabilities()["headless"],
            "noReset":Browser.__CONFIGS.ios_capabilities()["resetsim"]
        }
        return desired_caps

    @staticmethod
    def __android_desired_caps():
        desired_caps = {
                "platformName": "Android",
                "platformVersion": "10.0",
                "automationName": "Appium",
                "appActivity":"com.google.android.apps.chrome.Main",
                "appPackage":"com.android.chrome",
                "deviceName": "Pixel_XL_API_29",
                "browerName": "Chrome",
                'chromeOptions': {
                        'args': ['--no-first-run']
                        }
            }
        return desired_caps

    @staticmethod
    def get_current_url():
        WebDriverWait(Browser.get_driver(), 20).until(EC.url_changes)
        return Browser.get_driver().current_url

    @staticmethod
    def take_screenshot(test_name):
        file_name = "{}-{}.png".format(test_name, Browser.get_current_time())
        file_path = os.path.join(Browser.get_screenshots_dir(), file_name)
        Browser.get_driver().save_screenshot(file_path)
        return file_path

    @staticmethod
    def get_current_time():
        date_time_obj = datetime.datetime.now()
        return date_time_obj.strftime("%d%b%Y-%H%M%S")

    @staticmethod
    def config():
        configuration = Configuration()
        return configuration

    @staticmethod
    def switch_to_new_window_and_get_url(wait_time=20):
        old_url = Browser.get_current_url()
        Browser.switch_to_latest_active_window()
        start = time.time()
        while (time.time() - start) < wait_time:
          if old_url != Browser.get_current_url():
            break
          else:
            Browser.switch_to_latest_active_window()
        return Browser.get_current_url()

    @staticmethod
    def get_screenshots_dir():
        dir = 'Screenshots/'
        if sys.platform == "darwin":
            root_dir = os.path.join(Path.home(), dir)
        else:
            path = Path(sys.executable)
            root_dir = os.path.join(path.root, dir)
        sub_dir = 'Screenshots' + datetime.datetime.now().strftime("%d%b%Y")
        full_path = os.path.join(root_dir, sub_dir)
        if not os.path.exists(root_dir):
          os.mkdir(root_dir)
        if not os.path.exists(full_path):
          os.mkdir(full_path)
        return full_path

