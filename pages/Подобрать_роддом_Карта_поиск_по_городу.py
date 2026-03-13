from pages.base_page import BasePage

class SearchCityMap(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/clinics'

    BUTTON_MAP = ("xpath", "//div//button[text()='Карта']")
    INPUT_CITY = ("xpath", "//*[@id=':r2:']")
    BUTTON_CITY = ("xpath", "(//div//label)[1]")
  

    

    def click_button_map(self):
        button_map = self.driver.find_element(*self.BUTTON_MAP)
        self.driver.execute_script("arguments[0].click();", button_map) 
    

    def enter_input_city (self, driver):  
        input_city = self.driver.find_element(*self.INPUT_CITY) # Добавляем явное ожидание
        input_city.send_keys(driver)


    def click_button_city(self):
        button_city = self.driver.find_element(*self.BUTTON_CITY)
        self.driver.execute_script("arguments[0].click();", button_city) 
    
    