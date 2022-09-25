import unittest
from main import Main
from result import Result
from choice import Choice
from pytest import MonkeyPatch

class Test_Main(unittest.TestCase):
    monkeyPatch = MonkeyPatch()
    
    def test_Beats(self):
        inputs=["dharun", "1", "n"]
        monkeyPatch.setattr("builtins.input", lambda _: inputs.pop(0))
        Main.main()
        
        