from typing import Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BaseHelp:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
    
    def find(self, locator: Tuple[By, str]):
        by, value = locator
        return self.driver.find_element(by, value)
    
    def find_multiple(self, locator: By):
        return self.driver.find_elements(locator)
    
    def find_drop_down(self, locator: By):
        return Select(self.find(locator))
