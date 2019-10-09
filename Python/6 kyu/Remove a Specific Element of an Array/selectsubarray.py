import numpy as np

from itertools import combinations


def select_subarray(arr):
    
    def mul(lis):
        r = 1
        for x in lis:
            r *= x
        return r
    
    subarray_math = \
        [[sum(sub), mul(sub)] for sub in combinations(arr, len(arr)-1)]
    
    quotients = [np.abs(subproduct/subsum) if subsum else np.NaN
                 for (subsum, subproduct) in subarray_math[::-1]]
    
    mins = [i for i, q in enumerate(quotients) if q == min(quotients)]
    
    if len(mins) == 1:
        return [mins[0], arr[mins[0]]]
    else:
        return [[i, arr[i]] for i in mins]


if __name__ == '__main__':
    print(select_subarray([1, 23, 2, -8, 5]))
    print(select_subarray([1, 3, 23, 4, 2, -8, 5, 18]))
    print(select_subarray([10, 20, -30, 100, 200]))
    print(select_subarray([128, 64, 134, -120, 137, -118, 139, 142, 143, 16, -106,
                     23, -101, 156, 30, 159, 32, 34, 35, 198, -179, 41, -165,
                     -85, -82, 50, 181, -73, -200, 58, -197, 188, 61, -194,
                     -193, -64, 193, 194, -61, -113, -186, 73, -9, 77, -96, 80,
                     -47, -174, 163, -170, 87, -168, 89, 91, -34, -31, -158,
                     -29, 38, -183, 81, -152, -151, -146, 113, 83, -12, 117,
                     119, -136, -133,-132, 170]))
    print(select_subarray([135, -20, 139, 15, 144, 150, -39, -103, 155, 156, -99, -92,
                    -89, 40, 170, -84, -142, -82, -81, -79, 179, 52, 55, 184,
                    -199, -69, -66, 64, -63, 66, -60, -59, -185, 76, 79, -72,
                    82, -42, -168, 36, 90, 91, -35, 103, 104, -21, 108, -147,
                    -167, -143, 114, -141, 62, -136, 122, -5, 126]))
