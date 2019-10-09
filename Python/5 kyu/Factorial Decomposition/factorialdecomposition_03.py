def decomp(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(1, num):
            if i == 1:
                continue
            if num % i == 0:
                return False
        return True

    def sub(num, comps):
        for i in comps.keys():
            while num % i == 0:
                num /= i
                comps[i] += 1

    comps = {}

    for i in range(2, n+1):
        if i not in comps.keys() and is_prime(i):
            comps[i] = 0
        sub(i, comps)

    return " * ".join([f"{i}^{j}" if j > 1 else f"{i}" for i, j in comps.items()])
