import math


def make_readable(seconds):

    hh = math.floor(seconds / 3600)
    mm = math.floor((seconds - (hh * 3600)) / 60)
    ss = math.floor((seconds - (hh * 3600) - (mm * 60)))

    readable_time = f'{hh:02}:{mm:02}:{ss:02}'

    return readable_time


if __name__ == '__main__':
    make_readable(0)
    make_readable(5)
    make_readable(60)
    make_readable(86399)
    make_readable(359999)