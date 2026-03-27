#!/usr/bin/env python3


import sys


def score_analytics():
    argums = sys.argv[1:]
    valid_scores = []
    invalid_found = False
    if len(argums) == 0:
        print(
            f"No scores provided. Usage: "
            f"python{sys.version_info.major} "
            f"{sys.argv[0]}", end=" "
            )
        print("<score1> <score2> ...")
        return
    for a in argums:
        try:
            score = (int(a))
            valid_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{a}'")
            invalid_found = True
    if invalid_found and len(valid_scores) == 0:
        print(
            f"No scores provided. Usage: "
            f"python{sys.version_info.major}"
            f"{sys.argv[0]}", end=" "
            )
        print("<score1> <score2> ...")
        return

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {len(valid_scores)}")
    print(f"Total score: {sum(valid_scores)}")
    print(f"Average score: {round(sum(valid_scores) / len(valid_scores), 1)}")
    print(f"High score: {max(valid_scores)}")
    print(f"Low score: {min(valid_scores)}")
    print(f"Score range: {max(valid_scores) - min(valid_scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analytics()
    print("")
