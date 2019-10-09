from itertools import product


def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def gen_prime_digs(a, b):
    PRIMES = ['2', '3', '5', '7']
    nums = []
    for i in range(len(str(a)), len(str(b)) + 1):
        for j in list(product(PRIMES, repeat=i)):
            num = int(''.join(j))
            if a <= num < b:
                nums.append(num)
    return nums


def get_total_primes(a, b):
    count = 0
    for i in gen_prime_digs(a, b):
        if is_prime(i):
            count += 1
    return count


if __name__ == '__main__':
    get_total_primes(10, 100)
    get_total_primes(500, 600)
