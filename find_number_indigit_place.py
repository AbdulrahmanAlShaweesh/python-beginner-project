# this project used to ask the user for a three digits number
# and then ask the user which digit number needs to display. 

print('please enter a 3 digits numbers and' )
print('the follow by the index or digit of' ) 
print('the signle number you me to show display' )
print()
def showNumberInDigitPlace(number, digitSelected) :
    
    try : 
        number = int(number) 
         
        if digitSelected != '' :
            num = 0
            if digitSelected == 'first' : 
                num = number % 10 
                
            elif digitSelected == 'second' :
                num = (number // 10) % 10 
             
            else : 
                num = (number // 100) % 100 
            return num 
        else :
            return 'please enter number place'
    except : 
        return 'enter a valid data'
number = '235'


# keep asking the used to enter the index of a number until entern yes to quit the syetem
# then the system will quit. 
while True :
    digitSelected = input('enter which digit number do you want to see e.g(first/second/third) ? ').strip().lower()
    print(showNumberInDigitPlace(number, digitSelected))
    
    keep = input('Do you want to quit the system(yes/now)? ').strip().lower()
    if keep != 'yes' :
        continue 
    print('Thanks For using our system.')
    print('GoodBye :).')
    break 
     