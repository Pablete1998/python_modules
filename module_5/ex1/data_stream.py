#!/usr/bin/env python3
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List


class DataStream(ABC):
    """
    Base class for all streams.
    """

    stream_id: str
    processed_count: int

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def describe_batch(self, batch: List[Any]) -> str:
        raise NotImplementedError

    @abstractmethod
    def summarize_batch(self, batch: List[Any]) -> str:
        raise NotImplementedError

    @abstractmethod
    def filter_priority(self, batch: List[Any]) -> List[Any]:
        raise NotImplementedError


class SensorStream(DataStream):
    def get_type(self) -> str:
        return "Environmental Data"

    def describe_batch(self, batch: List[Any]) -> str:
        return f"Processing sensor batch: {batch}"

    def summarize_batch(self, batch: List[Any]) -> str:
        return f"- Sensor data: {len(batch)} readings processed"

    def filter_priority(self, batch: List[Any]) -> List[Any]:
        critical: List[Any] = []
        for d in batch:
            if isinstance(d, (int, float)) and (d > 100 or d < 0):
                critical.append(d)
            elif isinstance(d, str) and ":" in d:
                _, val = d.split(":", 1)
                try:
                    num = float(val)
                    if num > 100 or num < 0:
                        critical.append(d)
                except ValueError:
                    pass
        return critical

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)

        temps: List[float] = []
        for d in data_batch:
            if isinstance(d, (int, float)):
                temps.append(float(d))
            elif isinstance(d, str) and ":" in d:
                _, val = d.split(":", 1)
                try:
                    temps.append(float(val))
                except ValueError:
                    pass

        avg_temp = sum(temps) / len(temps) if temps else 0.0

        return (
            f"Sensor analysis: {len(data_batch)} readings processed, "
            f"avg temp: {avg_temp:.1f}°C"
        )


class TransactionStream(DataStream):
    def get_type(self) -> str:
        return "Financial Data"

    def describe_batch(self, batch: List[Any]) -> str:
        return f"Processing transaction batch: {batch}"

    def summarize_batch(self, batch: List[Any]) -> str:
        return f"- Transaction data: {len(batch)} operations processed"

    def filter_priority(self, batch: List[Any]) -> List[Any]:
        large: List[Any] = []
        for item in batch:
            if isinstance(item, str) and ":" in item:
                _, val = item.split(":", 1)
                try:
                    if int(val) > 100:
                        large.append(item)
                except ValueError:
                    pass
        return large

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)

        net_flow = 0
        for item in data_batch:
            if isinstance(item, str) and ":" in item:
                op, val = item.split(":", 1)
                try:
                    num = int(val)
                    if op == "buy":
                        net_flow += num
                    elif op == "sell":
                        net_flow -= num
                except ValueError:
                    pass

        sign = "+" if net_flow >= 0 else ""
        return (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: {sign}{net_flow} units\n"
        )


class EventStream(DataStream):
    def get_type(self) -> str:
        return "System Events"

    def describe_batch(self, batch: List[Any]) -> str:
        return f"Processing event batch: {batch}"

    def summarize_batch(self, batch: List[Any]) -> str:
        return f"- Event data: {len(batch)} events processed"

    def filter_priority(self, batch: List[Any]) -> List[Any]:
        return []

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)

        errors = sum(
            1 for d in data_batch
            if isinstance(d, str) and "error" in d.lower()
        )

        return (
            f"Event analysis: {len(data_batch)} events, "
            f"{errors} error detected"
        )


class StreamProcessor:
    streams: List[DataStream]

    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def run_batch(self, data_batches: List[List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")

        print("\nBatch 1 Results:")
        for stream, batch in zip(self.streams, data_batches):
            print(stream.summarize_batch(batch))

        print("\nStream filtering active: High-priority data only")

        sensor_crit = len(self.streams[0].filter_priority(data_batches[0]))
        trans_crit = len(self.streams[1].filter_priority(data_batches[1]))

        print(
            f"Filtered results: {sensor_crit} critical sensor alerts, "
            f"{trans_crit} large transaction\n"
        )


def ft_main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.get_type()}")
    batch1 = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(sensor.describe_batch(batch1))
    print(sensor.process_batch(batch1))

    print("\nInitializing Transaction Stream...")
    print(
        f"Stream ID: {transaction.stream_id}, "
        f"Type: {transaction.get_type()}"
        )
    batch2 = ["buy:100", "sell:150", "buy:75"]
    print(transaction.describe_batch(batch2))
    print(transaction.process_batch(batch2))

    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.get_type()}")
    batch3 = ["login", "error", "logout"]
    print(event.describe_batch(batch3))
    print(event.process_batch(batch3))

    print("")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    processor.run_batch([
        [22.5, 101.2],
        ["buy:50", "sell:25", "buy:200", "sell:10"],
        ["login", "logout", "error"],
    ])

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    ft_main()
