from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from main.helper.base_help import BaseHelp

class Assertions(BaseHelp):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
    
    def verify_page_url(self, url: str) -> bool:
        return self.driver.current_url() == url
    
    def verify_element_is_displayed(self, locator: Tuple[By, str]) -> bool:
        return self.find(locator).is_displayed()
    
    def verify_multiple_elements_are_displayed(self, locators: List[By]) -> bool:
        result: bool = True
        for locator in locators:
            result = self.verify_element_is_displayed(locator)
        return result
    
    def verify_element_is_not_displayed(self, locator: By) -> bool:
        return not self.verify_element_is_displayed(locator)
    
    def verify_element_is_enabled(self, locator: By) -> bool:
        return self.find(locator).is_enabled()
    
    def verify_element_has_text(self, locator: By, text: str) -> bool:
        return text in self.find(locator).text
    
    def verify_element_has_value(self, locator: By, value: str) -> bool:
        return value in self.find(locator).get_attribute('value')

