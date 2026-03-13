import pytest
from selenium import webdriver
from pages import Подобрать_роддом_Карта_поиск_по_городу
from pages.main_page import MainPage
from pages.Кнопка_Родить_в_Подмосковье import BirthPage
from pages.Кнопка_Оставить_заявку import LeavePage
from pages.Кнопка_Старая_версия_портала import OldVersionPage
from pages.Кнопка_Трубка_телефона import ButtonPhonePage
from pages.Раздел_Преимущества_выбор_значений import SelectPage
from pages.Раздел_Подарочный_набор_Узнать_больше import ButtonFindPage
from pages.Раздел_Подарочный_набор_Просмотр_каталога import ButtonCatalogPage
from pages.Хлебные_крошки_Услуга import ButtonServicesPage
from pages.Страница_Услуги_выбор_значений import ArticlesPage
from pages.Раздел_Лучшие_роддома_Все_специализации import ButtonSpecializationsPage
from pages.Раздел_Лучшие_роддома_кнопка_стрелка import ButtonRightPage
from pages.Кнопка_Посмотреть_все_раздел_Лучшие_роддома import ButtonViewPage
from pages.Раздел_Лучшие_роддома_переход_ЛПУ import ButtonHospitalPage
from pages.ЛПУ_кнопка_Записаться import RegisterHospitalPage
from pages.ЛПУ_кнопка_Все_врачи import ButtonDoctorsPage
from pages.Раздел_Контрактные_роды_деактивация_тогл import SelectToglPage
from pages.Раздел_Контрактные_роды_Получить_уникальное_предложение import ButtonUniquePage
from pages.Раздел_Новости_кнопка_Все_Новости import  ButtonAllNewsPage
from pages.Поле_Поиск_страница_Новости import SearchNews
from pages.Календарь_страница_Новости import ButtonCalendarPage
from pages.Страница_Новости_выбор_тега import ButtonTagsPage
from pages.Кнопка_Подписаться_страница_Новости import ButtonSubscribePage
from pages.Кнопка_для_перехода_на_страницу import ButtonNumberKeysPage
from pages.Кнопка_Перезвоните_мне import ButtonCallMePage
from pages.Раздел_Онлайн_сервисы_кнопки import ButtonOnlineService
from pages.Тест_Опросы_Голосование import CardSurveys
from pages.Поле_Поиск_страница_Тест_опросы_голосование import SearchImputPage
from pages.Тест_опросы_голосование_выбор_тега import TabTestPage
from pages.Тест_опросы_голосование_Темы import ButtonChoosingPage
from pages.Тест_опросы_голосование_прохождение_теста import PassingTestPage
from pages.Онлайн_консультация_гинеколога import CardGynecologist
from pages.Школа_матерей import CardMothersSchool
from pages.Школа_матерей_прохождение_теста import PassingTestMothersSchoolPage
from pages.Подобрать_роддом import CardMaternityHospital
from pages.Подобрать_роддом_вкладка_Список import ListClinicPage
from pages.Подобрать_роддом_вкладка_Карта import ListMapPage
from pages.Поле_Поиск_страница_Клиники import SearchClinic
from pages.Подобрать_роддом_Список_поиск_по_городу import SearchCity
from pages.Подобрать_роддом_Карта_поиск_по_городу import SearchCityMap
from pages.Кнопка_Показать_все_страница_Клиники import ButtonShowAllPage
from pages.Подобрать_роддом_блок_Специализация import BlockSpecialization
from pages.Первые_симптомы_беременности import CardFirstPregnancy
from pages.Оставить_обращение_в_чате import CardChatRequest
from pages.Поле_Напишите_ваш_городской_округ import FieldYourCounty
from pages.Вопрос_ответ import CardQuestionAnswer
from pages.Информация_на_странице_Вопрос_ответ import ButtonInformationPage
from pages.Блок_Не_Нашли_ответ_на_вопрос import NotFoundAnswer
from pages.Библиотека import CardLibrary
from pages.Поле_Поиск_страница_Полезное import PageUseful
from pages.Страница_Полезное_блок_Тема import PageUsefulTopic
from pages.Сортировка_По_Названию_Полезное import SortingUsefulPage



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def birth_page(driver):
    """Фикстура для страницы с формой"""
    page = BirthPage(driver)
    page.open()
    return page


@pytest.fixture
def leave_page(driver):
    page = LeavePage(driver)
    page.open()
    return page


@pytest.fixture
def old_version_page(driver):
    return OldVersionPage(driver)


@pytest.fixture
def button_phone (driver):
    return ButtonPhonePage (driver)


