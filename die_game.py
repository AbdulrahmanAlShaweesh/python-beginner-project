
import random


class DieGame :
    
    def __init__(self, startPlace, endPlace, userPlace,computerPlace, isUserWins, isComputerWins) :
        self.startPlace = startPlace 
        self.endPlace = endPlace 
        self.userPlace = userPlace 
        self.computerPlace = computerPlace 
        self.isUserWins = isUserWins 
        self.isComputerWins = isComputerWins
    
    def checkWhosWiner(self) :
        
        while not self.isUserWins or not self.isComputerWins :
            user_choose = input('do you want to continus (t/q) ? '.capitalize()).strip().lower() 
            
            if user_choose == 'q' :
                print('game over!'.capitalize())
                print(f'you need {40 - self.userPlace} place to win')
                break
            if user_choose == 't' :
                
                user_pick_value = random.randint(1,5)
                self.userPlace += user_pick_value 
                print(f'you need {self.userPlace} Place to win')
                
                # computer place 
                computer_pick_value = random.randint(1,5) 
                self.computerPlace += computer_pick_value 
                print(f'computer needs {self.computerPlace} Place to win')
                
                
                if self.userPlace > self.endPlace  : 
                    user_over_shot_place = self.userPlace - self.endPlace 
                    self.userPlace = self.endPlace - user_over_shot_place 
                    
                    if self.userPlace == 40 : 
                        self.isUserWins = True 
                        break 
                    
                elif self.computerPlace > self.endPlace  : 
                    computer_over_shot_place =  self.computerPlace - self.endPlace 
                    # if the overshot is 0, the computer will has exact 40 place
                    self.computerPlace = self.endPlace - computer_over_shot_place 
                    
                    if self.computerPlace == 40 :
                        self.isComputerWins = True
                        break
                    
            else :
                print('invalid user choose'.capitalize())
        if self.userPlace == 40 :
            print('You won') 
        elif self.computerPlace == 40 :
            print('computer won'.capitalize())
        # if self.userPlace == 40 :
        #     print('you won')t
die_game = DieGame(0, 40, 0, 0, False, False) 

die_game.checkWhosWiner()