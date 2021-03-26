from typing import List

import attr

from .utils.classes import Cube, ItemType, Rank, Option


@attr.s(auto_attribs=True)
class Item(object):
    itemtype: ItemType
    rank: Rank = attr.ib(default=Rank.rare)
    options: List[Option] = attr.ib(init=False, factory=list)
    addrank: Rank = attr.ib(default=Rank.rare)
    addoptions: List[Option] = attr.ib(init=False, factory=list)

    types = ItemType

    def __attrs_post_init__(self):
        # TODO: setting options
        raise NotImplementedError

    def runcube(self, cubetype: Cube):
        if self.rank < Rank.legendary:
            # TODO: rank upgrade
            pass
        # TODO: pick options
        raise NotImplementedError
