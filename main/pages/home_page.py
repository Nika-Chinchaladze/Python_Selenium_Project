from selenium.webdriver.common.by import By
from main.pages.base_page import BasePage

class HomePage(BasePage):
    URL = 'https://demoqa.com/'
    title = (By.CSS_SELECTOR, 'header a')
