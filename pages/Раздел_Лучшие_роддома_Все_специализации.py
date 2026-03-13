from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ButtonSpecializationsPage(BasePage):
    PAGE_URL = 'https://mama.zdrav.mosreg.ru/'

    # Локаторы
    INPUT_SPECIALIZATIONS = ("xpath", "//*[@id='__next']/main/div/div/div[4]/div/div/div[1]/div[2]/div/div/span")
    SELECTION_VALUES = ("xpath", "//*[@id='menu-']/div[3]/ul/li[3]")
    
    def click_input_specializations(self):
        """Клик по полю 'Все специалисты'"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.INPUT_SPECIALIZATIONS)
        )
        element.click()
    
    def select_value_from_list(self):
        """Выбор значения из списка"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SELECTION_VALUES)
        )
        element.click()