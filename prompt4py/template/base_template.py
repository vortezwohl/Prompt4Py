from abc import abstractmethod
from typing_extensions import Any


class BaseTemplate:
    def __init__(self):
        super().__init__()
        self._context: Any = None
        self._role: Any = None
        self._instruction: Any = None
        self._objective: Any = None
        self._capability: Any = None
        self._constraint: Any = None
        self._output_dtype: Any = None
        self._output_format: Any = None
        self._output_example: Any = None
        self._output_language: Any = None

    @abstractmethod
    def render(self) -> str: ...

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value: Any):
        self._context = value

    @property
    def role(self):
        return self._context

    @role.setter
    def role(self, value: Any):
        self._context = value

    @property
    def instruction(self):
        return self._context

    @instruction.setter
    def instruction(self, value: Any):
        self._context = value

    @property
    def objective(self):
        return self._context

    @objective.setter
    def objective(self, value: Any):
        self._context = value

    @property
    def capability(self):
        return self._context

    @capability.setter
    def capability(self, value: Any):
        self._context = value

    @property
    def constraint(self):
        return self._context

    @constraint.setter
    def constraint(self, value: Any):
        self._context = value

    @property
    def output_dtype(self):
        return self._context

    @output_dtype.setter
    def output_dtype(self, value: Any):
        self._context = value

    @property
    def output_format(self):
        return self._context

    @output_format.setter
    def output_format(self, value: Any):
        self._context = value

    @property
    def output_example(self):
        return self._output_example

    @output_example.setter
    def output_example(self, value: Any):
        self._context = value

    @property
    def output_language(self):
        return self._output_example

    @output_language.setter
    def output_language(self, value: Any):
        self._context = value
