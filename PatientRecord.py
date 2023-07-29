

 
def displayPationsRecord(**pations) :
   
   for names, pationsInfo in pations.items() :
       
       for key, value in pationsInfo.items() :
         print(f'name : {names} \n{key}  : {value}')
       print()

pations = {
           'Mohamed': {'age' : 23, 'height' : 1.9, 'weight' : 80}, 
           'Tom' : {'age' : 29, 'height' : 1.76, 'weight': 89}, 
           }
displayPationsRecord(**pations)
    
        

 


        
        