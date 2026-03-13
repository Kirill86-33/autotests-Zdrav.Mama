from pages.base_page import BasePage

class PageUseful(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/library'

    INPUT_USEFUL = ("xpath", "//*[@id=':r1:']")
    BUTTON_INFORMATION = ("xpath", "(//div//a)[11]")
  


    def click_enter_input_useful(self, driver):  
        input_useful = self.driver.find_element(*self.INPUT_USEFUL) # Добавляем явное ожидание
        input_useful.send_keys(driver)


    def click_information(self):
        button_information = self.driver.find_element(*self.BUTTON_INFORMATION)
        self.driver.execute_script("arguments[0].click();", button_information)