"""
Basic Takuzu / Binary / Binairo Puzzle solver written in python
Not optimized; written during a (long) lunch break. 2/4 rules implemented
@version 1.0.0
@author github.com/lesander
@license MIT
"""

__version__ = "1.0.0"

from sys import exit
import numpy as np

class Takuzu:

    def __init__(self, board=[], silent=False, debug=False):
        assert (isinstance(board, list)), 'board must be list'
        assert (isinstance(debug, bool)), 'debug parameter must be boolean'
        self.silent = silent
        self.debug = debug
        self.board = np.array(board)
        self.board_size = self.__calculate_board_size()
        self.max_steps = 65535
        self.last_drawn_board = np.array([])
        self.__validate_board()

    def __print(self, message):
        if self.silent != True:
            print(message)

    def __log(self, message):
        if self.debug:
            print(message)

    def __validate_board(self):
        assert (len(self.board) >= 2), 'board must at least be 2x2'
        assert (len(self.board) % 2 == 0), 'board must have even length'

    def __calculate_board_size(self):
        self.__validate_board()
        l = len(self.board)
        for i in range(0, l):
            assert (len(self.board[i]) == l), 'board must have equal rows and columns'
        self.__log('board_size={}'.format(l))
        return l

    def draw(self, only_print_if_changed=True):
        self.__validate_board()

        if self.silent == True:
            return False

        if only_print_if_changed == True and np.all(self.last_drawn_board == self.board):
            return False
        self.last_drawn_board = np.copy(self.board)

        for row in self.board:
            for value in row:
                if value == None:
                    value = ' '
                print('[{}]'.format(value), end='  ')
            print("\n")
        print('')
        return True

    def __rule_equal_num_of_values(self, list):
        if (list == None).sum() == 0:
            return list

        max_num = int(self.board_size / 2)
        num_ones = (list == 1).sum()
        num_zeros = (list == 0).sum()
        if num_ones == max_num:
            self.__log('sum(1) == max_num: replacing None with 0')
            return [ 0 if value is None else value for value in list ]
        elif num_zeros == max_num:
            self.__log('sum(0) == max_num: replacing None with 1')
            return [ 1 if value is None else value for value in list ]
        return list

    def __rule_max_two_of_same_nums_adjacent(self, list):
        # get neighbours; i{-1,-2} and i{+1,+2} for [2,1,i,1,2]
        # nr1 = right neighbour, 1 offset with i
        # nl2 = left neighbour, 2 offset with i

        for i, value in enumerate(list):

            if value != None:
                continue

            elif i == 0: # i,1,2
                nr1 = list[i+1]
                nr2 = list[i+2]
                if nr1 == nr2 and nr1 != None:
                    list[i] = int(not nr1)

            elif i == 1: # 1,i,1,2
                nl1 = list[i-1]
                nr1 = list[i+1]
                nr2 = list[i+2]

                if nl1 == nr1 and nl1 != None:
                    list[i] = int(not nl1)

                if nr1 == nr2 and nr1 != None:
                    list[i] = int(not nr1)

            elif i == self.board_size - 2: # 2,1,i,1
                nl2 = list[i-2]
                nl1 = list[i-1]
                nr1 = list[i+1]

                if (nr1 == nl1 or nl1 == nl2) and nl1 != None:
                    list[i] = int(not nl1)

            elif i == self.board.size - 1: # 2,1,i
                nl2 = list[i-2]
                nl1 = list[i-1]

                if nl1 == nl2 and nl1 != None:
                    list[i] = int(not nl1)

            elif i >= 2 and i <= self.board_size - 2: # 2,1,i,1,2

                nl1 = list[i-1]
                nl2 = list[i-2]
                nr1 = list[i+1]
                nr2 = list[i+2]

                if (nl1 == nr1 or nl1 == nl2) and nl1 != None:
                    list[i] = int(not nl1)

                if nr1 == nr2 and nr1 != None:
                    list[i] = int(not nr1)

        return list

    # TODO: rule 3: eliminate the impossible
    # 0: 4/6
    # 1: 5/6
    # [ ]  [0]  [1]  [0]  [1]  [ ]  [ ]  [0]  [1]  [1]  [0]  [1]
    #                           ^    ^    ^
    # [0]  [0]  [1]  [0]  [1]  [ ]  [ ]  [0]  [1]  [1]  [0]  [1]
    #  ^

    # TODO: rule 4: each col and row is unique
    # ...

    def solve(self):
        for c in range(1, self.max_steps):

            for i, row in enumerate(self.board):
                self.board[i] = self.__rule_equal_num_of_values(row)
                self.draw()
                self.board[i] = self.__rule_max_two_of_same_nums_adjacent(row)

            for i in range(0, self.board_size):
                col = self.board[:, i]
                self.board[:, i] = self.__rule_equal_num_of_values(col)
                self.draw()
                self.board[:, i] = self.__rule_max_two_of_same_nums_adjacent(col)
                self.draw()

            if (self.board == None).sum() == 0:
                self.__print('solved puzzle in {} steps'.format(c))
                self.__log('steps={}'.format(c))
                self.__log('solved=True')
                return self.board.tolist()

        self.__print('could not solve puzzle in {} steps :('.format(self.max_steps))
        self.__log('steps={}'.format(self.max_steps))
        self.__log('solved=False')
        return self.board.tolist()

    def check(self, a, b):
        a = np.array(a)
        b = np.array(b)
        assert(np.all(a == b)), 'solution does not match result'
        self.__log('correct=True')
