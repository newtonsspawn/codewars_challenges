def snail(array):
    
    if array == [[]]:
        return []
    
    snail_array = []
    
    def outward_crawl(x_start, x_end, y_start, y_end):
        if x_start == x_end and y_start == y_end:
            return
        for x_i in range(x_start, x_end):
            snail_array.append(array[y_start][x_i])
        y_start += 1
        if x_start == x_end and y_start == y_end:
            return
        for y_i in range(y_start, y_end):
            snail_array.append(array[y_i][x_end-1])
        x_end -= 1
        if x_start == x_end and y_start == y_end:
            return
        for x_i in range(x_end-1, x_start-1, -1):
            snail_array.append(array[y_end-1][x_i])
        y_end -= 1
        if x_start == x_end and y_start == y_end:
            return
        for y_i in range(y_end-1, y_start-1, -1):
            snail_array.append(array[y_i][x_start])
        x_start += 1
        outward_crawl(x_start, x_end, y_start, y_end)
    
    outward_crawl(0, len(array), 0, len(array))
    
    return snail_array


if __name__ == '__main__':
    print(snail([[]]))
    print(snail([[1]]))
    print(snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(snail([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))
    print(snail([[1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7],
                 [19, 32, 33, 34, 25, 8],
                 [18, 31, 36, 35, 26, 9],
                 [17, 30, 29, 28, 27, 10],
                 [16, 15, 14, 13, 12, 11]]))
    print(snail([[350]]))
    print(snail([[545, 588, 42, 119, 791, 866, 142, 699, 611,
                  400, 465, 373, 30, 71, 950, 813, 850, 652],
                 [664, 853, 1000, 561, 102, 363, 807, 553, 973,
                  643, 142, 433, 378, 702, 250, 641, 967, 172],
                 [908, 928, 776, 82, 547, 224, 730, 158, 169, 8,
                  111, 847, 891, 142, 906, 609, 443, 211],
                 [417, 35, 192, 167, 579, 885, 160, 755, 522,
                  360, 382, 783, 986, 474, 761, 416, 564, 561],
                 [506, 160, 540, 575, 374, 854, 313, 656, 546,
                  924, 838, 831, 23, 146, 116, 136, 47, 889],
                 [932, 515, 627, 982, 886, 609, 67, 966, 262,
                  953, 299, 246, 488, 526, 524, 855, 954, 752],
                 [182, 310, 522, 423, 907, 743, 440, 827, 548,
                  162, 397, 494, 592, 629, 856, 288, 601, 188],
                 [963, 862, 9, 812, 947, 721, 37, 170, 69, 326,
                  661, 829, 69, 341, 100, 751, 951, 844],
                 [252, 831, 293, 346, 830, 639, 657, 425, 294,
                  47, 477, 786, 852, 821, 858, 438, 251, 296],
                 [136, 891, 795, 298, 144, 686, 845, 781, 737,
                  850, 413, 88, 333, 311, 628, 962, 785, 548],
                 [307, 294, 706, 298, 825, 108, 508, 358, 978,
                  707, 26, 774, 332, 252, 407, 466, 77, 141],
                 [803, 134, 246, 768, 431, 724, 448, 362, 875,
                  983, 188, 254, 332, 249, 162, 167, 911, 639],
                 [266, 399, 765, 878, 433, 414, 178, 225, 507,
                  112, 510, 124, 88, 969, 728, 18, 813, 763],
                 [714, 580, 290, 935, 331, 813, 781, 114, 183,
                  437, 287, 870, 719, 690, 880, 319, 939, 715],
                 [283, 165, 518, 34, 109, 638, 327, 3, 369, 979,
                  696, 845, 34, 498, 736, 372, 166, 931],
                 [728, 490, 910, 342, 460, 955, 876, 935, 976,
                  887, 190, 517, 362, 15, 486, 138, 681, 996],
                 [585, 139, 62, 485, 628, 667, 213, 29, 910, 333,
                  854, 201, 613, 27, 552, 244, 251, 177],
                 [222, 791, 454, 246, 525, 626, 58, 512, 642,
                  561, 309, 674, 607, 441, 728, 782, 375, 113]]))
    print(snail([[844, 865, 787, 987, 255, 928, 812],
                 [533, 376, 869, 60, 824, 527, 355],
                 [238, 330, 215, 201, 335, 29, 225],
                 [828, 63, 172, 620, 315, 361, 758],
                 [14, 964, 210, 530, 997, 568, 288],
                 [855, 152, 486, 856, 360, 545, 564],
                 [549, 259, 544, 508, 793, 934, 567]]))
    print(snail([[277, 149, 76, 473, 385, 633, 41, 517, 918, 462,
                  769, 726, 161, 694, 26, 717, 309, 484],
                 [822, 156, 851, 683, 303, 638, 818, 714, 303,
                  509, 353, 557, 51, 592, 663, 475, 725, 40],
                 [40, 155, 345, 977, 600, 812, 851, 559, 152,
                  256, 965, 586, 591, 966, 146, 868, 262, 931],
                 [855, 170, 534, 89, 73, 910, 741, 195, 4, 547,
                  916, 887, 912, 610, 815, 619, 508, 196],
                 [600, 735, 378, 713, 511, 639, 703, 269, 326,
                  650, 223, 993, 760, 894, 430, 705, 896, 814],
                 [444, 223, 939, 289, 624, 837, 541, 975, 608,
                  446, 787, 963, 647, 660, 827, 544, 894, 634],
                 [643, 836, 653, 921, 77, 574, 411, 242, 52, 242,
                  411, 827, 875, 617, 653, 180, 85, 390],
                 [592, 287, 28, 699, 663, 170, 548, 812, 792, 68,
                  376, 733, 147, 475, 803, 513, 815, 515],
                 [366, 76, 557, 607, 661, 516, 434, 136, 41, 551,
                  670, 662, 248, 205, 485, 509, 59, 833],
                 [394, 608, 437, 669, 92, 194, 441, 444, 68, 269,
                  512, 104, 121, 176, 422, 278, 953, 69],
                 [187, 714, 933, 50, 576, 276, 594, 283, 258,
                  268, 95, 111, 353, 139, 342, 274, 141, 69],
                 [588, 50, 105, 400, 470, 733, 51, 342, 193, 6,
                  909, 690, 697, 215, 612, 27, 629, 861],
                 [784, 253, 98, 563, 118, 138, 610, 486, 602,
                  779, 153, 478, 956, 107, 460, 850, 447, 21],
                 [690, 48, 219, 72, 384, 261, 474, 383, 632, 868,
                  922, 826, 651, 612, 684, 339, 418, 743],
                 [955, 462, 403, 996, 131, 70, 485, 523, 407,
                  932, 100, 688, 240, 970, 98, 681, 356, 609],
                 [376, 795, 982, 482, 813, 496, 635, 618, 728,
                  96, 982, 884, 362, 168, 470, 919, 672, 921],
                 [327, 201, 195, 628, 731, 453, 778, 719, 751,
                  115, 429, 675, 983, 281, 389, 396, 876, 484],
                 [867, 449, 958, 381, 640, 749, 216, 358, 226,
                  155, 568, 795, 584, 220, 900, 207, 12, 440]]))
    print(snail([[831, 609, 235, 391, 645, 469, 352, 982, 96,
                  596, 79, 460, 438, 280, 390],
                 [639, 19, 257, 411, 862, 508, 652, 265, 609,
                  188, 443, 425, 584, 11, 329],
                 [616, 731, 442, 315, 530, 954, 306, 455, 808,
                  921, 604, 282, 695, 778, 711],
                 [205, 735, 423, 803, 480, 736, 47, 13, 478, 960,
                  268, 844, 611, 102, 489],
                 [271, 314, 134, 650, 634, 984, 925, 565, 67,
                  651, 139, 697, 735, 616, 83],
                 [124, 381, 202, 355, 488, 99, 269, 486, 900,
                  601, 449, 777, 607, 702, 504],
                 [259, 357, 104, 126, 784, 649, 30, 243, 716,
                  436, 917, 272, 629, 864, 131],
                 [333, 402, 81, 766, 352, 14, 227, 796, 572, 623,
                  176, 196, 870, 5, 822],
                 [469, 67, 286, 430, 711, 336, 78, 384, 71, 783,
                  832, 458, 940, 511, 160],
                 [783, 286, 352, 679, 233, 493, 549, 83, 137,
                  498, 450, 214, 856, 925, 585],
                 [360, 663, 80, 307, 411, 97, 42, 857, 865, 954,
                  30, 778, 691, 880, 898],
                 [354, 373, 818, 619, 465, 957, 268, 876, 19, 58,
                  163, 138, 283, 970, 267],
                 [773, 79, 892, 808, 810, 35, 147, 377, 502, 400,
                  742, 345, 35, 120, 859],
                 [933, 643, 548, 241, 817, 661, 936, 837, 571,
                  596, 177, 296, 531, 836, 805],
                 [915, 268, 534, 369, 791, 90, 843, 104, 293, 92,
                  270, 306, 226, 797, 903]]))
