from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'
   
    
    INPUT_LOOKING = ("xpath", "//input[@class='MuiBox-root css-11ruyns']")
    BUTTON_BIRTH = ("xpath", "//a[text()='Родить в Подмосковье']")



    def enter_looking_for (self, looking):  
        input_looking = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.INPUT_LOOKING) # Добавляем явное ожидание
        )
        input_looking.clear()  # Рекомендуется очистить поле перед вводом
        input_looking.send_keys(looking)
   
    def click_give_birth (self):  
        button_birth = self.driver.find_element(*self.BUTTON_BIRTH) # Добавляем явное ожидание
        button_birth.click()
