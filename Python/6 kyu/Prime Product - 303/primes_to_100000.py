import math


def is_prime(num):
    flag = True
    if num > 1:
        for i in range(2, int(math.ceil(num / 2)) + 1):
            if (num % i) == 0:
                flag = False
                return flag
    else:
        flag = False
    return flag


primes = [i for i in range(3, 100000, 2) if is_prime(i)]
primes = [2] + primes

print(primes)
