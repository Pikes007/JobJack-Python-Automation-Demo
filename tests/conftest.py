import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture(scope="function")
def setup(request, api_session):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = None
    if "web" in request.keywords:
        chromedriver_path = ChromeDriverManager().install()
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        url = "https://app.jobjack.co.za/"
        driver.get(url)
        driver.maximize_window()
    request.cls.driver = driver
    request.cls.api_session = api_session

    yield driver

    if request.cls.driver:
        driver.close()
