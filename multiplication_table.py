
# def multiplicationTable(table_number, number):
#     for i in range(1, table_number+1) : 
#         table = ''
#         for j in range(1, number+1) :
#             print(f'{i} * {j} = {i * j}')
#         print('\t')

# table_number = int(input('Enter the multiplication table ? ').strip())
# number = int(input('enter number'))

def mutiplicationTable(tableNumber, number) : 
    
    print('Multiplication Table, by Al Sweigart al@inventwithpython.com')
    print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
    print('--|---------------------------------------------------')

    for table in range(0, tableNumber+1):
        print(str(table).rjust(2), end='')
        print('|', end='')
        for num in range(0, number+1):
            print(str(table * num).rjust(3), end=' ')
        print() 
        
tablenNumber = int(input('Enter table number? ').strip())
number = int(input('emter the number ? ').strip())
mutiplicationTable(tablenNumber,number)