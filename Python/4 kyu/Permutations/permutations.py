import itertools


def permutations(string):
    
    return [''.join(strn) for strn in
            list(set(itertools.permutations(string, len(string))))]


if __name__ == '__main__':
    print(sorted(permutations('a')))
    print(sorted(permutations('ab')))
    print(sorted(permutations('aabb')))
