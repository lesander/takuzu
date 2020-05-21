from takuzu import Takuzu
boards = [ [], [None], [1, 0, None], [ [], [] ], [ [1,0] ], [ [1,0], [1] ] ]

for b in boards:
    try:
        t = Takuzu(board=b, debug=True)
    except AssertionError as e:
        pass
    else:
        raise Exception('board={} should throw AssertionError'.format(b))
