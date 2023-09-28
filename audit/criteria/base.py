from enum import Enum


class Criteria:
    level = None
    ref = None
    name = None
    summary = None

    def test(self, page, context):
        raise NotImplementedError()


class Level(Enum):
    A = "A"
    AA = "AA"
    AAA = "AAA"
