def score(dice):
    
    points = 0
    
    values = [dice.count(i) for i in range(1, 7)]
    
    points += sum([a*b for a, b in zip([a//3 for a in values],
                                       [1000, 200, 300, 400, 500, 600])])
    
    if values[0] > 2:
        values[0] -= 3
    if values[4] > 2:
        values[4] -= 3
    
    points += sum([a*b for a, b in zip(values, [100, 0, 0, 0, 50, 0])])
    
    return points


if __name__ == '__main__':
    print(score([2, 3, 4, 6, 2]))
    print(score([4, 4, 4, 3, 3]))
    print(score([2, 4, 4, 5, 4]))
    print(score([5, 1, 3, 4, 1]))
    print(score([1, 1, 1, 3, 1]))
