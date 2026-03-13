from pages.base_page import BasePage

class TabTestPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/quiz'

    TAB_TEST = ("xpath", "(//div//button)[2]")
 
  
    def click_tab_test (self):  
        click_tab = self.driver.find_element(*self.TAB_TEST) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", click_tab)