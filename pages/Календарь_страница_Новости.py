from pages.base_page import BasePage

class ButtonCalendarPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/news'


    BUTTON_CALENDAR = ("xpath", "(//div//button)[1]")


    def click_button_calendar(self):
        button_calendar = self.driver.find_element(*self.BUTTON_CALENDAR)
        self.driver.execute_script("arguments[0].click();", button_calendar)