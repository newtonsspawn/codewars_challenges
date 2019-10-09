import re
from math import factorial as fact


def expand(expr):
    
    a, x, b, n = re.match('\(([-]*[\d]*)([a-z])([+-][\d]+)\)\^([\d]+)',
                          expr).groups()
    if not a:
        a = 1
    elif a == '-':
        a = -1
    else:
        a = int(a)
    b, n = int(b), int(n)
    
    coefs = []
    for k in range(0, n+1):
        coefs.append(int((fact(n) / (fact(n - k) * fact(k))) * a**(n-k) * b**k))
    
    string = ''
    if len(coefs) > 2:
        for l in range(0, len(coefs)-2):
            if coefs[l] > 1:
                string += '+' + str(coefs[l]) + x + '^' + str(len(coefs) - 1 - l)
            elif coefs[l] == 1:
                string += '+' + x + '^' + str(len(coefs) - 1 - l)
            elif coefs[l] == -1:
                string += '-' + x + '^' + str(len(coefs) - 1 - l)
            elif coefs[l] < -1:
                string += str(coefs[l]) + x + '^' + str(len(coefs) - 1 - l)
    if len(coefs) > 1:
        if coefs[-2] > 1:
            string += '+' + str(coefs[-2]) + x
        elif coefs[-2] == 1:
            string += '+' + x
        elif coefs[-2] == -1:
            string += '-' + x
        elif coefs[-2] < -1:
            string += str(coefs[-2]) + x
    if coefs[-1] > 0:
        string += '+' + str(coefs[-1])
    elif coefs[-1] < 0:
        string += str(coefs[-1])
    
    return string.lstrip('+')


if __name__ == '__main__':
    print(expand("(x+1)^0"))
    print(expand("(x+1)^1"))
    print(expand("(x+1)^2"))
    print(expand("(x-1)^0"))
    print(expand("(x-1)^1"))
    print(expand("(x-1)^2"))
    print(expand("(5m+3)^4"))
    print(expand("(2x-3)^3"))
    print(expand("(7x-7)^0"))
    print(expand("(-5m+3)^4"))
    print(expand("(-2k-3)^3"))
    print(expand("(-7x-7)^0"))
