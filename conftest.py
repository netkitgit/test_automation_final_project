# Для корректной работы требуется установка:
# pip install pytest
# pip install -U selenium
# pip install webdriver_manager

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')

@pytest.fixture(scope="function")
def browser(request):
    language = None
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nStart CHROME browser for test...")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    print("\nQuite browser...")
    browser.quit()
