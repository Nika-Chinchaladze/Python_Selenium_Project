from typing import Literal, Set
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
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
    
    def scroll_to_element_js(self, locator: By) -> None:
        self.driver.execute_script('arguments[0].scrollIntoView();', self.find(locator))
    
    def scroll_to_element_and_click(self, locator: By, click_option: Literal['selenium', 'javascript']) -> None:
        self.scroll_to_element_js(locator)
        if click_option == 'selenium':
            self.click_on_element(locator)
        else:
            self.click_js(locator)
    
    def click_on_check_box(self, locator: By) -> None:
        if not self.find(locator).is_selected():
            self.scroll_to_element_and_click(locator, 'javascript')
    
    def un_click_on_check_box(self, locator: By) -> None:
        if self.find(locator).is_selected():
            self.scroll_to_element_and_click(locator, 'javascript')
    
    def set_value_into_field(self, locator: By, text: str) -> None:
        self.find(locator).send_keys(text)
    
    def clear_from_field(self, locator: By) -> None:
        self.find(locator).clear()
    
    def select_by_visible_text(self, locator: By, visible_text: str) -> None:
        self.scroll_to_element_js(locator)
        self.find_drop_down(locator).select_by_visible_text(visible_text)
    
    def select_by_hidden_value(self, locator: By, hidden_value: str) -> None:
        self.scroll_to_element_js(locator)
        self.find_drop_down(locator).select_by_value(hidden_value)
    
    def select_by_index(self, locator: By, index: int) -> None:
        self.scroll_to_element_js(locator)
        self.find_drop_down(locator).select_by_index(index)
    
    def de_select_by_visible_text(self, locator: By, visible_text: str) -> None:
        self.scroll_to_element_js(locator)
        self.find_drop_down(locator).deselect_by_visible_text(visible_text)
    
    def de_select_by_hidden_value(self, locator: By, hidden_value: str) -> None:
        self.scroll_to_element_js(locator)
        self.find_drop_down(locator).deselect_by_value(hidden_value)
    
    def de_select_by_index(self, locator: By, index: int) -> None:
        self.scroll_to_element_js(locator)
        self.find_drop_down(locator).deselect_by_index(index)
    
    def accept_alert(self) -> None:
        alert = self.waiter().until(expected_conditions.alert_is_present())
        alert.accept()
    
    def dismiss_alert(self) -> None:
        alert = self.waiter().until(expected_conditions.alert_is_present())
        alert.dismiss()
    
    def send_keys_to_alert(self, prompt_text: str) -> None:
        alert = self.waiter().until(expected_conditions.alert_is_present())
        alert.send_keys(prompt_text)
    
    def switch_to_frame_by_string_id(self, string_id: str) -> None:
        self.driver.switch_to.frame(string_id)
    
    def switch_to_frame_by_index(self, index: int) -> None:
        self.driver.switch_to.frame(index)
    
    def switch_to_frame_by_web_element(self, locator: By) -> None:
        self.driver.switch_to.frame(self.find(locator))

    def switch_from_frame_to_parent(self) -> None:
        self.driver.switch_to.parent_frame()
    
    def switch_from_frame_to_document(self) -> None:
        self.driver.switch_to.default_content()
    
    def store_original_window(self) -> str:
        return self.driver.current_window_handle

    def switch_to_new_window(self, original_window: str) -> None:
        window_handles: Set[str] = self.driver.window_handles
        for handle in window_handles:
            if not handle == original_window:
                self.driver.switch_to.window(handle)
                break
    
    def switch_back_to_original_window(self, original_window: str) -> None:
        self.driver.switch_to.window(original_window)
    
    def get_element_attribute_value(self, locator: By, attribute_name: str) -> str:
        return self.find(locator).get_attribute(attribute_name)
