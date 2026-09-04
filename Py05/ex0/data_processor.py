#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Tuple, Union, List, Dict


class DataProcessor(ABC):
    """Abstract base class for data processing architecture."""

    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check if the input data is appropriate for the current processor."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process and ingest the input data."""
        pass

    def output(self) -> Tuple[int, str]:
        """Output the currently ingested data."""
        if not self._storage:
            raise IndexError("No data available to output.")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    """Processor specialized in handling numeric data."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                isinstance(x, (int, float))
                and not isinstance(x, bool) for x in data
            )
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError(
                "Invalid data:  Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._rank += 1
            self._storage.append((self._rank, str(item)))


class TextProcessor(DataProcessor):
    """Processor specialized in handling text data."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data: TextProcessor expects a string.")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._rank += 1
            self._storage.append((self._rank, item))


class LogProcessor(DataProcessor):
    """Processor specialized in handling log data."""

    def validate(self, data: Any) -> bool:
        def is_valid_dict(d: Any) -> bool:
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            )

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(d) for d in data)
        return False

    def ingest(
        self, data: Union[Dict[str, str], List[Dict[str, str]]]
    ) -> None:
        if not self.validate(data):
            raise ValueError(
                "Invalid data: LogProcessor expects "
                "dict[str, str] or lists of them."
            )

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._rank += 1
            if (
                isinstance(item, dict)
                and "log_level" in item
                and "log_message" in item
            ):
                formatted_str = f"{item['log_level']}: {item['log_message']}"
            else:
                formatted_str = str(item)
            self._storage.append((self._rank, formatted_str))


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    # Testing Numeric Processor
    print("Testing Numeric Processor...")
    num_processor = NumericProcessor()
    print(f"Test to validate input 42: {num_processor.validate(42)}")
    print(f"Test to validate input 'Hello': {num_processor.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_processor.ingest("foo")  # type: ignore
    except ValueError as e:
        print(f"Got exception: {e}")

    num_data: List[Union[int, float]] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_processor.ingest(num_data)

    print("Extracting 3 values...")
    for i in range(3):
        rank, val = num_processor.output()
        print(f"Numeric value {i}: {val}")

    # Testing Text Processor
    print("\nTesting Text Processor...")
    text_processor = TextProcessor()
    print(f"Trying to validate input 42: {text_processor.validate(42)}")

    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text_processor.ingest(text_data)

    print("Extracting 1 value...")
    for i in range(1):
        rank, val = text_processor.output()
        print(f"Text value {i}: {val}")

    # Testing Log Processor
    print("\nTesting Log Processor...")
    log_processor = LogProcessor()
    print(f"Test to validate input 'Hello': {log_processor.validate('Hello')}")

    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ]
    print(f"Processing data: {log_data}")
    log_processor.ingest(log_data)

    print("Extracting 2 values...")
    for i in range(2):
        rank, val = log_processor.output()
        print(f"Log entry {i}: {val}")
