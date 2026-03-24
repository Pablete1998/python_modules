#!/usr/bin/env python3

def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        5 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "hola" + 5
    else:
        return


def test_error_types(operation_number):
    print(f"Testing operation {operation_number}...")

    try:
        garden_operations(operation_number)
        print("Operation completed successfully")
    except ValueError as e:
        print("Caught ValueError:", e)
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
    except TypeError as e:
        print("Caught TypeError:", e)


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")

    operations = [0, 1, 2, 3, 4]

    for op in operations:
        test_error_types(op)
    try:
        garden_operations(0)
    except (ValueError, TypeError) as e:
        print("Caught multiple error types:", e)

    print("All error types tested successfully!")
