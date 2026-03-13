from pages.base_page import BasePage

class ButtonNumberKeysPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/news'

    BUTTON_NEWS_KEY = ("xpath", "//div//button[@aria-label='Перейти на 3 страницу']")
 
  

    def click_button_number_keys (self):  
        button_number_keys = self.driver.find_element(*self.BUTTON_NEWS_KEY) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_number_keys)  