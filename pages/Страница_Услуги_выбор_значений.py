from pages.base_page import BasePage

class ArticlesPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/preimuschestvo'


    BUTTON_ARTICLES = ("xpath", "//*[@id='__next']/main/div/div[2]/div[1]/div[2]/div[1]/a")


    def click_button_articles_services(self):
        button_articles_services = self.driver.find_element(*self.BUTTON_ARTICLES)
        self.driver.execute_script("arguments[0].click();", button_articles_services)