

tax_rate = 0.06 

def tax_payment(employeeSalary) :
    tax = employeeSalary * tax_rate 
    return tax  

def employeeSalaryPayment() :
    salry = input('employee salary ? ').strip() 
     
    
    try :
        salry = float(salry)
        tax = tax_payment(salry)
 
        with open('tax.txt', mode='w') as f :
            f.write(f"{tax}\n")
            
    except :
        print('only digit allowed!')
        # f.close()
    finally : 
          print('finally')
employeeSalaryPayment() 
   
 
 