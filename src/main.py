'''
This is the main class where game is implemented. It takes user choice Rock Paper and Scissor, and generates computer choice randomly. It also store all the stats and displays it at the end. There are two function used to display in the monitor. The user can play multiple times

'''

from src.result import Result
from src.choice import Choice
import random
import time

def get_input(text=''):
    _input = input(text)
    print(_input)
    return _input


#This function is used to display the welcome message
def display():
    print("Welcome to the classic Rock Paper Scissor Game")
    time.sleep(1)
    print("Are you the master of RPS Game")
    print("It all depends on your Choice")
    print("So Choose Wisely!!!")
    
    name = get_input("Let's begin with your Name: ")
    time.sleep(0.5)
    print("Good Luck %s !!\n\n" %(name))
    
    
    
    print("you have 3 weapons to choose from ")
    for choice in Choice:
        print(str(choice.value)+": "+str(choice))
    
    return name

#this function is used to display stats
def displayStatistics(Results_Dic,Total_Games_Played):
    COUNT="count"
    
    print("Update your strategy with our statistics\n")
    time.sleep(0.5)
    print("You have played %d times" %(Total_Games_Played))
    
    
    for result in Results_Dic.keys():
            print("you have %s %d times"%(result,Results_Dic[result][COUNT]))
            for choice in Results_Dic[result].keys():
                if choice is COUNT:
                    continue
                print("\t with %s %d times"%(choice,Results_Dic[result][choice][COUNT]))
    
    return



def main():
    
    name=display()
    COUNT="count"
    Total_Games_Played = 0
    Results_Dic={}
    
    #creating stats Dictionary
    for result in Result:
        temp_dic={COUNT:0}
        for choice in Choice:
            temp_dic[choice.name]={COUNT:0}
        Results_Dic[result.name]=temp_dic
    
    #runs untill the user says N or n
    while (True):
    
        Computer_Choice=Choice(random.randint(1,3))
        time.sleep(0.5)
        print("The computer is making it\'s' selection") 
                
        while (True):
            try:
                User_Choice=Choice(int(get_input("Please select your weapon (1:R,2:P,3:S): ")))
                break
            except ValueError:
                print("Invalid selection, please choose form (1,2,3): ")
            
            
        print("You have chosen ", str(User_Choice))
        print ("The computer Chose ", str(Computer_Choice))
        
        result=User_Choice.Beats(Computer_Choice)
        
        print(result)
        
        time.sleep(1)
        
        while (True):
            inp=get_input("Do you want to play again (y/n): ")
            if (inp in ('Y','y','N','n')):
                break
            else:
                print("Invalid selection, please choose form (y,n): ")
        Total_Games_Played+=1
        Results_Dic[result.name][COUNT]+=1
        Results_Dic[result.name][User_Choice.name][COUNT]+=1
        if inp.lower() == 'n':
                break
        
    
    displayStatistics(Results_Dic,Total_Games_Played)
    
    time.sleep(1)
    print("\nThanks %s for playing our game" %(name))
    
    
   

if __name__ == '__main__':
    main()
