from pages.base_page import BasePage

class SearchNews(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/news'

    INPUT_NEWS = ("xpath", "//*[@id=':r1:']")
    
  
    def click_enter_input_news (self, driver):  
        input_news = self.driver.find_element(*self.INPUT_NEWS) # Добавляем явное ожидание
        input_news.send_keys(driver)


       