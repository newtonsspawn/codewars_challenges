import re


def mix(s1, s2):
    
    statement = ''
    
    s1 = re.sub("[^a-z]", "", s1)
    s2 = re.sub("[^a-z]", "", s2)
    
    d1, d2 = {}, {}
    
    for c in s1:
        if c in d1.keys():
            d1[c] += 1
        else:
            d1[c] = 1
            
    for c in s2:
        if c in d2.keys():
            d2[c] += 1
        else:
            d2[c] = 1
    
    max_counts = []
    
    for key in d1.keys():
        if key in d2.keys():
            if d1[key] > d2[key] and d1[key] > 1:
                max_counts.append([d1[key], '1:' + str(key * d1[key])])
            elif d2[key] > d1[key] and d2[key] > 1:
                max_counts.append([d2[key], '2:' + str(key * d2[key])])
            elif d2[key] == d1[key] > 1:
                max_counts.append([d1[key], '=:' + str(key * d1[key])])
    
    for key in d1.keys():
        if key not in d2.keys():
            if d1[key] > 1:
                max_counts.append([d1[key], '1:' + str(key * d1[key])])

    for key in d2.keys():
        if key not in d1.keys():
            if d2[key] > 1:
                max_counts.append([d2[key], '2:' + str(key * d2[key])])

    sorted_counts = []
    
    counts = (sorted(set([i[0] for i in max_counts]), reverse=True))
    
    for i in counts:
        for item in sorted([j[1] for j in max_counts if j[0] == i]):
            sorted_counts.append(item)

    statement = '/'.join(sorted_counts)
    
    return statement


if __name__ == '__main__':
    print(mix('Are they here', 'yes, they are here'))
    print(mix('looping is fun but dangerous',
              'less dangerous than coding'))
    print(mix(' In many languages', " there's a pair of functions"))
    print(mix('Lords of the Fallen', 'gamekult'))
    print(mix('codewars', 'codewars'))
    print(mix('A generation must confront the looming ', 'codewarrs'))
    print(mix('Xgzcg@fqtmBgbuw1alkj:qdrqVmctl',
              'DkjqkUtjbs&stzzFfnii6nwsa-enuv'))
    print(mix('XarlrNylasHapfkPsfqu:nqso5klmf',
              'Qbfvk8dviiBumsi$cxwb.nxslAuvea'))
    print(mix('Vheyf:nshyUvrpyWblrkHvltn-zqcy',
              'QlbicFtsqx8rbkh;vsom*vrlx7jssm'))
    print(mix('HsdrrIlanl)gunwIeasqYhkdo5rbbt',
              'Oedtm-hoog9quvk.moia9hvya;quen'))
