def udda(a):
    temp = a % 2
    if temp == 1:
        svar = bool(True)
    else:
        svar = bool(False)
    return svar


print(udda(int(input("Tallet är udda?"))))