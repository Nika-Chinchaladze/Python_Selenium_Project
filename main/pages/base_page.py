from selenium import webdriver
from main.helper.actions import Actions
from main.helper.assertions import Assertions

class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.actions = Actions(driver)
        self.assertions = Assertions(driver)
