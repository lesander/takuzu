from takuzu import Takuzu
b = [ [None, 1, None, 0],
      [None, None, 0, None],
      [None, 0, None, None],
      [1, 1, None, 0]
    ]
s = [ [0, 1, 1, 0],
      [1, 0, 0, 1],
      [0, 0, 1, 1],
      [1, 1, 0, 0]
    ]
t = Takuzu(board=b, debug=False, silent=True)
r = t.solve()
t.check(s, r)
