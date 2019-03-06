# Use from shell with python main.py <int>

import sys

from fibonacci import fibonacci

var1 = sys.argv[1]

if var1.isdigit():
    print(fibonacci(int(var1)))
else:
    print("Value is not a string")
