#!/usr/bin/env python3
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    Base abstract processor defining the common interface.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        raise NotImplementedError

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError

    def format_output(self, result: str) -> str:
        """
        Default formatting. Subclasses may override.
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        )

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        total = sum(data)
        avg = total / len(data) if data else 0.0
        return (
            f"Processed {len(data)} numeric values,"
            f" sum={total}, avg={avg:.1f}"
            )

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")

        chars = len(data)
        words = len(data.split())
        return f"Processed text: {chars} characters, {words} words"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log entry")

        level, msg = data.split(":", 1)
        level = level.strip().upper()
        msg = msg.strip()

        if level == "ERROR":
            return f"[ALERT] ERROR level detected: {msg}"
        if level == "INFO":
            return f"[INFO] INFO level detected: {msg}"

        return f"[LOG] {level}: {msg}"

    def format_output(self, result: str) -> str:
        return result


def ft_main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # Numeric Processor
    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    data1 = [1, 2, 3, 4, 5]
    print(f"Processing data: {data1}")
    print("Validation: Numeric data verified")
    print(num_proc.format_output(num_proc.process(data1)), end="\n\n")

    # Text Processor
    print("Initializing Text Processor...")
    text_proc = TextProcessor()
    data2 = "Hello Nexus World"
    print(f'Processing data: "{data2}"')
    print("Validation: Text data verified")
    print(text_proc.format_output(text_proc.process(data2)), end="\n\n")

    # Log Processor
    print("Initializing Log Processor...")
    log_proc = LogProcessor()
    data3 = "ERROR: Connection timeout"
    print(f'Processing data: "{data3}"')
    print("Validation: Log entry verified")
    print(log_proc.format_output(log_proc.process(data3)))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    # Polymorphic demo
    try:
        r1 = num_proc.process([1, 2, 3])
        print(f"Result 1: {r1}")
    except Exception as e:
        print(f"Error: {e}")

    try:
        r2 = text_proc.process("Hello World!!")
        print(f"Result 2: {r2}")
    except Exception as e:
        print(f"Error: {e}")

    try:
        r3 = log_proc.process("INFO: System ready")
        print(f"Result 3: {r3}")
    except Exception as e:
        print(f"Error: {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    ft_main()
