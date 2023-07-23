
import random as rd

# this a number gussing game used to take the number from the user
# the prog generated a rando int number. if the user number match the
# prog random number it congrat the use for gussing the correct number
# and display how much time take to gusse the correct number.
def radnomNumberGussingGame(topRange, numberOfTryes) :
        random_number = rd.randint(0, topRange+1) 
         
        while True : 

            try :
                user_gussed = int(input('enter your gussing number? ').strip())
                numberOfTryes += 1

                # if the number entered by user is less than 0, will exit the prog
                if user_gussed <= 0 :
                    print('Please enter a number greate than 0') 
                    keep_playing = input('Do you want to keep playing ? ').strip().lower()
                
                    if keep_playing == 'yes' :
                        continue
                    else :
                        break

                 # if the number entered by user is greated than 0, will exit the follwing block if code
                elif user_gussed > 0 :
                    if user_gussed == random_number : 
                        print(f'you gussed the number correctly, in {numberOfTryes} {"tries" if numberOfTryes > 1 else "try"}')
                        keep_playing = input('Do you want to keep playing ? ').strip().lower() 
                        if keep_playing != 'yes' :
                            break 
                        else :
                            continue
                    if user_gussed > random_number : 
                        print('your gussed number is above the the random number') 
                    elif user_gussed < random_number :
                        print('your gussed number is below the random number') 
                    
                    # print('you did not gussed  the right number')
            except :
                print('only digits allowed'.capitalize()) 
                keep_play = input('Do you want to replay again ? ').strip().lower()
                
                if keep_play != 'yes' : 
                    break 
                else :
                    continue            
try :
    numberOfTryes = 0
    topRange = int(input('enter the top range number? ').strip())
    radnomNumberGussingGame(topRange, numberOfTryes)
except :
    print('only digits numbers allowed')
