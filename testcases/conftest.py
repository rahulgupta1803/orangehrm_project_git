import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        print("launching chrome")
        driver = webdriver.Chrome()

    elif browser == 'firefox':
        print("launching firefox")
        driver = webdriver.Firefox()

    elif browser == "edge":
        print('launching edge')
        driver = webdriver.Edge()

    else:
        print("launching headless")
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    time.sleep(1)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()
    return driver


@pytest.fixture(params=[
    ("Admin123", "admin123"),
    ("Admi", "admin123"),
    ("Admino", "admin12345"),
    ("Admin", "admin123"),
    ("Alladin", "abu")
])
def get_data_for_login(request):
    return request.param


def pytest_metadata(metadata):
    metadata["Class"] = 'Credence Automation Testing'
    metadata['Batch'] = 'CT-15'
    metadata['Tester'] = 'Rahul Gupta'
    metadata.pop("Platform",None)
