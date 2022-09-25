import unittest
from src.main import main
from src.result import Result
from src.choice import Choice
from unittest.mock import patch

class Test_Main(unittest.TestCase):
    
    @patch("src.main.get_input", side_effect=["dharun", "1", "n"])
    def test_Beats(self, input):
        # mock_input.=["dharun", "1", "n"]
        # monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        main()
        
        