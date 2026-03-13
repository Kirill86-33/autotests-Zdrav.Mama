from pages.base_page import BasePage

class ButtonAllNewsPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    BUTTON_ALL_NEWS = ("xpath", "//div//a[@href='/news']")



    def click_button_all_news(self):
        button_news = self.driver.find_element(*self.BUTTON_ALL_NEWS)
        self.driver.execute_script("arguments[0].click();", button_news)   