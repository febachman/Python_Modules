#!/usr/bin/env python3

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "use", "release"
    ]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    event_list: list,
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        index = random.randint(0, len(event_list) - 1)
        event = event_list[index]
        event_list[:] = event_list[:index] + event_list[index + 1:]
        yield event


def main():
    print("=== Game Data Stream Processor ===")
    print()
    event_stream = gen_event()
    for i in range(1000):
        event = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    print()
    ten_events = [next(event_stream) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")
    for consumed in consume_event(ten_events):
        print(f"Got event from list: {consumed}")
        print(f"Remains in list: {ten_events}")
        print()


if __name__ == "__main__":
    main()
