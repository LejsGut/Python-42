
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"[Processed] {result}"

class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("Invalid numeric data: expected a non-empty list of numbers")

        for x in data:
            if isinstance(x, bool) or not isinstance(x, (int, float)):
                raise ValueError(
                    f"Invalid numeric data: {x!r} is not a valid number (int/float)"
                )

        return True


    def process(self, data: Any) -> str:
        print("Initializing Numeric Processor...")
        print(f"Processing data: {data}")

        self.validate(data)

        total = 0.0
        count = len(data)

        for x in data:
            total += float(x)

        avg = total / count

        result = f"Processed {count} numeric values, sum={total}, avg={avg}"

        return self.format_output(result)


class TextProcessor(DataProcessor):
    
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or data.strip() == "":
            raise ValueError("Invalid text data: expected a non-empty string")
        return True

    def process(self, data: Any) -> str:
        print("Initializing Text Processor...")
        print(f"Processing data: {data!r}")

        self.validate(data)

        text = data.strip()
        word_count = len(text.split())
        char_count = len(text)

        result = f"Processed text with {word_count} words and {char_count} characters"

        return self.format_output(result)


class LogProcessor(DataProcessor):
    pass