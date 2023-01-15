# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any

Input = TypeVar("Input")
Output = TypeVar("Output")


class UseCase(Generic[Input, Output], ABC):
    @abstractmethod
    def execute(self, input_use_case: Input, db: Any) -> Output:
        raise NotImplementedError()
