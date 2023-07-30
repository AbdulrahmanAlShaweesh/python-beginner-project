


class GroceryCasher :
    
    def __init__(self,) : 
        self.buyingList = {} 
        self.productsPrice = {'checken': 2, 'finish': 3, 'botato': 1, 'eggs' : 0.4, 'meat' : 3, 'tomato' : 0.3} 
    
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
                 

    def get_price(self) :
        item_price = 0
        sub_total = 0 
        print('Product\t\tQuintity\tPrice')
        print('.....................................')
        for product, quntity in self.buyingList.items(): 
            item_price = self.productsPrice[product] * quntity
            sub_total += item_price
            
            print(product + '\t\t ', str(quntity), '\t\t' , item_price)
        print('total price' + '\t\t\t', sub_total)
        print('.....................................')
      
    


buying  = {'checken' : 3, 'finish' : 4, 'botato': 10, 'eggs': 20}
total = 0

casher = GroceryCasher() 
print(casher.get_buying_items())
 

# for i, j in buying.items() :
    
    
#     sub = dictr[i] * j
#     print(f'price for {i} => {sub}')
#     print(sub)
 