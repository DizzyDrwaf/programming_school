tal = int(input("Mata in ett hel tal"))
if tal >= 0 and tal < 10:
    print("Ditt tal är ensiffrigt")
elif tal >= 10 and tal < 100:
    print("Ditt tal är tvåsiffrigt")
elif tal >= 100 and tal < 1000:
    print("Ditt tal är tresiffrigt")
elif tal >= 1000:
    print("Ditt tal är minst fyrsiffrigt")
else:
    print("Ditt tal är negatift.")