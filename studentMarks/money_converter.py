# show a welcoming message once the system starts.
print( )
print('Welcome to Money Change System') 
print('This System can change money from')
print('Egyptain Pound to [USD, Rial Saudi,]')
print(  )

# propot the imput from the user.
money = input('Enter the amount of money you need to change ? ').strip()  
country_currency = input('Enter the country\'s currency you to change ? ').strip().lower()

# check if user promot an empty input. 
if money == "" or country_currency == "" :
    if money == "" and country_currency == "":
        print('you need to enter a valid amount of money and country\'s currency')
    
    elif money == "" : 
        print('you need to enter a valid amount of money') 
        
    else  :
         print('you need to enter a valid country currency')  
# if the money user enter is in a digit format. 
elif money.isdigit : 
    if country_currency.isalpha : 
         
        if country_currency == 'usd' : 
            money_changed = float(money) * 0.03236 
            print('the money convert into ' + f'"{country_currency.upper()}"' + ' and the total is ' +  f'{"$" if country_currency == "usd" else "SR"}' + str(money_changed))
        elif country_currency == 'rial suadi' :
            money_changed = float(money) * 0.12219
            print('the money convert into ' + f'"{country_currency.upper()}"' + ' and the total is ' +  f'{"$" if country_currency == "usd" else "SR"}' + str(money_changed))
            
        else :
            print('this system can only change from egyptain pound to USD and Saudi Riyal')
        
    else :
        print('the country name should contains only letters.')  
else :
    print('invalid country name or money type.')

# print(1000 * 0.12219)
