i = 1
tal1 = 1  
tal2 = 1
nr = 1
while i < 31:
    print(f'{nr}:', tal1)
    temptal = tal2 
    tal2 = tal1 + tal2
    tal1 = temptal
    i = i + 1
    nr = nr + 1

    