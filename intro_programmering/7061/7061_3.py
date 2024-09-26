svar = int(input("Gissa ett nummer."))
a = 1
while svar != 42 and a < 4:
    if svar < 42: 
        svar = int(input("För litet gissa igen."))
    elif svar > 42: 
        svar = int(input("För stort gissa igen."))
    a = a + 1
if svar == 42:
    print("Rätt wow!!!!")
elif a == 4:
    print("Tyvärr du förlorade")