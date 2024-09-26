svar = int(input("Gissa ett nummer."))

while svar != 42:
    if svar < 42: 
        svar = int(input("För litet gissa igen."))
    elif svar > 42: 
        svar = int(input("För stort gissa igen."))
print("Rätt wow!!!!")