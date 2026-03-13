from pages.base_page import BasePage

class SortingUsefulPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/library'

    BUTTON_SORTING= ("xpath", "//div[text()='Сортировка:']")
    BUTTON_SORTING_USEFUL = ("xpath", "//div[text()='По названию']")
  

    def click_button_sorting (self):  
        button_sorting = self.driver.find_element(*self.BUTTON_SORTING) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_sorting)


    def click_button_sorting_useful (self):  
        button_sorting_useful = self.driver.find_element(*self.BUTTON_SORTING_USEFUL) # Добавляем явное ожидание
        self.driver.execute_script("arguments[0].click();", button_sorting_useful)