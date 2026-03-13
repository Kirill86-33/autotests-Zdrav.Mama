from pages.base_page import BasePage

class ButtonServicesPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/preimuschestvo/podarok_ili_denezhnaya_viplata'

    BUTTON_SERVICES = ("xpath", "(//nav//li[@class='MuiBreadcrumbs-li'])[2]")



    def click_button_services(self):
        button_services = self.driver.find_element(*self.BUTTON_SERVICES)
        self.driver.execute_script("arguments[0].click();", button_services)   