import operator


def sum_of_intervals(intervals):
    
    ints = sorted(set(intervals), key=operator.itemgetter(0, 1))
    print(ints)
    
    range_sum = 0
    
    for i in range(len(ints)):
        if i == 0:
            range_start, range_end = ints[i]
        if i == len(ints) - 1:
            range_sum += max(range_end, ints[i][1]) - range_start
            return range_sum
        if ints[i+1][0] <= range_end:
            range_end = max(range_end, ints[i+1][1])
        else:
            range_sum += range_end - range_start
            range_start, range_end = ints[i+1]
    

if __name__ == '__main__':
    print(sum_of_intervals([(1, 5)]))
    print(sum_of_intervals([(1, 5), (3, 6)]))
    print(sum_of_intervals([(3, 6), (1, 5)]))
    print(sum_of_intervals([(1, 5), (6, 10)]))
    print(sum_of_intervals([(3, 4), (1, 5)]))
    print(sum_of_intervals([(1, 5), (3, 4)]))
    print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
    print(sum_of_intervals(
                [(228, 251), (-441, -131), (411, 417), (482, 485), (22, 349),
                 (91, 162), (-193, 88), (114, 204), (-148, -97), (-327, 417),
                 (-269, -256), (375, 499), (84, 166), (-87, 162), (51, 350),
                 (101, 286), (38, 112), (145, 498), (37, 474), (-326, -231)]))
