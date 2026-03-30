#!/usr/bin/env python3

import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print("")
    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")
    print("")
    # 1. New list with all names capitalized
    all_caps = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_caps}")
    print("")
    # 2. New list of names that were already capitalized in the original list
    already_caps = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {already_caps}")
    print("")
    # 3. Dictionary of scores for each capitalized name
    score_dict = {name: random.randint(0, 1000) for name in all_caps}
    print(f"Score dict: {score_dict}")

    # 4. Average score
    avg = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {avg}")

    # 5. Dictionary of high scores (above average)
    high_scores = {name: score for name,
                   score in score_dict.items() if score > avg}
    print(f"High scores: {high_scores}")
