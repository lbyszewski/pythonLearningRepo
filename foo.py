

def fibb(n):
    if(n<3):
        return 1
    else:
        return fibb(n-2) + fibb(n-1)

def silnia(n):
    if(n == 0):
        return 1
    else:
        return n*silnia(n-1)

def ropietoscPrzedzialu(p,k,d):
    for przedzial in range(p,k+1):
        if(przedzial % d == 0):
            print(przedzial)