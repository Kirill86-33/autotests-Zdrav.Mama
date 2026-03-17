from testit_python_commons.decorators import externalId, displayName

class TestSpecializationPage:
    @externalId("test_block_specialization")
    @displayName("Блок специализации")
    def test_block_specialization(self, meaning_block_specialization):
        meaning_block_specialization.open()
        meaning_block_specialization.enter_meaning_block_specialization()