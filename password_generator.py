
class PasswordGenerator : 
    
    def __init__(self): 
        pass 
    
    # this method generat a symbolm number, uppercase letters and lower cause letters. 
    def passwordContains(self) :
        upperCauseLetters = [chr(letter) for letter in range(65,91)]
        lowerCauseLetters = [chr(lowerLetter) for lowerLetter in range(97,123)]
        numbers = [number for number in range(0, 10)]
        symbols = [chr(sym) for sym in range(32, 48)]
        symbols += [chr(sym) for sym in range(58, 64)]
        symbols += [chr(sym) for sym in range(123, 127)]
        return upperCauseLetters, lowerCauseLetters, numbers, symbols
    
    # this method ask user for password length and chech if user input length valid and return
    # password length 
    @property
    def userDesiredPasswordLength(self) :
        userPasswordLength = input('Enter the password length ? ').strip() 
        uppercase = input('enter the number of uppercase letter you want ? ') 
        lowercase = input('enter the number of lowercase letter you want ? ') 
        numberinc = input('enter how many numbers you want your password includs? ')  
        symbols = input('enter how many symbols you want your password includs? ')  
        
        while any([userPasswordLength == "",uppercase == '', lowercase=='', numberinc == '', symbols == '']) : 
             
            userPasswordLength = input('Enter the password length ? ').strip() 
            uppercase = input('enter the number of uppercase letter you want ? ') 
            lowercase = input('enter the number of lowercase letter you want ? ') 
            numberinc = input('enter how many numbers you want your password includs? ')  
            symbols = input('enter how many symbols you want your password includs? ') 
        else : 
            try : 
                desiredPasswordLength = int(uppercase) + int(lowercase) + int(numberinc) + int(symbols)
                if userPasswordLength == desiredPasswordLength  : 
                    return int(userPasswordLength),  int(uppercase), int(lowercase), int(numberinc), int(symbols)
                else : 
                    return 'total password charcketers not match your desirebed passwprd length'
            except :
                return 'enter the length of the password, only digits allowed.'    
    @property
    def generatPassword(self) :
        passLength = self.userDesiredPasswordLength
        upperCauseLetters, lowerCauseLetters, numbers, symbols = self.passwordContains
        
        # if 
        return passLength
    
code = [chr(i) for i in range(65, 91)]

password = PasswordGenerator()

# upperCauseLetters, lowerCauseLetters, numbers, symbols = 
print(password.userDesiredPasswordLength)