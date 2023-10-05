from enum import Enum
import uuid


class ResultType(Enum):
    ADVISORY = "Advisory"
    FAILURE = "Failure"
    SUFFICIENT = "Sufficient"


class Met(Enum):
    NO = "No"
    UNKNOWN = "Unknown"
    YES = "Yes"


class TechniqueResult:
    def __init__(self, code, description, element, is_met, type):
        self.id_ = str(uuid.uuid4())
        self.code = code
        self.description = description
        self.element = element
        self.is_met = is_met
        self.type = type

    def as_dict(self):
        return {
            "id": self.id_,
            "type": self.type.value,
            "is_met": self.is_met.value,
            "code": self.code,
            "description": self.description,
            "element": self.element._impl_obj._selector,
        }


class Ask(TechniqueResult):
    YESNO = [(True, "Yes"), (False, "No")]

    def __init__(self, code, question, element, type, question_id, choices):
        super().__init__(code, question, element, Met.UNKNOWN, type)
        self.question_id = question_id
        self.choices = choices

    def as_dict(self):
        d = super().as_dict()
        d["question_id"] = self.question_id
        d["choices"] = self.choices
        return d


class CriteriaResult:
    def __init__(self, code, description, is_met):
        self.id_ = str(uuid.uuid4())
        self.code = code
        self.description = description
        self.is_met = is_met

    def as_dict(self):
        return {
            "id": self.id_,
            "is_met": self.is_met.value,
            "code": self.code,
            "description": self.description,
        }
