i = 1
tal1 = 1  
tal2 = 1
nr = 1
antal = 1000
while i < antal + 1:
    
    if nr % 20 == 0:
        print(nr, tal1 / tal2)
    temptal = tal2 
    tal2 = tal1 + tal2
    tal1 = temptal
    i = i + 1
    nr = nr + 1

    