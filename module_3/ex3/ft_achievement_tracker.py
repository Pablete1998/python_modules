#!/usr/bin/env python3


import random


ACHIEVEMENTS = {
    "Crafting Genius", "World Savior", "Master Explorer", "Collector Supreme",
    "Untouchable", "Boss Slayer", "Strategist", "Unstoppable", "Speed Runner",
    "Survivor", "Treasure Hunter", "First Steps", "Sharp Mind",
    "Hidden Path Finder"
    }


def gen_player_achievements():
    count = random.randint(4, 8)
    return set(random.sample(ACHIEVEMENTS, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print("")
    players = {
        "Alice": gen_player_achievements(),
        "Miky": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan":  gen_player_achievements()
    }
    for player, achievements in players.items():
        print(f"Player {player}: {achievements}")
    print("")
    all_distinct = set.union(*players.values())
    print(f"all distinct achievements: {all_distinct}")
    print("")
    common = set.intersection(*players.values())
    print(f"Common achievements: {common}")
    print("")
    for player, achievements in players.items():
        others = set.union(*(v for k, v in players.items() if k != player))
        unique = achievements.difference(others)
        print(f"Only {player} has: {unique}")
    print("")
    for player, achievements in players.items():
        missing = all_distinct.difference(achievements)
        print(f"{player} is missing: {missing}")
