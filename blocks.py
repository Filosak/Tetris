base_blocks = [
    [
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0]
    ],

    [
        [1,0,0],
        [1,1,1],
        [0,0,0]
        
    ],

    [
        [0,0,1],
        [1,1,1],
        [0,0,0]
        
    ],

    [
        [0,1,1],
        [1,1,0],
        [0,0,0]
    ],

    [
        [1,1,0],
        [0,1,1],
        [0,0,0]
    ],


    [
        [0,1,0],
        [1,1,1],
        [0,0,0],
    ],

    [
        [1,1],
        [1,1],
    ],
]


# import random
# base = random.choice(base_blocks)



# for i in range(0, lm // 2):
#     for j in range(i, lm-i-1):
#         base[i][j], base[j][-1-i], base[-1-i][-1-j], base[-1-j][i] = base[-1-j][i], base[i][j], base[j][-1-i], base[-1-i][-1-j]