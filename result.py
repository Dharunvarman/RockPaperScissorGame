
from enum import Enum

#Enum is used because they are immutable related set of constant values
class Result(Enum):
    Won = 1
    Tied = 0
    Lost = -1
    
    def __str__(self):
        if self is Result.Won:
            return "Congratulations!! You have won the game"
        elif self is Result.Lost:
            return "You have lost the game, Better luck next time!!"
        else:
            return "It\'s a tie, Better luck next time!!"