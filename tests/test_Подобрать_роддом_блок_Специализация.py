import pytest

class TestSpecializationPage:
    def test_block_specialization(self, meaning_block_specialization):
        meaning_block_specialization.open()
        meaning_block_specialization.enter_meaning_block_specialization()