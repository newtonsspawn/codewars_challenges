from itertools import count


color = {
        'RR': 'R', 'GB': 'R', 'BG': 'R',
        'GG': 'G', 'RB': 'G', 'BR': 'G',
        'BB': 'B', 'RG': 'B', 'GR': 'B'
}


def next_col(col):
    return color[col]


def draw_pyramid(row, r, first=True):
    global initial_len
    if len(row) == 1:
        return row
    if first:
        string = ' '.join([j for j in row])
        initial_len = len(row)
        print(f'row {r + 1:02d}: ' + string)
    string = ' ' * (initial_len - r)
    for i in range(len(row) - 1):
        string += next_col(row[i] + row[i + 1]) + ' '
    print(f'row {r:02d}: ' + string)
    r -= 1
    return draw_pyramid(''.join(string.strip(' ').split(' ')), r, first=False)


def colorizer(string):
    if len(string) == 1:
        return string
    temp_string = ''
    for col in range(0, len(string)-1, 2):
        temp_string += next_col(string[col] + string[col+1])
    return colorizer(temp_string)


def triangle(row):
    
    # draw_pyramid(row, len(row) - 1)
    
    length_initial = len(row)
    
    if length_initial == 1:
        return row
    
    previous = [0]
    
    def minimize(length_temp=length_initial-1, included_items=None):
        if included_items is None:
            included_items = [0]
        temp_items = []
        if length_temp == 0:
            string = ''
            for col in range(0, len(included_items)-1, 2):
                string += next_col(row[int(included_items[col])] + row[int(included_items[col+1])])
            return colorizer(string)
        if length_temp > 1:
            for n in count(0):
                if (3**n + 1) > length_temp:
                    val = 3 ** (n - 1)
                    for item in included_items:
                        temp_items.append((val / 2) + item - (val / 2))
                        temp_items.append((val / 2) + item + (val / 2))
                    previous.append(val/2)
                    break
        if length_temp == 1:
            val = 1
            for item in included_items:
                temp_items.append(val/2 + item - val/2)
                temp_items.append(val/2 + item + val/2)
                previous.append(val/2)

        # print(sorted(temp_items))
        
        return minimize(length_temp - val, temp_items)
    
    return minimize()


if __name__ == '__main__':
    print(triangle('B'))
    print(triangle('GB'))
    print(triangle('RRR'))
    print(triangle('RGBG'))
    print(triangle('RBRGBRB'))
    print(triangle('RBRGBRBGGRRRBGBBBGG'))
    print(triangle(
            'GGRBBGRBRGBRGRGRBGGGGBBBGRBBGBBGGRGRBGGBRGGGRRGGBGBGRRBBBGGGBBGRRBBBBRGBBRRRBGGRGRGRBGBRBGBRBBGGGRGRGBGRBGBGRRGGBRRRRBGRGBRRRRRBGGRGGGBRGGGRBBBRGGBRGGGRGBGBGRRRRBBRGRBBGBGGRGGBGGBGRGBBGGBRBGRGBRRGGGGRGBGBBGBRBBBRRRBRRRGRRRBGRGBGRRRRGGRBBGGRBGRBRRGBBBGBGRGBRBGGRRRRRRBGBRBBRRRBRRRGBBRBBGBGGBGRRRGBGRGBBBGGRBGBBBGGRRBGRBBRRGBRGGGBBGGGGGRGGRBBRGGRBRGGGBRRGRGRBRRRBRBRGGGGGGRGGBBBBBGGGGRRBGBRGRBBBGRBBGRRRRRBGGRGRRRBRRBGRGBGRRBGBGGGGRBRBBBRRRRRBRRGRRRBRGRBGRBBBBGGGGGRRBBBBGBBGRGRBRBRRGGBRGRRGBGRRRRBGRGGBGGGBBRGGBGBBRRBBRRGRRGBGRRRGRBRBGGRRBBGBBBRGRRBRRBGBBRBGGRGRRRGRBBGGRBGBBBRGGRRGGRRRGGBRBGGGGRRGRGGBBGBGGBBGBGGBGBRRRRRGBG'))

    print(triangle('BRGRGBRGBBBRGBR'))
