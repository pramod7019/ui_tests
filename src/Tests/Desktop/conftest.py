import pytest
from ...Helpers.Browser import Browser
from ...PageObjects.Page import Page
from uitests.src.ConfigReader import Configuration


def config():
    configuration = Configuration()
    return configuration

# def pytest_addoption(parser):
#   parser.addoption("--browser", action="store", default="chrome", help='specify browser eg: "chrome"')
#   parser.addoption("--banner", action="store", default="ALDO-CAEN", help='specify banner eg: "ALDO"')
#   parser.addoption("--environment", action="store", default="PROD", help='specify environment eg: "UAT"')


@pytest.fixture(params=config().banners)
def site(request):
    browser = config().browser
    env = config().environment
    url = None
    return Page(banner=request.param, browser=browser, environment=env, url=url)

@pytest.fixture(autouse=True)
def setup(site):
    site.open()
    yield
    site.close()

@pytest.fixture()
def data(site):
    return site.test_data()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    result = outcome.get_result()
    test = result.nodeid.split("::")[-1]
    extra = getattr(result, 'extra', [])
    if result.when == "call" and result.failed:
        screenshot = Browser.take_screenshot(test)
        if screenshot:
            html = '<div><img src=' +screenshot+' alt="screenshot" style="width:450px;height:228px;" ' \
                                                'align="right" onclick="window.open(this.src)"'
            extra.append(pytest_html.extras.html(html))
            result.extra = extra


skip_for_prod = pytest.mark.skipif(
  config().environment == 'PROD', reason="This test should not run in prod"
)


aldo = pytest.mark.parametrize('site', config().aldo_banners, indirect=True)
cis = pytest.mark.parametrize('site', config().cis_banners, indirect=True)
globo = pytest.mark.parametrize('site', config().globo_banners, indirect=True)
aldo_cis = pytest.mark.parametrize('site', config().aldo_cis_banners, indirect=True)
aldo_globo = pytest.mark.parametrize('site', config().aldo_globo_banners, indirect=True)
globo_cis = pytest.mark.parametrize('site', config().globo_cis_banners, indirect=True)
aldo_us = pytest.mark.parametrize('site', config().aldo_us_banner, indirect=True)

