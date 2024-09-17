i = 1
tal1 = 1  
tal2 = 1
while i < 31:
    print(tal1)
    temptal = tal2 
    tal2 = tal1 + tal2
    tal1 = temptal
    i = i + 1

    