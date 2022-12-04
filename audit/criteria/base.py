class Criteria:
    SUFFICIENT = None
    ADVISORY = None
    FAILURE = None

    def test(self, element):
        yield from self.test_failure(element)
        yield from self.test_sufficient(element)
        yield from self.test_advisory(element)

    def find_elements(self, page):
        raise NotImplementedError()

    def test_failure(self, element):
        if self.FAILURE is not None:
            yield self.FAILURE.resolve(element)

    def test_sufficient(self, element):
        if self.SUFFICIENT is not None:
            yield self.SUFFICIENT.resolve(element)

    def test_advisory(self, element):
        if self.ADVISORY is not None:
            yield self.ADVISORY.resolve(element)
