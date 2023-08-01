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
    
    def generateQuation(self) : 
        if self.operators == '+' : 
            answer = self.number1 + self.number2 
        elif self.operators == '-' :
            answer = self.number1 - self.number2 
        elif self.operators == '/'  :
            answer = self.number1 / self.number2 
        elif self.operators == '//' :
            answer = self.number1 * self.number2 
        elif self.operators == '%' : 
            answer = self.number1 % self.number2 
        else : 
            answer = self.number1 ** self.number2
        return answer
     
    # this function display the quation. 
    def quation(self) : 
        number1, number2, opertor = self.numberAndOperator()
        quation = input(f'{number1} {opertor} {number2}? = ')
        print(quation)
play_game = ArithmeticGames(10) 

play_game.quation()