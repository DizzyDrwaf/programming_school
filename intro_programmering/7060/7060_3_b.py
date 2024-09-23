i = 1
tal1 = 1  
tal2 = 1
nr = 1
antal = int(input("Hur många talfölder vill du ha?"))
antal = antal + 1
while i < antal:
    print(f'{nr}:', tal1)
    temptal = tal2 
    tal2 = tal1 + tal2
    tal1 = temptal
    i = i + 1
    nr = nr + 1