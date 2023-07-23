
import random as rd

# this a simple rock paper and scissor game using python
def RockPaperScissorGame(userWins, computerWins, options) :

    print('=============================================================') 
    print('Welcome to Online rock, paper and scissor game by python prog') 
    print('=============================================================')

    while True : 

        try : 
            user_choise = input('enter Rock/Paper/Scissor or Q to quit the prog ? ').strip().lower()
            
            if user_choise == 'q' :
                print('thanks for playing rock, paper and scissor game')
                print('goodbye')
                break
            
            elif user_choise not in options :
                print('Invalid choise, please try to type a valid choise!')
                continue

            else :  
                # let the computer choise a random value for the rock, paper and scissor from the list above
                computer_choise = rd.choice(options)
                print(f'your pick {user_choise} Vs. computer pick {computer_choise}')
                if user_choise == 'rock' and computer_choise == 'paper' :
                    print('you won!') 
                    userWins += 1

                elif user_choise == 'paper' and computer_choise == 'rock' :
                    print('you won!') 
                    userWins += 1 
                    
                elif user_choise == 'scissor' and computer_choise == 'paper' :
                    print('you won!') 
                    userWins += 1

                else :
                    print('computer won!') 
                    computerWins += 1
                keep_playing = input('Do you want to keep playing this game? (Y/N) ? ').strip().lower() 
                if keep_playing == 'yes' or keep_playing == 'y' :
                    continue 
                else : 
                    print('---------------------------------')
                    print(f'You won {userWins} {"times" if userWins > 1 else "won"}')
                    print(f'Computer wons {computerWins} {"times" if computerWins > 1 else "time"}')
                    print('----------------------------------')
                    break
        except : 
            print('invlid input')

UserWarning = 0 
computerWins = 0
options = ['rock', 'paper', 'scissor']
RockPaperScissorGame(UserWarning, computerWins, options)