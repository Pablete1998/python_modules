#!/usr/bin/env python3

def input_temperature(temp_str: str | int) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("")

    temp: str | int = "25"
    print(f"input data is '{temp}'")
    temp = input_temperature(temp)
    print(f"temperature is now {temp} ºC")

    invalid = "abc"
    print(f"Input data is '{invalid}'")

    try:
        temp = input_temperature(invalid)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
