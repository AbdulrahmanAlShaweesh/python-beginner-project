
# import random

# class DieGame :
    
#     def __init__(self, startPlace, endPlace, userPlace, computerPlace, userWins, computerWins) :
#         self.startPlace = startPlace 
#         self.endplace = endPlace 
#         self.userPlace = userPlace 
#         self.computerPlace = computerPlace 
#         self.userWins = userWins 
#         self.computerWins = computerPlace
    
#     def winer(self) :
        
#         while not self.userWins or not self.computerWins :
#             user_choose = input('enter t : to toss or q to quit the game ? ').strip().lower() 
            
#             if user_choose == 'q' :
#                 break 
#             elif user_choose == 't' :
#                 user_more = random.randint(0,5) 
#                 self.userPlace += user_more 
                
#                 if self.userPlace > 40 : 
#                     over_shot = self.userPlace - 40 
#                     self.userPlace = 40 -over_shot 

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
                break
            elif user_choose == 't' :
                pass
            else :
                print('invalid user choose'.capitalize())


die_game = DieGame(0, 40, 0, 0, False, False) 

die_game.checkWhosWiner()