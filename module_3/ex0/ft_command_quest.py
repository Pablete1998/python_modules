#!/usr/bin/env python3


import sys


def command_quest():
    print(f"Program name: {sys.argv[0]}")
    args = sys.argv
    i = 1
    count = len(args[1:])
    if count > 0:
        print(f"Arguments recieved: {count}")
        args_1 = sys.argv[1:]
        for argum in args_1:
            print(f"Argument {i}: {argum}")
            i += 1
    else:
        print("No arguments provided!")

    print(f"Total arguments: {i}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    command_quest()
    print("")
