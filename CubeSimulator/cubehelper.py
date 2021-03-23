from typing import Iterable

import attr

from .item import Item
from .utils.classes import Cube, Option, Rank


@attr.s(auto_attribs=True)
class Target(object):
    cube: Cube
    targetrank: Rank = attr.ib(default=None)
    targetoptions: Iterable[Iterable[Option]] = attr.ib(default=None)

    def __attrs_post_init__(self):
        # TODO: Check validate
        if self.targetrank is None and self.targetoptions is None:
            raise ValueError("Either targetrank or targetoptions must not be None.")

    @classmethod
    def rank(cls, cube: Cube, rank: Rank):
        return cls(cube, rank)

    @classmethod
    def single_options(cls, cube: Cube, rank: Rank, options: Iterable[str]):
        return cls(cube, rank, targetoptions=([Option(x) for x in options],))


def cubeusage(item: Item, *target: Target):
    pass