@pytest.fixture
def select_tab (driver):
    return SelectPage (driver)

@pytest.fixture
def button_find (driver):
    return ButtonFindPage(driver)


@pytest.fixture
def button_catalog (driver):
    return ButtonCatalogPage(driver)

@pytest.fixture
def button_services (driver):
    return ButtonServicesPage(driver)

@pytest.fixture
def button_articles_services(driver):
    return ArticlesPage(driver)

@pytest.fixture
def input_specializations(driver):
    return ButtonSpecializationsPage(driver)

@pytest.fixture
def button_right(driver):
    return ButtonRightPage(driver)

@pytest.fixture
def button_view_all(driver):
    return ButtonViewPage(driver)


@pytest.fixture
def button_hospital(driver):
    return ButtonHospitalPage(driver)

@pytest.fixture
def register_page(driver):
    page =  RegisterHospitalPage(driver) # RegisterHospitalPage -это созданный класс в button_register_maternity_hospital
    page.open()
    return page

@pytest.fixture
def button_doctors(driver):
    return ButtonDoctorsPage (driver)

@pytest.fixture
def button_togl(driver):
    page = SelectToglPage(driver)
    page.open()
    return page

@pytest.fixture
def button_unique_offer(driver):
    page = ButtonUniquePage(driver)
    page.open()
    return page

@pytest.fixture
def button_all_news(driver):
    return  ButtonAllNewsPage(driver)

@pytest.fixture
def input_search_news(driver):
    return SearchNews(driver)

@pytest.fixture
def button_calendar(driver):
    return ButtonCalendarPage(driver)

@pytest.fixture
def button_tag_news(driver):
    return ButtonTagsPage(driver)

@pytest.fixture
def button_subscribe(driver):
    page = ButtonSubscribePage (driver) 
    page.open()
    return page

@pytest.fixture
def button_news_key(driver):
    return ButtonNumberKeysPage(driver)

@pytest.fixture
def button_call_me(driver):
    page = ButtonCallMePage(driver) 
    page.open()
    return page


@pytest.fixture
def online_service(driver):
    return ButtonOnlineService(driver)


@pytest.fixture
def card_test_voting(driver):
    return CardSurveys(driver)



@pytest.fixture
def search_test_voting(driver):
    return SearchImputPage (driver)


@pytest.fixture
def button_tab_test(driver):
    return TabTestPage(driver)



@pytest.fixture
def button_selecting_topic(driver):
    return ButtonChoosingPage(driver)


@pytest.fixture
def button_passing_test(driver):
    return PassingTestPage(driver)

@pytest.fixture
def card_gynecologist(driver):
    return CardGynecologist(driver)


@pytest.fixture
def card_mothers_school(driver):
    return CardMothersSchool(driver)


@pytest.fixture
def test_passing_mothers_school(driver):
    return PassingTestMothersSchoolPage(driver)


@pytest.fixture
def card_maternity_hospital(driver):
    return CardMaternityHospital(driver)


@pytest.fixture
def tab_list(driver):
    return ListClinicPage(driver)

@pytest.fixture
def tab_map(driver):
    return ListMapPage(driver)


@pytest.fixture
def input_search_clinic(driver):
    return SearchClinic(driver)



@pytest.fixture
def input_search_city(driver):
    page = SearchCity(driver) 
    page.open()
    return page


@pytest.fixture
def button_search_city(driver):
    page = SearchCityMap (driver) 
    page.open()
    return page


@pytest.fixture
def button_show_all(driver):
    return ButtonShowAllPage(driver)


@pytest.fixture
def meaning_block_specialization(driver):
    return BlockSpecialization(driver)


@pytest.fixture
def card_first_pregnancy(driver):
    return CardFirstPregnancy(driver)


@pytest.fixture
def card_chat_request(driver):
    return CardChatRequest(driver)


@pytest.fixture
def input_field_your_county(driver):
    page = FieldYourCounty(driver) 
    page.open()
    return page


@pytest.fixture
def card_question_answer(driver):
    return CardQuestionAnswer(driver)


@pytest.fixture
def input_page_question_answer(driver):
    return ButtonInformationPage (driver)


@pytest.fixture
def input_not_found_answer(driver):
    page = NotFoundAnswer(driver) 
    page.open()
    return page


@pytest.fixture
def card_library(driver):
    return CardLibrary(driver)

@pytest.fixture
def input_search_useful(driver):
    page = PageUseful(driver) 
    page.open()
    return page


@pytest.fixture
def button_topic(driver):
    return PageUsefulTopic(driver)


@pytest.fixture
def button_sorting_useful(driver):
    return SortingUsefulPage(driver)