from testit_python_commons.decorators import externalId, displayName

class TestLinkClinicPage:
    @externalId("test_link_clinic")
    @displayName("Поиск клиники")
    def test_link_clinic(self, input_search_clinic ):  # Фикстура автоматически передаст login_page
        input_search_clinic.open()
        input_search_clinic.click_enter_input_clinic("ГБУЗ МО Клинская больница")