from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
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
    
    def verify_element_is_selected(self, locator: By) -> bool:
        return self.find(locator).is_selected()
    
    def verify_drop_down_selected_element(self, locator: By, element_content: str) -> bool:
        all_selected_elements: List[WebElement] = self.find_drop_down(locator).all_selected_options
        all_selected_text_content: List[str] = [element.text for element in all_selected_elements]
        return element_content in all_selected_text_content
        
    def verify_alert_by_text_content(self, alert_text: str) -> bool:
        alert = self.waiter().until(expected_conditions.alert_is_present())
        return alert.text == alert_text

    def verify_attribute_value(self, locator: By, attribute_name: str, attribute_value: str) -> bool:
        return self.find(locator).get_attribute(attribute_name) == attribute_value
    