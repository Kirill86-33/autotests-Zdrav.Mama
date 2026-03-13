import pytest

class TestMainPage:
    
    def test_looking(self, main_page):  # Фикстура автоматически передаст login_page
        main_page.open()
        main_page.enter_looking_for("Доктор")
        
        print("Ввод значение 'Доктор' в поле 'Что вы ищите?' выполнен успешно ")

    def test_give_birth_button(self, main_page):  # Исправлено название и фикстура
        main_page.open()
        main_page.click_give_birth()
        print("✓ Кнопка 'Родить' работает")
      