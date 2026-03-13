import pytest

class TestOldPage:
    
    def test_old_version(self, old_version_page):  # old_version_page - это название созданной фикстура
        old_version_page.open()
        old_version_page.click_old_version_button()
        print("✓ Кнопка 'Старая версия портала'")

