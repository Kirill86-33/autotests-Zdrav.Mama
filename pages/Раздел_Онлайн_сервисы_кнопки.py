from pages.base_page import BasePage

class ButtonOnlineService(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'


    BUTTON_RIGHT = ("xpath", "(//div//button[@type='button'])[53]")
    BUTTON_LEFT = ("xpath", "(//div//button[@type='button'])[52]")


    def click_button_right(self):
        button_right = self.driver.find_element(*self.BUTTON_RIGHT)
        self.driver.execute_script("arguments[0].click();", button_right)


    def click_button_left(self):
        button_left = self.driver.find_element(*self.BUTTON_LEFT)
        self.driver.execute_script("arguments[0].click();", button_left)


 