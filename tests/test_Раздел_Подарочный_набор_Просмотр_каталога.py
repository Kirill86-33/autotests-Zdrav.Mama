from testit_python_commons.decorators import externalId, displayName

class TestCatalogForm:
    @externalId("test_button_catalog")
    @displayName("Кнопка 'Каталог'")
    def test_button_catalog(self, button_catalog):
        button_catalog.open()
        button_catalog.click_button_catalog()