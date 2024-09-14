import pytest

from selenium import webdriver
import os

import sys



sys.path.append(os.path.abspath('C:\\Users\\VRM\\OneDrive\\Documents\\saucedemo_pom-main\\task26\\pytest.ini'))
@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://orangehrm.com/")  # Replace with the actual OrangeHRM URL
    request.cls.driver = driver
    yield
    driver.quit()
