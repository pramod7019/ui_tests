import os, sys
import yaml, json
from .Tests.Testdata.TestData import json_to_obj
import subprocess
import ssl
import urllib.request
import urllib.error
import xml.etree.ElementTree as elemTree


class ConfigReader:

    @staticmethod
    def __get_config():
        dir = os.path.dirname(__file__)
        file = os.path.join(dir, 'configs.json')
        with open(file, 'r') as f:
            return json.load(f)

    def map_config(self):
        return json_to_obj(self.__get_config())

    def get_matched_chromedriver_version(self, version):
        if sys.platform == 'darwin':
          ssl._create_default_https_context = ssl._create_unverified_context
        doc = urllib.request.urlopen('https://chromedriver.storage.googleapis.com').read()
        root = elemTree.fromstring(doc)
        for k in root.iter('{http://doc.s3.amazonaws.com/2006-03-01}Key'):
           if k.text.find(self.get_major_version(version) + '.') == 0:
            return k.text.split('/')[0]
        return

    def get_major_version(self, version):
        return version.split('.')[0]

    def get_platform_architecture(self):
      if sys.platform.startswith('linux') and sys.maxsize > 2 ** 32:
        platform = 'linux'
        architecture = '64'
      elif sys.platform == 'darwin':
        platform = 'mac'
        architecture = '64'
      elif sys.platform.startswith('win'):
        platform = 'win'
        architecture = '32'
      else:
        raise RuntimeError('Could not determine chromedriver download URL for this platform.')
      return platform, architecture

    def get_chrome_browser_version(self):
      platform, _ = self.get_platform_architecture()
      if platform == 'linux':
        with subprocess.Popen(['chromium-browser', '--version'], stdout=subprocess.PIPE) as proc:
          version = proc.stdout.read().decode('utf-8').replace('Chromium', '').strip()
          version = version.replace('Google Chrome', '').strip()
      elif platform == 'mac':
        process = subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'],
                                   stdout=subprocess.PIPE)
        version = process.communicate()[0].decode('UTF-8').replace('Google Chrome', '').strip()
      elif platform == 'win':
        process = subprocess.Popen(
          ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
        )
        version = process.communicate()[0].decode('UTF-8').strip().split()[-1]
      else:
        return
      return version

    # @staticmethod
    # def get_banners():
    #      return ConfigReader.__get_config()["Configs"]["Banners"]
    #
    # @staticmethod
    # def ios_capabilities():
    #     return ConfigReader.__get_config()["Configs"]["IOSCapabilities"]
    #
    # @staticmethod
    # def appium_server():
    #     return ConfigReader.__get_config()["Configs"]["Appiumserver"]
    #
    # @staticmethod
    # def get_browser():
    #     return ConfigReader.__get_config()["Configs"]["Browser"]["browser"]
    #
    # @staticmethod
    # def get_chrome_version():
    #     return ConfigReader.__get_config()["Configs"]["Chromedriver_version"]
    #
    # @staticmethod
    # def get_environment():
    #     return ConfigReader.__get_config()["Configs"]["Environemnt"]


class Configuration(object):
  def __init__(self):
    self__config_reader = ConfigReader()
    self__config_map = self__config_reader.map_config()
    self.banners = self__config_map.banners
    self.ios_capabilities = IOSCapabilities(self__config_map.ios_capabilities)
    self.browser = self__config_map.browser
    if self.browser == "chrome" or "android":
        self.chrome_browser_version = self__config_reader.get_chrome_browser_version()
        self.chrome_version = self__config_reader.get_matched_chromedriver_version(self.chrome_browser_version)
    else:
        self.chrome_version = self__config_map.chrome_driver_version
    self.environment = self__config_map.environment
    self.aldo_banners = self__config_map.aldo_banners
    self.cis_banners = self__config_map.cis_banners
    self.globo_banners = self__config_map.globo_banners
    self.aldo_cis_banners = self__config_map.aldo_cis_banners
    self.aldo_globo_banners = self__config_map.aldo_globo_banners
    self.globo_cis_banners = self__config_map.globo_cis_banners
    self.aldo_us_banner = self__config_map.aldo_us_banner


class IOSCapabilities:
  def __init__(self, ioscaps):
    self.device = ioscaps.device
