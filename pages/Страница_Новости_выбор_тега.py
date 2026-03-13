from pages.base_page import BasePage

class ButtonTagsPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/news'

    TAG_PREGNANCY = ("xpath", "(//div//span[text()='#Беременность'])[1]")
 
  

    def click_button_tag (self):  
        button_tag = self.driver.find_element(*self.TAG_PREGNANCY) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_tag)