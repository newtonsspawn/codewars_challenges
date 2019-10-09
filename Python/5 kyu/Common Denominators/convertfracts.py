from math import gcd
from functools import reduce


def convertFracts(lst):
    
    if not lst: return []

    def lcm(denoms):
        return reduce(lambda a, b: a * b // gcd(a, b), denoms)
    
    denom = lcm([d for n, d in lst])
    
    fracs = [[n * int((denom/d)), denom] for n, d in lst]
    
    return fracs


if __name__ == '__main__':
    print(convertFracts([]))
    print(convertFracts([[1, 2], [1, 3], [1, 4]]))
    print(convertFracts([[5, 7], [3, 21], [1, 2]]))
    print(convertFracts([[27115, 5262], [87546, 11111111], [43216, 255689]]))
