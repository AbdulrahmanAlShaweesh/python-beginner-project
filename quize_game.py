
 
# this a quaze game build using python programming languges, 
# used to ask the user to enter a answer a chech if the answer 
# is correct or not and then display if the answer user types
# is coreect or not and at the end display the user's points.
def quizeGame(totalPoints, **quations) : 
    print('===========================================') 
    print('Welcome to Online quize game by python prog') 
    print('===========================================') 

    play = input('Do you want to play ? ').strip().lower()
    
    while play == 'yes' :
        
        for quation in quations : 
            quation_ = input(f'What does {quation} stands for ? ').strip().title() 

            if quation_ == quations[quation] :
                totalPoints += 1
                print('coreect answer'.capitalize())
            else :
                print('incorrect answer'.capitalize())
        
        play = input('Do you want to play again? ').strip().lower() 
        if play != 'yes' :
            print('--------------------------------')
            print(f'your total Point is {totalPoints} {"points".capitalize() if totalPoints > 1 else "point".capitalize()}')
            print(f'your total Percentage is {(totalPoints / len(quations.keys())) * 100} %')
            print('--------------------------------')
            break
        print('-----------------------------------------')

print('Okay, let\'s play.')

quations = {
    'CPU' : 'Center Processing Unit', 
    'GPU' : 'Graphic Processing Unit',
    'RAM' : 'Random Access Memory', 
    'PSU' : 'Power Supply Unit',
    'AI' :  'Artifical Intelagence'
}
totalPoints = 0 

quizeGame(totalPoints , **quations)