def next_smaller(n):
    
    n = list(str(n))
    
    if len(n) == 1:
        return -1
    
    i = len(n) - 1
    while n[i-1] <= n[i]:
        i -= 1
        if i == 0:
            return -1
    
    first, last = n[:i-1], n[i-1:]
    
    dig_to_move = max([x for x in n[i:] if x < n[i-1]])
    
    last.remove(dig_to_move)
    last = sorted(last, reverse=True)
    last.insert(0, dig_to_move)
    
    if not len(first) and last[0] == '0':
        return -1
    
    return int(''.join(first + last))


if __name__ == '__main__':
    print(next_smaller(907))
    print(next_smaller(21))
    print(next_smaller(531))
    print(next_smaller(1027))
    print(next_smaller(441))
    print(next_smaller(123456798))
    print(next_smaller(513))
    print(next_smaller(351))
    print(next_smaller(315))
    print(next_smaller(100))
    print(next_smaller(59884848483559))
    print(next_smaller(9999999999))
    print(next_smaller(19759037663779930133356677779999))
