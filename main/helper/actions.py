from selenium import webdriver
from selenium.webdriver.common.by import By
from main.helper.base_help import BaseHelp

class Actions(BaseHelp):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
    
    def navigate_to_url(self, url: str) -> None:
        self.driver.get(url)
    
    def click_on_element(self, locator: By) -> None:
        self.find(locator).click()
    
    def click_js(self, locator: By) -> None:
        self.driver.execute_script('arguments[0].click();', self.find(locator))
    
    def set_value_into_field(self, locator: By, text: str) -> None:
        self.find(locator).send_keys(text)
    
    def clear_from_field(self, locator: By) -> None:
        self.find(locator).clear()
    
    def scroll_to_element_js(self, locator: By) -> None:
        self.driver.execute_script('arguments[0].scrollIntoView();', self.find(locator))
