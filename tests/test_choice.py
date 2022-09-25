import unittest
from src.result import Result
from src.choice import Choice

class Test_choice(unittest.TestCase):

    def test_Beats(self):
        Rock=Choice(1)
        Paper=Choice(2)
        Scissor=Choice(3)
        Win=Result(1)
        Tie=Result(0)
        Loose=Result(-1)
        
        response=Rock.Beats(Scissor)
        response1=Paper.Beats(Scissor)
        response2=Rock.Beats(Rock)
        response3=Scissor.Beats(Rock)
        response4=Scissor.Beats(Paper)
        response5=Rock.Beats(Paper)
        self.assertEqual(response,Win)
        self.assertEqual(response1,Loose)
        self.assertEqual(response2,Tie)
        self.assertEqual(response3,Loose)
        self.assertEqual(response4,Win)
        self.assertEqual(response5,Loose)

    def test_Equals(self):
        Rock=Choice(1)
        Paper=Choice(2)
        
        response=Rock.Equals(Paper)
        response1=Rock.Equals(Rock)
        
        self.assertEqual(response,False)
        self.assertEqual(response1,True)
        

if __name__ == "__main__":
    unittest.main()

