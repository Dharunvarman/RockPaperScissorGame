from enum import Enum
from result import Result

class Choice(Enum):
    
    Rock = 1
    Paper = 2
    Scissor = 3
    
    def __str__(self):
        return str(self.name)
    
    def Beats(self,choice):
        
        won=1
        tie=0
        lost=-1
        
        if(self.value==choice.value):
                return Result(tie)
        
        
        if Choice.Rock.Equals(self) or Choice.Rock.Equals(choice):
            n=len(Choice)
            
            if (self.value%n)>(choice.value%n):
                return Result(won)
            return Result(lost)
            
        if self.value>choice.value:
            return Result(won)
        
        return Result(lost)

    def Equals(self,choice):
        return self is choice