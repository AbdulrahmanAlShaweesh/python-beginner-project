


class GroceryCasher :
    
    def __init__(self,) : 
        self.buyingList = {} 
        self.productsPrice = {'mango':1.2, 'apple': 0.99, 'checken': 2, 'finish': 3, 'botato': 1, 'eggs' : 0.4, 'meat' : 3, 'tomato' : 0.3} 
        self.membership = 'gold' 
        
    def get_buying_items(self) :
        
            try : 
                 
                items_number = int(input('how many product did you purchse? '.capitalize()).strip()) 
                
                for item in range(items_number) : 
                    product_name = input('enter product\'s name ? ').strip().lower() 
                    product_qunt = int(input(f'enter how many {product_name} you have ? '))
                    
                    self.buyingList.update({product_name : product_qunt})
                
                return self.buyingList
            except :
                print('only digits allowed')
            return self.buyingList
    
    # ------------------------------------------------------------
    @staticmethod 
    def welcome_user() : 
        print('*****************************************')
        print('wecome to online shopping card.'.center(40, ' '))
        print('*****************************************')
    
    # get price 
    def price(self, totalPrice) :
        self.price = totalPrice
         
    
    @property 
    def get_discount(self) :
        
        if self.price >= 55 and self.membership == 'gold': 
            self.price_after_des = self.price * 0.85
            return self.price_after_des, '15%'
        else :
            return self.price, '0 %'
            
        
    def get_price(self) :
        item_price = 0
        sub_total = 0 
        print('Product\t\tQuintity\tPrice')
        print('.....................................')
        for product, quntity in self.buyingList.items(): 
            item_price = self.productsPrice[product] * quntity
            sub_total += item_price
            
            print(product + '\t\t ', str(quntity), '\t\t' , round(item_price,2))
        print('.....................................')
        self.price(sub_total)
        print('total price' + '\t\t\t', round(sub_total,2 ))
        print('total descount' + '\t\t\t', round((sub_total - self.get_discount[0]), 2))
        print('.....................................')
        print('total price' + '\t\t\t', round(self.get_discount[0], 2))
        print('total descout' + '\t\t\t', self.get_discount[1])
        
        print('.....................................')
    # -------------------------------------------------------------
    


buying  = {'checken' : 3, 'finish' : 4, 'botato': 10, 'eggs': 20}
total = 0

casher = GroceryCasher() 
 
def user_interface() : 
    
    casher.welcome_user()
    while True : 
        
        items = input('Do you want to see products, or add items and q to exit(see/add/q) ? ').strip().lower() 
        
        if items == 'see' : 
            if len(casher.buyingList.keys()) == 0 :
                print('You do not have a products to display.')
            else :
                casher.get_price() 
        elif items == 'add' : 
            casher.get_buying_items() 
        elif items == 'q' :
           break 
        else :
             print('invalid options')
        
        
user_interface() 

        
 
 