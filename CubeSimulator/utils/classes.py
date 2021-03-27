from enum import Enum

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
    weapon = "무기"
    emblem = "엠블렘"
    subweapon = "보조무기"
    forcering = "포스실드, 소울링"
    shield = "방패"
    helmet = "모자"
    top = "상의"
    suit = "한벌옷"
    bottom = "하의"
    shoes = "신발"
    glove = "장갑"
    cloak = "망토"
    belt = "벨트"
    shoulder = "어깨장식"
    face = "얼굴장식"
    eye = "눈장식"
    earring = "귀고리"
    ring = "반지"
    pendant = "펜던트"
    heart = "기계심장"


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
