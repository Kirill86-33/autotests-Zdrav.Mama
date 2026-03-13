from pages.base_page import BasePage

class ButtonDoctorsPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/top_clinics/gbuz-mo-moskovskij-oblastnoj-nauchno-issledovatelskij-institut-akusherstv-i-ginekologii'


    BUTTON_ALL_DOCTORS = ("xpath", "(//div//a)[4]")


    def click_button_doctors(self):
        button_doctors = self.driver.find_element(*self.BUTTON_ALL_DOCTORS)
        self.driver.execute_script("arguments[0].click();", button_doctors)