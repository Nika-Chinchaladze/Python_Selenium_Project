import pytest
from tests.base_test import BaseTest

@pytest.mark.regression
class TestHomePage(BaseTest):
    def test_home_page(self):
        self.home_page.actions.navigate_to_url(self.home_page.URL)
        assert self.home_page.assertions.verify_element_is_displayed(self.home_page.title)
    