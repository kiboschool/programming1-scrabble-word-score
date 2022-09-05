from unittest.mock import patch
from unittest import TestCase
import unittest
import sys
import io

class Test(TestCase):
    @patch('builtins.print')
    @patch('builtins.input', return_value="apple")
    def test_apple(self, mock_input, mock_print):
        import main
        mock_print.assert_called_with("apple has a scrabble score of 9")
        sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', return_value="quixotic")
    def test_quixotic(self, mock_input, mock_print):
        import main
        mock_print.assert_called_with("quixotic has a scrabble score of 26")
        sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', return_value="freezer")
    def test_freezer(self, mock_input, mock_print):
        import main
        mock_print.assert_called_with("freezer has a scrabble score of 19")
        sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', return_value="abcdefghijklmnopqrstuvwxyz")
    def test_alphabet(self, mock_input, mock_print):
        import main
        mock_print.assert_called_with("abcdefghijklmnopqrstuvwxyz has a scrabble score of 87")
        sys.modules.pop('main')
if __name__ == '__main__':
    unittest.main()
