import math
from functools import lru_cache

CACHE_SIZE = 1024


class Point(object):
    name = "foo"

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    @lru_cache(maxsize=CACHE_SIZE)
    def magic(self) -> str:
        return "magic"

    @staticmethod
    def distance(a: int, b: int) -> float:
        dis = a ** 2 + b ** 2
        return math.sqrt(dis)

    def __str__(self) -> str:
        return f"Point({self.a}, {self.b})"
