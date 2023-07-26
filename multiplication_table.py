
# def multiplicationTable(table_number, number):
#     for i in range(1, table_number+1) : 
#         table = ''
#         for j in range(1, number+1) :
#             print(f'{i} * {j} = {i * j}')
#         print('\t')

# table_number = int(input('Enter the multiplication table ? ').strip())
# number = int(input('enter number'))
print('Multiplication Table, by Al Sweigart al@inventwithpython.com')
print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
print('--|---------------------------------------------------')

for number1 in range(0, 13):
     print(str(number1).rjust(2), end='')
     print('|', end='')
     for number2 in range(0, 13):
         print(str(number1 * number2).rjust(3), end=' ')
     print() 