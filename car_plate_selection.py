

def carPlateSelection(car_pates, odd_days, even_days, selected_plate):
    totay = input('enter today\'s day e.g(tu/mo/fi/su)? ').strip().lower()

    for plats in car_pates:
        try:
            plat = int(plats[-1])
            if totay in odd_days and plat % 2 == 0:
                selected_plate.append(plats)

            elif totay in even_days and plat % 2 != 0:
                selected_plate.append(plats)
            elif totay == 'su':
                selected_plate.append(plats)
        except:
            print('last car palt\'s should be interger number.')
            break
    return selected_plate


car_pates = ['AB1234', 'CD5678', 'EF901', 'GH234', 'JK567', 'LM8901']
odd_days = ['mo', 'we', 'fr']
even_days = ['tu', 'th', 'sa']
selected_plate = []
selected_plats = carPlateSelection(
    car_pates, odd_days, even_days, selected_plate)

print('*' * 50)
print('the plate selected for today\'s are:'.center(
    50, ' '), *selected_plats, sep='\n')
print('*' * 50)
############################################################################
# this using a dictionary.
############################################################################


def carPlateSelection(car_pates, even_odd_days, selected_plate):

    today = input('enter today\'s day e.g(tu/mo/fi/su)? ').strip().lower()

    for plats in car_pates:
        plat = int(plats[-1])
        if today in even_odd_days['even_days'] and plat % 2 == 0:
            selected_plate.append(plats)
        elif today in even_odd_days['odd_days'] and plat % 2 != 0:
            selected_plate.append(plats)
        elif today == 'su':
            selected_plate.append(plats)
        else:
            continue

    return selected_plate


selected_plate = []
car_pates = ['AB1234', 'CD5678', 'EF901', 'GH234', 'JK567', 'LM8901']
even_odd_days = {'even_days': ['mo', 'we', 'fr'],
                 'odd_days': ['tu', 'th', 'sa']}
plats = carPlateSelection(car_pates, even_odd_days, selected_plate)
print(*plats, sep='\n')
