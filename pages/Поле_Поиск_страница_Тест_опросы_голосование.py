from pages.base_page import BasePage

class SearchImputPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/quiz'

    SEARCH_TEST_VOTING = ("xpath", "//*[@id=':r1:']")
 
  
    def click_search_enter_test (self, driver):  
        input_search = self.driver.find_element(*self.SEARCH_TEST_VOTING) # Добавляем явное ожидание
        input_search.send_keys(driver)