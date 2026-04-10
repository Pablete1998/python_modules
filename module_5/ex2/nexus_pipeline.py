#!/usr/bin/env python3

from __future__ import annotations

from typing import List, Tuple, Protocol
from data_processor import (
    NumericProcessor,
    TextProcessor,
    LogProcessor,
)
from data_stream import DataStream


# ---------------------------------------------------------
# Export Plugin Protocol
# ---------------------------------------------------------

class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        """
        Receives a list of (rank, string) tuples.
        """
        ...


# ---------------------------------------------------------
# CSV Export Plugin
# ---------------------------------------------------------

class CSVExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        # Convert only the string values into CSV
        values = [item[1] for item in data]
        csv_line = ",".join(values)
        print("CSV Output:")
        print(csv_line)


# ---------------------------------------------------------
# JSON Export Plugin
# ---------------------------------------------------------

class JSONExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        # Convert to {"item_rank": "value", ...}
        json_items = []
        for rank, value in data:
            json_items.append(f'"item_{rank}": "{value}"')

        json_str = "{ " + ", ".join(json_items) + " }"
        print("JSON Output:")
        print(json_str)


# ---------------------------------------------------------
# Extend DataStream with output_pipeline
# ---------------------------------------------------------

class PipelineDataStream(DataStream):
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """
        Consume nb elements from each processor and export them.
        """
        for proc in self._processors:
            collected: List[Tuple[int, str]] = []

            for _ in range(nb):
                try:
                    rank, value = proc.output()
                    collected.append((rank, value))
                    self._stats_remaining[proc] -= 1
                except IndexError:
                    break

            if collected:
                plugin.process_output(collected)


# ---------------------------------------------------------
# Test scenario (as required by the PDF)
# ---------------------------------------------------------

def ft_main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    ds = PipelineDataStream()
    ds.print_processors_stats()

    print("Registering Processors")
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    ds.register_processor(num)
    ds.register_processor(text)
    ds.register_processor(log)

    batch1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("Send first batch of data on stream:", batch1)
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print("Send another batch of data:", batch2)
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()


if __name__ == "__main__":
    ft_main()
