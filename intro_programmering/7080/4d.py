
def ctk(temp):
    return temp + 273.15

def ktc(temp):
    return temp - 273.15

def ctf(temp):
    return (9/5) * temp + 32

def ftc(temp):
    return (5/9) * (temp - 32)

def ktf(temp):
    tmp = ktc(temp)
    return ctf(tmp)

def ftk(temp):
    tmp = ftc(temp)
    return ctk(tmp)


i = "ja" 

while i == "ja":
    print("viken omvandling vill du göra?")
    print("| C till K | K till C | C till F | F till C | K till F | F till K |")
    print("      1          2          3          4          5          6")
    svar = int(input("input: "))
    if svar == 1:
        grad = ctk(float(input("vilken grad C vill du omvandla till K: ")))
        print(grad, " K")
    elif svar == 2:
        grad = ktc(float(input("vilken grad K vill du omvandla till C: ")))
        print(grad, " C")
    elif svar == 3:
        grad = ctf(float(input("vilken grad C vill du omvandla till F: ")))
        print(grad, "F")
    elif svar == 4:
        grad = ftc(float(input("vilken grad F vill du omvandla till C: ")))
        print(grad, "C")
    elif svar == 5:
        grad = ktf(float(input("vilken grad K vill du omvandla till F: ")))
        print(grad, "F")
    elif svar == 6:
        grad = ftk(float(input("vilken grad F vill du omvandla till K: ")))
        print(grad, "K")
    i = str.lower(input("vill du forsätta med en annan om vandling? : "))
