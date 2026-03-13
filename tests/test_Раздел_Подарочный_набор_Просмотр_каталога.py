import pytest

class TestCatalogForm:
    def test_button_catalog(self, button_catalog):
        button_catalog.open()
        button_catalog.click_button_catalog()