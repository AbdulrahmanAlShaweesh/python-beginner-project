

# caculate Sum of a number etered by user. 

def sumOfNumber(numbers) : 
    
    # try cascat the number and find the sum of the number if 
    # user entered a digits only
    try : 
        total = 0
        numbers = int(numbers) 
        
        for number in range(numbers + 1) : 
            total += number 
        return total
    # provide the error message if the user input can not be
    # cascated to interger value. 
    except :
        
        return 'Only digits allowed' 
number = input('enter a number and will find the sum of it for you ? ').strip()
print(sumOfNumber(number))