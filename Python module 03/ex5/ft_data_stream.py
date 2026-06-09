import typing
from typing import Generator
import random


def gen_event() -> Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["move", "run", "climb", "swim", "grab"]
    while True:
        yield (random.choice(players), random.choice(actions))

def consume_event(events: list) -> Generator[tuple, None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)


def main():
    print("=== Game Data Stream Processor")
    liist = []
    g = gen_event()
    for _ in range(1000):
        event = next(g)
        print(f"Event {_ + 1}: Player {event[0]} did action {event[1]}")
    for _ in range(10):
        event = next(g)
        liist.append(event)
    print(f"Last 10 events: {liist}")
    for event in consume_event(liist):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {liist}")

    


if __name__ == "__main__":
    main()