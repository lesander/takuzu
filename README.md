# takuzu
A basic binary / takuzu puzzle solver written in Python 3.

Implemented [rules](https://en.wikipedia.org/wiki/Takuzu) (2/4):
1. Each row and each column must contain an equal number of 0s and 1s;
2. More than two of the same digits can't be adjacent;
3. ~Eliminate the impossible;~
4. ~Each column and row is unique.~

## Installation
```shell
$ git clone https://github.com/lesander/takuzu.git && cd takuzu
$ pip3 install -r requirements.txt
```

## Usage
```python
from takuzu import Takuzu
board =   [[None, 1,    None, 0],
      	 [None, None, 0,    None],
      	 [None, 0,    None, None],
      	 [1,    1,    None, 0]]
takuzu = Takuzu(board=board, debug=False, silent=False)
result = takuzu.solve()
print(result)

"""
result =
[[0, 1, 1, 0],
 [1, 0, 0, 1],
 [0, 0, 1, 1],
 [1, 1, 0, 0]]
"""
```

You can compare the result with a known solution.
```python
takuzu.check(solution) # returns True or AssertionError
```

## Testing
Some scenarios can be tested.

```shell
$ python3 -m invalid_boards
$ python3 -m tests.4x4
$ python3 -m tests.12x12
```
