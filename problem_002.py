"""
Even Fibonacci Numbers.
"""
from functools import lru_cache


@lru_cache(maxsize=None)
def ith_fibonacci(i: int):
    if i < 2:
        return i

    return ith_fibonacci(i - 1) + ith_fibonacci(i - 2)


j, even_sum = 0, 0
while (current_fibonacci := ith_fibonacci(j)) < 4e6:
    even_sum += current_fibonacci if current_fibonacci % 2 == 0 else 0
    j += 1

print(even_sum)
