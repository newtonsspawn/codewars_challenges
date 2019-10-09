def dbl_linear(n):
    
    u = [1]
    
    def func(nums):
        global fin
        new_nums = []
        for i in nums:
            new_nums.append(2 * i + 1)
            new_nums.append(3 * i + 1)
        u.extend(new_nums)
        if len(u) > n*12:
            fin = list(sorted(set(u)))
        else:
            func(new_nums)
        return fin[n]
    
    return func(u)


if __name__ == "__main__":
    print(dbl_linear(10))
    print(dbl_linear(500))
    print(dbl_linear(60000))
