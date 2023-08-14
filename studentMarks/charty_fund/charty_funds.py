

class ChartyFunds  : 
    counter = 0  # class attrubute
    def __init__(self, balance): 
        self.balance = balance # instance attrubute
    
    
    # instance methods
    def saveFunds(self, depositeAmount) :
        self.balance += depositeAmount 
    
    def spendFunds(self, spendAmount) :
        self.balance -= spendAmount  
    
    def inverstment(self, rate) :
        self.balance += (self.balance * rate) 
    
    def warning(self):
        
        if self.balance < 5000 : 
            return 'Your balance is down of the limit' 
        return self.balance 
charty = ChartyFunds(5000)



def userInput() : 
    inputData = input('Do you wan to save/withdrow/check state/investe ? ').strip().lower() 
    
    if inputData == 'save' : 
        charty.saveFunds(1000)
        print( charty.warning())
    elif inputData == 'withdrow' :  
        charty.spendFunds(2500)  # 'Your balance is down of the limit'
        print( charty.warning())
    elif inputData == 'check' :
            print(charty.warning())
    elif inputData == 'investe' : 
        rate = input('enter the rate of investment ? ').strip()
        
        if rate.isdigit : 
            rate = float(rate) 
            charty.inverstment(rate)
            print(charty.warning())
        return 'please enter a digits values'
userInput() 