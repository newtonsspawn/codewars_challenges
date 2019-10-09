def is_interesting(number, awesome_phrases):
    
    def check(num):
        if num < 100:
            return False
        if num in awesome_phrases:
            return True
        num = str(num)
        if num[1:] == '0' * len(num[1:]):
            return True
        if [int(num[i + 1]) - int(num[i]) for i in range(len(num) - 1)] == [
                0] * (len(num) - 1):
            return True
        if len(num) % 2 == 0 and (
                num[:int(len(num) / 2)] == num[int(len(num) / 2):][::-1]):
            return True
        if len(num) % 2 != 0 and (
                num[:int(len(num) / 2)] == num[int(len(num) / 2) + 1:][::-1]):
            return True
        if [int(num[i + 1]) - int(num[i]) for i in
            range(len(num) - 1)] == [
                -1] * (len(num) - 1):
            return True
        new_num = []
        for i in str(num):
            if i == '0':
                new_num.append('10')
            else:
                new_num.append(i)
        if [int(new_num[i + 1]) - int(new_num[i]) for i in
            range(len(new_num) - 1)] == [
                1] * (len(new_num) - 1):
            return True
    
    if check(number):
        return 2
    if check(number + 1) or check(number + 2):
        return 1
    
    return 0


if __name__ == '__main__':
    print(is_interesting(1, []))
    print(is_interesting(7382, []))
    print(is_interesting(99919911, []))
    print(is_interesting(800000, []))
    print(is_interesting(9999999, []))
    print(is_interesting(256, [1337, 256, 376006]))
    print(is_interesting(7473747, []))
    print(is_interesting(67890, []))
    print(is_interesting(234567890, []))
    print(is_interesting(987654321, []))
    print(is_interesting(799999, []))
    print(is_interesting(442, []))
    print(is_interesting(7473745, []))
    print(is_interesting(234567889, []))
