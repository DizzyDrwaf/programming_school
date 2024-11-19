svar = ""
alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ord = input("input ord:")
for steg in range(26):
    for bokstav in ord:
        if bokstav in alfa:
            sak = alfa.index(bokstav)
            svar += alfa[sak - steg]
        else: 
            svar += bokstav
    print(svar)
    svar = ""
