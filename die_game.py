import random
class DieGame : 
    
    def __init__(self, startPlace, endPlace, userPlace, computerPlace, isUserWin, isComputerWin) : 
        self.startPlace = startPlace 
        self.endPlace = endPlace 
        self.userPlace = userPlace 
        self.computerPlace = computerPlace 
        self.isUserWin = isUserWin 
        self.isComputerWin = isComputerWin 
        
    def track_winer(self) :
        
        while not self.isUserWin or not self.isComputerWin : 
            user_input = input('enter "t" to quntinue and "Q" to quite (t/q)? ').strip().lower() 
            
            if user_input != 't' and user_input != 'q' :
                user_input = input('invalid chooise, please enter "t" to quntine or "q" to quite? ').strip().lower()
                
                if user_input != 'q' :
                    continue
                else :
                    print('------------------------------')
                    print('you choosed to leave the game')
                    print('Thank For playing this game.')
                    print('Goodbye...')  
                    print('------------------------------')
                    break
            elif user_input == 'q' : 
                print('------------------------------')
                print('Thank For playing this game.')
                print('Goodbye...') 
                print('------------------------------')
                break 
            
            elif user_input == 't'  : 
                user_random_picked = random.randint(1,6) 
                self.userPlace += user_random_picked 
                print(f'you have {self.endPlace - self.userPlace} left to win')
                
                computer_random_place = random.randint(1,6)
                self.computerPlace += computer_random_place
                print(f'you have {self.endPlace - self.computerPlace} left to win')
                
                 
                if self.userPlace > self.endPlace : 
                    overShotPlace  = self.userPlace - self.endPlace 
                    self.userPlace = self.endPlace - overShotPlace # calculate the userplace after removing the shot place.

                    if self.userPlace == 40 : 
                        self.isUserWin = True 
                        break
                
               
                
                if self.computerPlace > self.endPlace :
                    overshot_place = self.computerPlace - self.endPlace 
                    self.computerPlace = self.endPlace - overshot_place
                    
                    if self.computerPlace == 40  : 
                        self.isComputerWin = True 
                        break 
                 
            if self.userPlace == 40 :
                print('Congrats, you won')
                break
            elif self.computerPlace == 40 :
                print('Sorry, computer won' )
                break
        
    def checkWiner(self) : 
        winder  = self.checkWiner() 
        print(winder)
        # if userPlace == 40 :
        #     return 'Congrat, you won the game.'
        # elif computerPlace == 40 :
        #     return 'computer won the game'

die_game = DieGame(0, 40, 0, 0, False, False)

die_game.track_winer()
            