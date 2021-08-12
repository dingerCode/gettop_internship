from pages.base_page import Page
from support.logger import logger


class Main(Page):
    def open_main(self):
        logger.info('Opening the url https://gettop.us/')
        self.open_url(url='https://gettop.us/')