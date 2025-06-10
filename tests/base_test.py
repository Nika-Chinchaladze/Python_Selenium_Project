import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from main.pages.home_page import HomePage

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)

        # Make driver and home_page available to test methods
        request.instance.driver = self.driver
        request.instance.home_page = self.home_page
        yield
        self.driver.quit()
