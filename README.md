# takuzu
A binary puzzle (takuzu) solver written in python.

```shell
$ git clone https://github.com/lesander/takuzu.git && cd takuzu
$ pip3 install -r requirements.txt
```

```python
from takuzu import Takuzu
board = [[None, 1, None, 0],
      	[None, None, 0, None],
      	[None, 0, None, None],
      	[1, 1, None, 0]]
takuzu = Takuzu(board=board, debug=False, silent=False)
result = takuzu.solve()
print(result)
```

```python
takuzu.check(solution, result)
```
