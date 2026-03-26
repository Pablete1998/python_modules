#!/usr/bin/env python3

import sys

class InvalidError():
        def __init__(self, message="invalid parameter: "):
            print(f"{message}")


def checker_chachi(argumen):
    print("patata")


def score_analytics():
    arg = sys.argv[1:]
    count = len(arg) - 1
    if count == 0:
        print(f"No scores provided. Usage: python{sys.version_info.major}", end=" ")
        for e in arg:
            print(f"{e}", end=" ")
        print("<score1> <score2> ...")
        return
    else:
        for e in arg:
            checker_chachi(e)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analytics()
    print("")