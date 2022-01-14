from functools import lru_cache
import sys
num = int(sys.stdin.readline())
@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(num))

