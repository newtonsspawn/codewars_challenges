def elder_age(m, n, l, t):
    
    def larger(x, temp=1):
        while temp < x:
            temp <<= 1
        return temp
    
    def sum_range(lf, r):
        ans = (lf + r) * (r - lf + 1) // 2
        return ans
    
    if m == 0 or n == 0:
        return 0
    elif m > n:
        m, n = n, m
    
    lm, ln = larger(m), larger(n)
    if l > ln:
        return 0
    
    if lm == ln:
        tm = (sum_range(1, ln - l - 1) * (m + n - ln) +
              elder_age(ln - n, lm - m, l, t)) % t
        return tm
    elif lm < ln:
        lm = ln // 2
        tmp = sum_range(1, ln - l - 1) * m - (ln - n) * sum_range(
            max(lm - l, 0), ln - l - 1)
        if l <= lm:
            tmp += (lm - l) * (lm - m) * (ln - n) + elder_age(lm - m, ln - n, 0,
                                                              t)
        else:
            tmp += elder_age(lm - m, ln - n, l - lm, t)
        return tmp % t


if __name__ == '__main__':
    print(elder_age(8, 5, 1, 100))  # 5
    print(elder_age(8, 8, 0, 100007))  # 224
    print(elder_age(25, 31, 0, 100007))  # 11925
    print(elder_age(5, 45, 3, 1000007))  # 4323
    print(elder_age(31, 39, 7, 2345))  # 1586
    print(elder_age(545, 435, 342, 1000007))  # 808451
    print(elder_age(28827050410, 35165045587, 7109602, 13719506))  # 5456283
