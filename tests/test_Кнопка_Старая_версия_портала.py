from testit_python_commons.decorators import externalId, displayName

class TestOldPage:
    @externalId("test_old_version")
    @displayName("Кнопка 'Старая версия портала'")
    def test_old_version(self, old_version_page):  # old_version_page - это название созданной фикстура
        old_version_page.open()
        old_version_page.click_old_version_button()
        print("✓ Кнопка 'Старая версия портала'")

