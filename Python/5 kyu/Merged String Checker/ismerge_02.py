import collections


def is_merge(s, part1, part2):
    
    if collections.Counter(s) != collections.Counter(part1 + part2):
        return False

    i, j = 0, 0
    while j < len(part1):
        if i == len(s):
            return False
        if part1[j] == s[i]:
            j += 1
        i += 1

    i, j = 0, 0
    while j < len(part2):
        if i == len(s):
            return False
        if part2[j] == s[i]:
            j += 1
        i += 1
  
    return True


if __name__ == '__main__':
    # is_merge('codewars', 'code', 'wars')
    # is_merge('codewars', 'cdw', 'oears')
    # is_merge('codewars', 'cod', 'wars')
    # is_merge('codewars', '', 'codewars')
    # is_merge('Making progress', 'Mak pross', 'inggre')
    # is_merge('codewars', 'cwdr', 'oeas')
    # is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am')
    is_merge('codewars', 'code', 'wasr')
