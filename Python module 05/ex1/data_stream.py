from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.rank: int = 0
        self.total: int = 0
        self.name: str = ""

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
        self.name = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        ) or isinstance(data, (int, float)):
            return True
        return False

    def ingest(self, data: int | float | list) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(str(item))
                self.total += 1
        elif isinstance(data, (int, float)):
            self.storage.append(str(data))
            self.total += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list) and all(
            isinstance(x, str) for x in data
        ) or isinstance(data, str):
            return True
        return False

    def ingest(self, data: str | list) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(item)
                self.total += 1
        elif isinstance(data, str):
            self.storage.append(data)
            self.total += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Log Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and all(
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
            self.total += 1
        elif isinstance(data, list):
            for item in data:
                self.storage.append(
                    f"{item['log_level']}: {item['log_message']}"
                )
                self.total += 1


class DataStream:
    def __init__(self) -> None:
        self.processor_list: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processor_list.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for proc in self.processor_list:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print(
                    f"DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processor_list:
            print("No processor found, no data")
            return
        for proc in self.processor_list:
            print(
                f"{proc.name}: total {proc.total} items processed, "
                f"remaining {len(proc.storage)} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Numeric Processor")
    ds.register_processor(NumericProcessor())

    batch: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"\nSend first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())
    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        ds.processor_list[0].output()
    for _ in range(2):
        ds.processor_list[1].output()
    ds.processor_list[2].output()
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
