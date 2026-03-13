from pages.base_page import BasePage

class SelectPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    SELECT_TAB = ("xpath", "//div//h3[text()='Выбор способа родов']")
 
  

    def click_select_tab (self):  
        select_tab = self.driver.find_element(*self.SELECT_TAB) # Добавляем явное ожидание
        select_tab.click()
