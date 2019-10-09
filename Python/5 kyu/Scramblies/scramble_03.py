def scramble(s1, s2):

    for l in set(s2):
        if s2.count(l) > s1.count(l):
            return False

    return True


if __name__ == "__main__":
    scramble('rkqodlw', 'world')
    scramble('cedewaraaossoqqyt', 'codewars')
    scramble('katas', 'steak')
    scramble('scriptjava', 'javascript')
    scramble('scriptingjava', 'javascript')
    scramble('eqspppzgexxd', 'zkxiwmcizcrqimxhjv')