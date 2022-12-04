import uuid


class AXSResult:
    TYPE = "Result"
    IS_FAILURE = False

    def __init__(self, code, description, element):
        self.id_ = str(uuid.uuid4())
        self.code = code
        self.description = description
        self.element = element

    def __str__(self):
        return f"<{self.TYPE} {self.code} {self.element._impl_obj._selector} id={self.id_}>"

    def as_dict(self):
        return {
            "id": self.id_,
            "type": self.TYPE,
            "code": self.code,
            "description": self.description,
            "element": self.element._impl_obj._selector,
        }


class AXSWarning(AXSResult):
    TYPE = "Warning"


class AXSFailure(AXSResult):
    TYPE = "Failure"
    IS_FAILURE = True


class AXSSkipped(AXSResult):
    TYPE = "Skipped"


class AXSSufficient(AXSResult):
    TYPE = "Sufficient"


class AXSAdvisory(AXSResult):
    TYPE = "Advisory"
