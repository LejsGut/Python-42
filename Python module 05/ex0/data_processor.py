from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        value = self.storage.pop(0)
        out_tuple = (self.rank, value)
        self.rank += 1
        return out_tuple


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.storage: list[str] = []

    def validate(self, data: Any) -> bool:
        if (
            isinstance(data, list)
            and all(isinstance(x, (int, float)) for x in data)
            or isinstance(data, (int, float))
        ):
            return True
        return False

    def ingest(self, data: int | float | list) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(str(item))
        elif isinstance(data, (int, float)):
            self.storage.append(str(data))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.storage: list[str] = []

    def validate(self, data: Any) -> bool:
        if (
            isinstance(data, list)
            and all(isinstance(x, str) for x in data)
            or isinstance(data, str)
        ):
            return True
        return False

    def ingest(self, data: str | list) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(str(item))
        elif isinstance(data, str):
            self.storage.append(str(data))


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.storage: list[str] = []

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items()
                )
                for item in data
            )
        return False

    def ingest(self, data: dict | list) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, dict):
            self.storage.append(f"{data['log_level']}: {data['log_message']}")
        elif isinstance(data, list):
            for item in data:
                self.storage.append(
                    f"{item['log_level']}: {item['log_message']}"
                )


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    num = NumericProcessor()
    print(f" Trying to validate input '42': {num.validate(42)}")
    print(f" Trying to validate input 'Hello': {num.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest("foo")  # type: ignore
    except Exception as e:
        print(f" Got exception: {e}")
    num.ingest([1, 2, 3, 4, 5])
    print(" Processing data: [1, 2, 3, 4, 5]")
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = num.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    txt = TextProcessor()
    print(f" Trying to validate input '42': {txt.validate(42)}")
    txt.ingest(["Hello", "Nexus", "World"])
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    print(" Extracting 1 value...")
    rank, value = txt.output()
    print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    log.ingest(logs)
    print(f" Processing data: {logs}")
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
