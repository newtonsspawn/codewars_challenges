from functools import reduce


def last_digit(numbers):
    
    def get_exp(n):
        
        if n <= 4:
            return n
        
        if n % 100 > 1:
            end = n % 100
        else:
            end = n % 1000

        if end % 4 == 0:
            exp = 4
        else:
            exp = end % 4

        if exp > 1:
            ans = exp
        else:
            ans = end
        
        return ans
    
    if not numbers:
        return 1
    elif len(numbers) == 1:
        return numbers[0] % 10
    elif len(numbers) == 2:
        expo = numbers[1]
    else:
        expo = reduce(lambda y, x: x ** get_exp(y), numbers[1:][::-1])
    
    return ((numbers[0] % 10) ** get_exp(expo)) % 10


if __name__ == '__main__':
    print(last_digit([]))                           # 1
    print(last_digit([0, 0]))                       # 1
    print(last_digit([0, 0, 0]))                    # 0
    print(last_digit([1, 2]))                       # 1
    print(last_digit([3, 4, 5]))                    # 1
    print(last_digit([4, 3, 6]))                    # 4
    print(last_digit([7, 6, 21]))                   # 1
    print(last_digit([12, 30, 21]))                 # 6
    print(last_digit([2, 2, 2, 0]))                 # 4
    print(last_digit([937640, 767456, 981242]))     # 0
    print(last_digit([123232, 694022, 140249]))     # 6
    print(last_digit([499942, 898102, 846073]))     # 6
