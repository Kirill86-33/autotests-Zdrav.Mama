from pages.base_page import BasePage

class ButtonPhonePage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'


    BUTTON_PHONE = ("xpath", "//*[@id='__next']/main/div/div/div[9]/div/div[2]/button[2]")


    def click_button_phone(self):
        button_phone = self.driver.find_element(*self.BUTTON_PHONE)
        self.driver.execute_script("arguments[0].click();", button_phone)