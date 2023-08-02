



import random 
import time

def arithmaticGame() :
    
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50) 
    operations = random.choice(['+', '-', '*','//'])
    print(number1, number2, operations)
    
    if operations == '+' : 
        answer = number1 + number2 
    elif operations == '-' : 
        answer = number1 - number2
    elif operations == '*' : 
        answer = number1 * number2 
    else : 
        answer = number1 // number2 
    quation = f'{number1} {operations} {number2} = '
    return answer, quation

def userAnswer(number_of_quation): 
    
    try :
         
        start_time = time.time() 
        
        counter = 0
        for i in range(number_of_quation):
            correctAnswer, quation = arithmaticGame()
             
            quation = int(input(quation.strip() + ' ')) 
            # waiting = time.sleep()
            end_time = time.time() 
            if end_time - start_time > 6 :
                print('you took to long to answer the quaton, try to be fast next time.')
                continue
            else :
                print(end_time - start_time)
                if quation != correctAnswer : 
                    print('wrrong answer.')
                else :
                    counter += 1
                    print('correct answer.')
        # print(waiting)
        return counter
    except : 
        print('error')
    
marks = userAnswer(3)
print(marks)