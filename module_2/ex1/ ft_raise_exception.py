#!/usr/bin/env python3

def input_temperature(temp_str) -> int:
    temp = int(temp_str)

    if temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
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

    big = "100"
    print(f"Input data is '{big}'")

    try:
        temp = input_temperature(big)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    small = "-50"
    print(f"Input data is '{small}'")

    try:
        temp = input_temperature(small)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
