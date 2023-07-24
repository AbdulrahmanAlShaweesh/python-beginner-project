
import random

class DieGame :
    
    def __init__(self, startPlace, endPlace, userPlace, computerPlace, userWins, computerWins) :
        self.startPlace = startPlace 
        self.endplace = endPlace 
        self.userPlace = userPlace 
        self.computerPlace = computerPlace 
        self.userWins = userWins 
        self.computerWins = computerPlace
    
    def winer(self) :
        
        while not self.userWins or not self.computerWins :
            user_choose = input('enter t : to toss or q to quit the game ? ').strip().lower() 
            
            if user_choose == 'q' :
                break 
            elif user_choose == 't' :
                user_more = random.randint(0,5)