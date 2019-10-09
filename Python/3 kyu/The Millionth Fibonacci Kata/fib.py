def fib(num):
    
    def cal(n):
        if n == 0:
            return 0, 1
        elif n == 1:
            return 1, 1
        else:
            a, b = cal(n // 2)
            p = a * (2 * b - a)
            q = b * b + a * a
            if n % 2 == 0:
                return p, q
            else:
                return q, p + q
    
    if num >= 0:
        return cal(num)[0]
    else:
        if not num % 2:
            return -1 * cal(-num)[0]
        else:
            return cal(-num)[0]


if __name__ == '__main__':
    print fib(0)
    print fib(1)
    print fib(2)
    print fib(3)
    print fib(4)
    print fib(5)
    print fib(-6)
    print fib(-96)
    print fib(-95)
