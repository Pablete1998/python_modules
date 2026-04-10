#!/usr/bin/env python3

from __future__ import annotations

from typing import Any, List, Dict
from data_processor import (
    DataProcessor,
    NumericProcessor,
    TextProcessor,
    LogProcessor,
)


class DataStream:
    """
    Routes heterogeneous data to the correct processor using polymorphism.
    """

    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []
        self._stats_total: Dict[DataProcessor, int] = {}
        self._stats_remaining: Dict[DataProcessor, int] = {}

    # ---------------------------------------------------------
    # Register a processor
    # ---------------------------------------------------------
    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        self._stats_total[proc] = 0
        self._stats_remaining[proc] = 0

    # ---------------------------------------------------------
    # Process a heterogeneous stream
    # ---------------------------------------------------------
    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            handled = False

            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)

                    count = len(element) if isinstance(element, list) else 1
                    self._stats_total[proc] += count
                    self._stats_remaining[proc] += count

                    handled = True
                    break

            if not handled:
                print(
                    "DataStream error - Can't process element in stream:",
                    element,
                )

    # ---------------------------------------------------------
    # Print statistics
    # ---------------------------------------------------------
    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            name = proc.__class__.__name__
            total = self._stats_total[proc]
            remaining = self._stats_remaining[proc]
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


# ---------------------------------------------------------
# Test scenario (as required by the PDF)
# ---------------------------------------------------------

def ft_main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")

    ds = DataStream()
    ds.print_processors_stats()

    # Register Numeric Processor
    print("Registering Numeric Processor")
    num = NumericProcessor()
    ds.register_processor(num)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
             },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("Send first batch of data on stream:", batch)
    ds.process_stream(batch)
    ds.print_processors_stats()

    # Register other processors
    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    ds.register_processor(text)
    ds.register_processor(log)

    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    # Consume outputs
    for _ in range(3):
        try:
            num.output()
            ds._stats_remaining[num] -= 1
        except IndexError:
            break

    for _ in range(2):
        try:
            text.output()
            ds._stats_remaining[text] -= 1
        except IndexError:
            break

    try:
        log.output()
        ds._stats_remaining[log] -= 1
    except IndexError:
        pass

    ds.print_processors_stats()


if __name__ == "__main__":
    ft_main()
