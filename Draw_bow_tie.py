


def drowTie(number) :
    
    for i in range(number) :
        string = '*' * (number - i) 
        string += '  ' * (i)
        string += '*' * (number - i)
        print(string)
    for j in range(number) : 
        string = '*' * (j+2)
        string += ' ' * (2 * (number - j - 1))
        string += '*' * (j+2)
        print(string)
        
number = int(input('enter number of tie ? ').strip())

drowTie(number)