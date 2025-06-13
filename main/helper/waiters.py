import time
from typing import Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from main.helper.base_help import BaseHelp

class Waiters(BaseHelp):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def delay(self, milliseconds: int) -> None:
        try:
            time.sleep(milliseconds / 1000)
        except KeyboardInterrupt:
            print("Delay interrupted")
    
    def wait_for_new_tab(self, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(lambda driver: len(driver.window_handles) > 1)
    
    def explicit_waiter(self, timeout: int = 10) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)

    def fluent_waiter(self, timeout: int = 10, poll_frequency: int = 2, ignored_exceptions: Exception = KeyboardInterrupt) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions)
    
    def explicit_wait_until_visible(self, locator: Tuple[By, str], timeout: int) -> None:
        self.explicit_waiter(timeout).until(expected_conditions.visibility_of_element_located(locator))
    
    def explicit_wait_until_attribute_value(self, locator: Tuple[By, str], attribute_name: str, attribute_value: str, timeout: int) -> None:
        self.explicit_waiter(timeout).until(self.find(locator).get_attribute(attribute_name) == attribute_value)

    def fluent_wait_until_visible(self, locator: Tuple[By, str], timeout: int) -> None:
        self.fluent_waiter(timeout).until(expected_conditions.visibility_of_element_located(locator))
    
    def fluent_wait_until_attribute_value(self, locator: Tuple[By, str], attribute_name: str, attribute_value: str, timeout: int) -> None:
        self.fluent_waiter(timeout).until(self.find(locator).get_attribute(attribute_name) == attribute_value)
