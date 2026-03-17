from testit_python_commons.decorators import externalId, displayName
class TestSpecializationsPage:
    @externalId("test_specializations_and_selection")
    @displayName("Специализации и выбор из списка")
    def test_specializations_and_selection(self, input_specializations):
        """Тест: открытие списка и выбор значения"""
        input_specializations.open()
        input_specializations.click_input_specializations()
        input_specializations.select_value_from_list()
      
