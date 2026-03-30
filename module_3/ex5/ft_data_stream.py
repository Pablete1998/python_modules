#!/usr/bin/env python3

import random


def gen_event():
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release", "use"]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


# Generator that consumes a list by randomly removing elements
def consume_event(events):
    while len(events) > 0:
        idx = random.randrange(len(events))
        event = events.pop(idx)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    # 1000 events from infinite generator
    stream = gen_event()
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    # Build list of 10 events
    event_list = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    # Consume list with generator
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
