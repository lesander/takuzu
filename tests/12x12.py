from takuzu import Takuzu
b = [
        [None, None, None, 1, None, 1, None, None, None, 1, None, 0],
        [0, None, None, None, None, None, 0, None, None, None, None, 0],
        [None, 1, None, None, None, None, 0, None, 1, None, 1, None],
        [None, None, None, 0, 0, None, None, None, None, None, None, None],
        [None, None, 1, None, None, None, None, 0, None, None, None, None],
        [None, None, None, None, None, None, 1, None, None, None, None, 0],
        [None, None, None, None, 1, None, None, None, None, 1, None, None],
        [None, None, 0, None, None, None, 0, None, None, None, None, 0],
        [None, 1, None, None, None, None, None, None, 1, 1, None, None],
        [0, None, None, None, None, None, None, None, 1, 1, None, None],
        [None, None, None, 1, 1, None, None, None, None, None, None, None],
        [None, None, 0, None, None, None, None, None, 0, None, 0, None]
    ]

s = [
        [1,0,1,1,0,1,1,0,0,1,0,0],
        [0,0,1,1,0,1,0,1,1,0,1,0],
        [0,1,0,0,1,0,0,1,1,0,1,1],
        [1,0,1,0,0,1,1,0,0,1,0,1],
        [1,0,1,1,0,1,0,0,1,0,1,0],
        [0,1,0,1,1,0,1,1,0,0,1,0],
        [0,0,1,0,1,0,1,0,1,1,0,1],
        [1,1,0,1,0,1,0,1,0,0,1,0],
        [0,1,0,0,1,0,1,0,1,1,0,1],
        [0,0,1,0,0,1,1,0,1,1,0,1],
        [1,1,0,1,1,0,0,1,0,0,1,0],
        [1,1,0,0,1,0,0,1,0,1,0,1]
    ]

t = Takuzu(board=b, debug=False, silent=False)
r = t.solve()
t.check(s)
