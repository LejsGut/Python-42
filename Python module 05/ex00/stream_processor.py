
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            for num in data:
                if not isinstance(num, (int, float)):
                    raise ValueError(f"Invalid data: {num} is not a number")
                return False
        except TypeError:
            raise ValueError("Invalid data: expected a number or a list of numbers")
        return True

    def process(self, data: Any) -> str:
        print("Initialize Numeric Processor....")
        print(f"Processing data: {data}")