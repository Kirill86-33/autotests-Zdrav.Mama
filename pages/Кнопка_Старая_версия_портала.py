from pages.base_page import BasePage

class OldVersionPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    BUTTON_OLD_VERSION = ("xpath", "//button[text()='Старая версия портала']")
 
  

    def click_old_version_button (self):  
        button_old = self.driver.find_element(*self.BUTTON_OLD_VERSION) # Добавляем явное ожидание
        button_old.click()

