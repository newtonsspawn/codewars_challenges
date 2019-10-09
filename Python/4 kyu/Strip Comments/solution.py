import re


def solution(string, markers):
    
    if not markers:
        return string
    
    for marker in markers:
        if marker in ".?$^*-§":
            marker = '\\' + marker
        
        string = re.sub(f"[ ]*{marker}[^\n]*", '', string)
    
    return string.strip(" ")


if __name__ == '__main__':
    
    print(solution("apples, pears # and bananas\ngrapes\nbananas !apples",
                   ['#', '!']))

    print(solution("a #b\nc\nd $e f g", ['#', '$']))

    print(solution("apples, pears # and bananas\ngrapes\nbananas !#apples",
                   ['#', '!']))
    
    print(solution("apples, pears # and bananas\ngrapes\nbananas #!apples",
                   ['#', '!']))
    
    print(solution("apples, pears # and bananas\ngrapes\navocado @apples",
                   ['@', '!']))
