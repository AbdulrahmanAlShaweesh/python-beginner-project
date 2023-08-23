""" 
the programm used to find the area of circle rectangulare and squre
"""
import math as m 
 
def areaCircle(radius) :
    try : 
        radius = float(radius) 
        
        area = m.pi * radius ** 2 
        return f'the aread of circle is {area:.2f}' 
    except : 
        return 'enter a valid format data'


    
 

while True : 
    area = input('Do you want to calculate the area of (c/r/s)? ').strip()
    if area == 'c' :
        radius = input('enter the radius of the circle ? ').strip() 
        print(areaCircle(radius))
    
    