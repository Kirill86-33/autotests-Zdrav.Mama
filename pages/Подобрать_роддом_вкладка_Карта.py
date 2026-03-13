from pages.base_page import BasePage

class ListMapPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/clinics'

    TAB_MAP = ("xpath", "//div//button[text()='Карта']")
 
  
    def click_tab_map (self):  
        click_map = self.driver.find_element(*self.TAB_MAP) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", click_map)