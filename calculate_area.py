""" 
the programm used to find the area of circle rectangulare and squre
"""
import math as m 
 ###########################################################################
def areaCircle(radius) :
    try : 
        radius = float(radius) 
        
        area = m.pi * radius ** 2 
        return f'the aread of circle is {area:.2f}' 
    except : 
        return 'enter a valid format data'
###########################################################################
def areaRectangulare(width, height) :
    try : 
        width = float(width) 
        height = float(height)
        area = width * height 
        return f'The area of a rctangulare is {area:.2f}'
    except : 
        return 'enter a valid format data'
###########################################################################
def areaSqure(area) : 
    
    try :
        area = float(area) 
        
        areaSqure = area ** 2  
        
        return f'The area of a squre is {areaSqure:.2f}'
    
    except : 
        return 'enter a valid format data'  
 

while True : 
    area = input('Do you want to calculate the area of (c/r/s)? ').strip()
    ###########################################################################
    if area == 'c' :
        radius = input('enter the radius of the circle ? ').strip() 
        print(areaCircle(radius))
    ###########################################################################
    elif area == 'r' : 
        width = input('enter the width of the rectangure ? ').strip() 
        height = input('enter the height of the rectanguler ? ').strip() 
        print(areaRectangulare(width, height))
    ###########################################################################
    elif area == 's' : 
        area = input('enter the area of a squre ? ').strip() 
        print(areaSqure(area))
    ###########################################################################
    else : 
        print('Invalid area shap, we can use this system to check area of circle, squre and rectangulre.')
    keep = input('Do you need to calculate any area (yes/no)? ').strip().lower() 
    
    if keep != 'yes' :
        break
    continue

    
    