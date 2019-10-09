import re


def solution(args):
    
    statement = ''
    
    diffs = [args[i] - args[i-1] for i in range(1, len(args))]
    diffs.insert(0, 0)
    
    diffs = ''.join([str(i) for i in diffs])

    matches = []
    
    def repl(m):
        matches.append(m.group())
        return ("+" * len(m.group()[:-2])).format(m.group()[:-2]) + "-e"
    
    pattern = re.compile(r"1[1+]*1")
    diffs = re.sub(pattern, repl, diffs)
    
    for i in range(len(diffs)):
        if diffs[i] == "+":
            continue
        elif diffs[i] == "-":
            statement += "-" + str(args[i+1]) + ","
        else:
            statement += "," + str(args[i])
    
    statement = re.sub(",,-*\d+", "", statement[1:])
    
    return statement
    

if __name__ == '__main__':
    print(solution(
            [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18,
             19, 20]))
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
    print(solution([1, 2, 3, 4, 5]))
    print(solution(
            [-94, -93, -91, -88, -86, -84, -83, -80, -78, -75, -72, -70,
             -67, -65, -63, -60, -59, -57, -55, -54, -52, -50, -48, -46,
             -45, -43, -41, -38]))
    print(solution(
            [-64, -61, -60, -59, -57, -55, -54, -53, -51, -49, -47, -46,
             -43, -42, -41, -40, -39, -38, -36, -34, -31, -28, -27, -25,
             -23, -21, -18]))
    print(solution(
            [-52, -49, -46, -45, -42, -39, -36, -34, -32, -31, -28, -26,
             -24, -23, -22, -19, -16, -13, -12, -9, -6, -4, -2, -1, 2]))
    print(solution(
            [-93, -90, -88, -85, -82, -80, -79, -77, -75, -74, -71, -69,
             -67, -66, -63, -61, -59, -57, -56, -54, -52, -51, -48, -47,
             -45, -44, -42, -40]))
    print(solution(
            [-84, -83, -82, -79, -76, -75, -74, -71, -70, -69, -67, -66,
             -63, -61, -60, -57, -55, -52, -50, -47, -45, -43, -41, -39,
             -36, -33, -30, -27, -24, -23, -22]))
    print(solution(
            [-52, -50, -49, -46, -44, -41, -39, -37, -35, -34, -33, -31,
             -29, -27, -25, -23, -22, -21, -20]))
    print(solution(
            [-62, -59, -57, -55, -54, -51, -50, -48, -47, -44, -43, -41]))
