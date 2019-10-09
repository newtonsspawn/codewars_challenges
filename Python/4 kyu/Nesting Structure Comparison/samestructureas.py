def same_structure_as(original, other):
    
    if not type(original) == type(other):
        return False
    
    if not len(original) == len(other):
        return False
    
    def get_structure(lis, struct=[]):
        for i in range(len(lis)):
            if type(lis[i]) == list:
                struct.append(str(i) + ': yes')
                get_structure(lis[i], struct)
            else:
                struct.append(i)
        return struct
    
    return get_structure(original, []) == get_structure(other, [])


if __name__ == '__main__':
    print(same_structure_as([1, 1, 1], [2, 2, 2]))
    print(same_structure_as([1, [1, 1]], [2, [2, 2]]))
    print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
    print(same_structure_as([1, [1, 1]], [2, [2]]))
    print(same_structure_as([[[], []]], [[[], []]]))
    print(same_structure_as([[[], []]], [[1, 1]]))
    print(same_structure_as([1, [[[1]]]], [2, [[[2]]]]))
    print(same_structure_as([], 1))
    print(same_structure_as([], {}))
    print(same_structure_as([1, '[', ']'], ['[', ']', 1]))
