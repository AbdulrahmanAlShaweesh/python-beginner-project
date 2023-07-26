

def drow_tie_shap(number) : 
    
    for i in range(number) : 
        
        string = '*' * (i + 1)
        string += ' ' * (2 * (number - i - 1))
        string += '*' * (i + 1)
        print(string)
    for i in range(number - 1) :
        string = '*' *  (number - i - 1)
        string += ' ' * (2 * (i + 1))
        string += '*' * (number - i - 1)
        print(string)
drow_tie_shap(5)