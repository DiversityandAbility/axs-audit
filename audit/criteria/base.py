from enum import Enum
import itertools

from audit.results import Met, ResultType


class Criteria:
    level = None
    ref = None
    name = None
    summary = None

    def test(self, page, context):
        raise NotImplementedError()

    def is_met(self, all_results):
        for r in all_results:
            if r.is_met == Met.UNKNOWN:
                return Met.UNKNOWN
            if r.type == ResultType.FAILURE and r.is_met == Met.YES:
                return Met.NO
            if r.type == ResultType.SUFFICIENT and r.is_met == Met.NO:
                return Met.NO
        return Met.YES


class Level(Enum):
    A = "A"
    AA = "AA"
    AAA = "AAA"
