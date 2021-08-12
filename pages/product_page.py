from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    HOME_LINK = (By.XPATH, "//a[(@href='https://gettop.us')]")

    def click_home_link(self):
        self.click(*self.HOME_LINK)