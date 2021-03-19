from urllib.parse import urljoin
from uitests.src.Helpers.Browser import Browser
from ..Tests.Testdata.TestData import TestData, json_to_obj, TestDataJSONObj


class CommonConfig:

    def __init__(self,
                 banner_local='ALDO-CAEN',
                 browser='chrome',
                 environment='UAT',
                 purl=None
                 ):
        self.__banner_local = banner_local
        self.__browser = browser
        self.__environment = environment
        self.__purl = purl



    def __base_url(self):
        banner = self.__banner_local.split('-')[0]
        if banner == 'ALDO':
            return 'aldoshoes'
        elif banner == 'CIS':
            return 'callitspring'
        elif banner == 'GLOBO':
            return 'globoshoes'
        else:
            raise Exception(" No support of Banner {.banner}" .format(self.__banner_local))


    def __domain(self):
        if self.__environment == 'UAT':
              # return ['https://wfe-','-uat-nlb.ecom-uat.paws.aldogroup.com']
              return ['https://uat.', '.com']
        elif self.__environment == 'PERF':
              return ['https://perf.', '.com']
        elif self.__environment == 'DEV3':
            return ['https://wfe-', '-dev3-nlb.ecom-dev.paws.aldogroup.com']
        elif self.__environment == 'QA3':
            return ['https://wfe-', '-qa3-nlb.ecom-dev.paws.aldogroup.com']
        elif self.__environment == 'PROD':
            return ['https://www.', ".com"]
        else:
            raise Exception(" No support of Environment{.environment}".format(self.__environment))

    def __country_language(self):
        local = self.__banner_local.split('-')[1]
        if local == 'CAEN':
            return '/ca/en/'
        elif local == 'CAFR':
            return '/ca/fr/'
        elif local == 'USEN':
            return '/us/en_US/'
        elif local == 'UKEN':
            return '/uk/en_UK/'
        else:
            raise Exception(" No support of Local{.local}".format(self.__banner_local))


    def get_site_url(self):
        domain = self.__domain()
        base = domain[0]+self.__base_url()+domain[1]+self.__country_language()
        url = urljoin(base, self.__purl)
        return url


    def get_browser(self):
        if self.__browser == "chrome":
            return Browser.CHROME
        elif self.__browser == 'firefox':
            return Browser.FF
        elif self.__browser == 'safari':
            return Browser.SAFARI
        elif self.__browser == 'remote':
            return Browser.REMOTE
        elif self.__browser == 'mobile':
            return Browser.MOBILE
        elif self.__browser == 'android':
            return Browser.ANDROID
        else:
            raise Exception(" No support of Browser{.browser}".format(self.__browser))

    def test_data(self):
        data = TestDataJSONObj(banner=self.__banner_local, environment=self.__environment).data()
        return TestData(json_to_obj(data))

