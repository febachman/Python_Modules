#!/usr/bin/env python3

import json
from abc import ABC, abstractmethod
from typing import Any, Tuple, Union, List, Dict, Protocol


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


class ExportPlugin(Protocol):
    """Protocol defining the interface for export plugins."""

    def process_output(self, data: List[Tuple[int, str]]) -> None:
        """Export the processed data items."""
        ...


class CsvExportPlugin:
    """Export plugin for CSV formatting."""

    def process_output(self, data: List[Tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(val for _, val in data))


class JsonExportPlugin:
    """Export plugin for JSON formatting."""

    def process_output(self, data: List[Tuple[int, str]]) -> None:
        print("JSON Output:")
        items_dict = {f"item_{rank - 1}": val for rank, val in data}
        print(json.dumps(items_dict))


class DataStream:
    """Manages adaptive stream processing and routes data to processors."""

    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            processed = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break
            if not processed:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(
                f"{name}: total {proc._rank} items processed,"
                f" remaining {len(proc._storage)} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            processor_data: List[Tuple[int, str]] = []
            for _ in range(nb):
                try:
                    processor_data.append(proc.output())
                except IndexError:
                    break
            plugin.process_output(processor_data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors")
    num_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    stream.register_processor(num_processor)
    stream.register_processor(text_processor)
    stream.register_processor(log_processor)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"\nSend first batch of data on stream: {batch}")
    stream.process_stream(batch)

    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CsvExportPlugin()
    stream.output_pipeline(3, csv_plugin)

    stream.print_processors_stats()

    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)

    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JsonExportPlugin()
    stream.output_pipeline(5, json_plugin)

    stream.print_processors_stats()
