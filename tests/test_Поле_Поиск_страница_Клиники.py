import pytest

class TestLinkClinicPage:
    
    def test_link_clinic(self, input_search_clinic ):  # Фикстура автоматически передаст login_page
        input_search_clinic.open()
        input_search_clinic.click_enter_input_clinic("ГБУЗ МО Клинская больница")