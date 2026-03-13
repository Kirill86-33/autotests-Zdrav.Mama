from pages.base_page import BasePage

class ButtonRightPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    RIGHT_ARROW = ("xpath", "(//div//button[@type='button']) [40]")



    def click_button_right_arrow(self):
        button_right_arrow = self.driver.find_element(*self.RIGHT_ARROW)
        self.driver.execute_script("arguments[0].click();", button_right_arrow)   