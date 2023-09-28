from enum import Enum
import uuid


class ResultType(Enum):
    WARNING = "Warning"
    FAILURE = "Failure"
    SKIPPED = "Skipped"
    ADVISORY = "Advisory"
    SUFFICIENT = "Sufficient"
    ASK = "Ask"


class Result:
    TYPE = ResultType.FAILURE
    IS_FAILURE = True

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
            "type": self.TYPE.value,
            "code": self.code,
            "description": self.description,
            "element": self.element._impl_obj._selector,
        }

    @classmethod
    def from_(cls, other):
        return cls(other.code, other.description, other.element)


class Warning(Result):
    TYPE = ResultType.WARNING


class Failure(Result):
    TYPE = ResultType.FAILURE
    IS_FAILURE = True


class Skipped(Result):
    TYPE = ResultType.SKIPPED


class Sufficient(Result):
    TYPE = ResultType.SUFFICIENT


class Advisory(Result):
    TYPE = ResultType.ADVISORY


class Ask(Result):
    TYPE = ResultType.ASK
    YESNO = [(True, "Yes"), (False, "No")]

    def __init__(self, code, question, element, question_id, choices):
        super().__init__(code, question, element)
        self.question_id = question_id
        self.choices = choices

    def as_dict(self):
        d = super().as_dict()
        d["question_id"] = self.question_id
        d["choices"] = self.choices
        return d
