

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
#################################################################
def maxNumber(*numbers) : 
      
    
    try : 
        number = 0 
        
        for num in numbers : 
            num = float(num)
            if num > number : 
                number = num 
        return number
    except : 
        return 'enter a valid numbers'
##################################################################
def minNumber(*numbers) : 
    try : 
        minNumber = None
        for number in numbers :
            
            number = float(number)
            if minNumber is None  or number < minNumber : 
                minNumber = float(number)
        return minNumber
    except : 
        return 'enter a valid numbers'
##################################################################
msg = 'Do you want to find the max number of a give numbers/ min number/sum of a number? '
mesg = input(msg).strip().lower()

if mesg == 'sum' : 
    
    number = input('enter a number and will find the sum of it for you ? ').strip()
    total = sumOfNumber(number)
    print(f'The sum of the number {number} is "{total}".')
elif mesg == 'max' : 
    numbers = input('enter a numbers ? ') 
    
    numbers = numbers.split()
    maxNumber = maxNumber(*numbers) 
    print(f'The maximum Number is {maxNumber}')
elif mesg == 'min' : 
    numbers = input('enter a numbers ? ') 
    
    numbers = numbers.split()
    minNumbers = minNumber(*numbers) 
    print(f'The minimum Number is {minNumbers}')
