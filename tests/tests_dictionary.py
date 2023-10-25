import unittest
from unittest.mock import patch
from game.dictionary import (
    validate_dictionary,
    DictionaryConnectionError,
)

class TestDiccionary(unittest.TestCase):
    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='1. interj. U. como salutación familiar.'
        )
    )

    def test_valid(self, search_by_word_patched):
        self.assertTrue(validate_dictionary('hola'))
    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
        )
    )

    def test_invalid(self, search_by_word_patched):
        self.assertFalse(validate_dictionary('asd'))
    @patch(
        'pyrae.dle.search_by_word',
        return_value=None
    )

    def test_connection_error(self, search_by_word_patched):
        with self.assertRaises(DictionaryConnectionError):
            validate_dictionary('hola')


if __name__ == '__main__':
    unittest.main()