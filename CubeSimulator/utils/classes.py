from enum import Enum, auto

import attr


class Cube(Enum):
    red = 0
    black = 1
    additional = 2


class Rank(Enum):
    rare = 0
    epic = 1
    unique = 2
    legendary = 3


class ItemType(Enum):
    weapon = auto()
    emblem = auto()
    subweapon = auto()
    forcering = auto()
    shield = auto()
    helmet = auto()
    top = auto()
    suit = auto()
    bottom = auto()
    shoes = auto()
    glove = auto()
    cloak = auto()
    belt = auto()
    shoulder = auto()
    face = auto()
    eye = auto()
    earring = auto()
    ring = auto()
    pendant = auto()
    heart = auto()


@attr.s(auto_attribs=True, frozen=True)
class Option(object):
    name: str
    value: str = attr.ib(init=False)
    rank: Rank = attr.ib(init=False)

    def __attrs_post_init__(self):
        # TODO: Validate
        pass

    def __eq__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass
