Suppose we need to extract `row` and `col` from a string:

```python
import re
some_string = 'R1C2_row62_col24.png'
m = re.match(r".*row(\d+)_col(\d+).*.png", some_string)
row = int(m.group(1))
col = int(m.group(2))
assert row == 62
assert col == 24
```

Test here [https://regex101.com/](https://regex101.com/)

| Character | Action |
| - | - |
|  `.` | any character |
| `\d` | only numbers (if we need decimal point user a backslash (\.) |
| `?`  | Zero or one character | 
| `+`  | One or many |
| `*`  | Any character count |

Good [tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285).