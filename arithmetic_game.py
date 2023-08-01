import random as r 
import time as t 


class ArithmeticGames : 
    
    def __init__(self, number_of_quations) :
        self.number_of_quations = number_of_quations 
    
    # this function is to return the quations and operator. 
    def numberAndOperator(self):
        self.number1 = r.randint(1,50) 
        self.number2 = r.randint(1, 50) 
        self.operators = r.choice(['+', '-', '/', '//', '*', '%', '**']) 
        
        return self.number1, self.number2, self.operators
    
    # this function used to generate the quations. 
    def generateQuation(self) : 
        if self.operators == '+' : 
            quation = self.number1 + self.number2 
        elif self.operators == '-' :
            quation = self.number1 - self.number2 
        elif self.operators == '/'  :
            quation = self.number1 / self.number2   
        elif self.operators == '//' :
            quation = self.number1 * self.number2   
        elif self.operators == '%' :                
            quation = self.number1 % self.number2   
        else : 
            quation = self.number1 ** self.number2   
        return quation
     
    # this function display the quation. 
    def quation(self) : 
        for i in range(self.number_of_quations) : 
            number1, number2, opertor = self.numberAndOperator()
            quation = self.generateQuation()
            print(quation)
            # answer = input(f'{number1} {opertor} {number2}? = ')
            
            # if answer == quation :
            #     pass
            
            # print(quation)x
play_game = ArithmeticGames(10) 

play_game.quation()