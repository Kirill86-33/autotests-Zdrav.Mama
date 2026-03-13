from pages.base_page import BasePage

class ButtonShowAllPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/clinics'

    BUTTON_SHOW_ALL= ("xpath", "//div[text()='Показать все']")



    def click_button_show_all (self):
        button_show = self.driver.find_element(*self.BUTTON_SHOW_ALL)
        self.driver.execute_script("arguments[0].click();", button_show)   