
import pytest

from uitests.src.ConfigReader import ConfigReader
from uitests.src.ConfigReader import Configuration
from ...PageObjects.Page import Page


def config():
    configuration = Configuration()
    return configuration


@pytest.fixture(params=config().banners)
def site(request):
    browser = config().browser
    env = config().environment
    url = None
    return Page(banner=request.param, browser=browser, environment=env, url=url)


@pytest.fixture()
def data(site):
    return site.test_data()


@pytest.fixture(autouse=True)
def setup(site):
    site.open()
    yield
    site.close()
