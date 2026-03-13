from pages.base_page import BasePage

class ListClinicPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/clinics'

    TAB_LIST = ("xpath", "//div//button[text()='Список']")
 
  
    def click_tab_list (self):  
        click_tab = self.driver.find_element(*self.TAB_LIST) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", click_tab)