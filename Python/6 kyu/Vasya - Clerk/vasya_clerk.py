def tickets(people):

    d_25, d_50, d_100 = 0, 0, 0
    success = "YES"

    def make_change(d):
        flag = False
        for i50 in range(d_50 + 1)[::-1]:
            for i25 in range(d_25 + 1):
                if ((25 * i25) + (50 * i50)) == (d - 25):
                    flag = True
                    return flag, i25, i50
        return flag, 0, 0

    for person in people:
        if person == 25:
            d_25 += 1
        elif person == 50:
            f, a, b = make_change(50)
            if not f:
                success = "NO"
                return success
            else:
                d_25 -= a
                d_50 -= b
            d_50 += 1
        else:
            f, a, b = make_change(100)
            if not f:
                success = "NO"
                return success
            else:
                d_25 -= a
                d_50 -= b
            d_100 += 1

    return success


if __name__ == '__main__':
    tickets([25, 25, 50])
    tickets([25, 100])
