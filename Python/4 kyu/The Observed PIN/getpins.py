import itertools as it


def get_pins(observed):
    
    adj_dict = {
            '0': ['0', '8'],
            '1': ['1', '2', '4'],
            '2': ['1', '2', '3', '5'],
            '3': ['2', '3', '6'],
            '4': ['1', '4', '5', '7'],
            '5': ['2', '4', '5', '6', '8'],
            '6': ['3', '5', '6', '9'],
            '7': ['4', '7', '8'],
            '8': ['5', '7', '8', '9', '0'],
            '9': ['6', '8', '9']
    }
    
    adj_nums = []
    
    for c in str(observed):
        adj_nums.append(adj_dict[c])
    
    pins = [''.join(pin) for pin in list(it.product(*adj_nums))]
    
    return sorted(pins)


if __name__ == '__main__':
    print(get_pins('2'))
    print(get_pins('8'))
    print(get_pins('0'))
    print(get_pins('11'))
    print(get_pins('58'))
    print(get_pins('46'))
    print(get_pins('369'))
    print(get_pins('007'))
    print(get_pins('9173'))
    print(get_pins('1357'))
    print(get_pins('00000000'))
