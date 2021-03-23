import itertools
import random
from bisect import bisect
from decimal import Decimal
from typing import List, TypeVar

T = TypeVar("T")


def pick(arr: List[T], key=None) -> T:
    def return_self(i):
        return i

    if key is None:
        key = return_self

    weights = [key(x) for x in arr]
    cumdist = list(itertools.accumulate(weights))
    x = Decimal(random.random()) * cumdist[-1]
    return arr[bisect(cumdist, x)]


def pickfloat(arr: List[T], key=None) -> T:
    def return_self(i):
        return i

    if key is None:
        key = return_self

    weights = [key(x) for x in arr]
    cumdist = list(itertools.accumulate(weights))
    x = random.random() * cumdist[-1]
    return arr[bisect(cumdist, x)]


def pickchoices(arr: List[T], key=None) -> T:
    def return_self(i):
        return i

    if key is None:
        key = return_self

    weights = [key(x) for x in arr]
    return random.choices(arr, weights=weights)[0]
