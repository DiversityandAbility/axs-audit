from dataclasses import dataclass
from typing import List
from audit.ask import ask

from audit.results import AXSResult


@dataclass
class TechniqueResult:
    is_failure: bool
    results: List[AXSResult]


class Resolveable:
    def __or__(self, other):
        return OrResolveable(self, other)

    def __and__(self, other):
        return AndResolveable(self, other)

    def resolve(self, element) -> TechniqueResult:
        raise NotImplementedError()


class AndResolveable(Resolveable):
    def __init__(self, lhs: Resolveable, rhs: Resolveable):
        self.lhs = lhs
        self.rhs = rhs

    def resolve(self, element) -> TechniqueResult:
        l_result = self.lhs.resolve(element)
        if l_result.is_failure:
            return l_result

        r_result = self.rhs.resolve(element)
        if r_result.is_failure:
            return r_result

        return TechniqueResult(
            is_failure=False,
            results=l_result.results + r_result.results,
        )


class OrResolveable(Resolveable):
    def __init__(self, lhs: Resolveable, rhs: Resolveable):
        self.lhs = lhs
        self.rhs = rhs

    def resolve(self, element) -> TechniqueResult:
        l_result = self.lhs.resolve(element)
        if not l_result.is_failure:
            return l_result

        r_result = self.rhs.resolve(element)
        if not r_result.is_failure:
            return r_result

        return TechniqueResult(
            is_failure=True,
            results=l_result.results + r_result.results,
        )


class Technique(Resolveable):
    def resolve(self, element) -> TechniqueResult:
        is_failure = False
        results = []
        for r in self.test(element):
            results.append(r)
            is_failure = is_failure or r.IS_FAILURE
        return TechniqueResult(is_failure, results=results)

    def test(self, element):
        raise NotImplementedError()
