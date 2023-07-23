

def chooseYourOwnAdventureGame(name) :
    
    print('-----------------------------------------------')
    print('Welcome to Choose Your Own Adventure Game by Py') 
    print('-----------------------------------------------')

    while True : 
        answer = input(
            'you are in a drit road, it has come to the end and you can go left or right or back. Which way would you like to choose ?(left/right/back/q to exit) '
            ).strip().lower()
        
        # if user choose to exit the game
        if answer == 'q' :
            print(f'you choose to exit the game, thanks for tring this game {name}')
            break

        elif answer == 'left' :
            answer = input('you come to the river, do you want to walk around it , swim or take a boat? (walk/swim/boad)? ').strip().lower()

            if answer == 'walk' :
                answer = input('you walked and you came to a end of the road, do you want to go left or right(left/right)? ').strip().lower()

                if answer == 'left' :
                    print('you waked around and you wear killed by a keller :('.capitalize())
                    break
                elif answer == 'swim' :
                    print('you swim a creoss and you wear eaten by a shark'.capitalize())
                else :
                    print('you choose invalid choose'.capitalize())
                    break

            elif answer == 'swim' :
                    answer = input('you swim cross and you come to meet a shark, do you want to collect gun or knif(gun/knif)? ').strip().lower()
                    
                    if answer == 'gun' :
                        print('you swim across and you meet the sharka and pick up a gun to deinted your self and you wear eaten by shrak :('.capitalize())
                        break
                    elif answer == 'knif' :
                        print('you swim across and you meet the sharka and pick up a kinif to deinted your self and you wear eaten by shrak :('.capitalize())

                    else :
                        print('you choose invalid choose'.capitalize())
                        break
            else :
                print('you entered invalid options, please try to enter a valid option') 
                continue
        elif answer == 'back' :
            print('you choised to back and you lost!')
            break
        elif answer == 'right' :
            answer = input('you come to a bridge, it looks wobbly, do you want to cross or head back(cross/back)? ').strip().lower()
            if answer == 'back' : 
                answer = input('you go back to the main road, now you can decied to drive (left/right) ? ').strip().lower() 
                if answer == 'left' :
                    print('you decided to go left and you dead')
                elif answer == 'right' :
                    print('you choose to go right and you lost')
                else :
                    print('invalid choose, please try angain late')
                    continue
            elif answer == 'cross' :
                answer = input('you crossed arount and you meet a stranger, did you take to him ?(yes/no) ').strip().lower() 
                if answer == 'yes' : 
                    print('you meet the stranger and you take to him and he gave you a gift and you WON!')
                elif answer == 'no' :
                    print('you meet the stranger and you did not take to him, you lost.')
                else :
                    print('you enter invalid option.')
                    continue
            else : 
                print('you choosed invalid option, please try again later.') 
                continue
        else :
            print('you entered an invalid option, please try again or enter q to exit the game!')
name = input('enter your name ? ').strip().capitalize()
chooseYourOwnAdventureGame(name)

 