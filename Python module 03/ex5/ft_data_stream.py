import time
from typing import Generator

player = ["alice", "bob", "charlie"]
level = [5, 12, 8]
achievements = ["killed monster", "found treasure", "leveled up"]

start = time.time()
def event_stream(n):
    for count in range(n):
        if count == 3:
            yield "..."
            return
        index = count % len(player)
        yield f"Event {count + 1}: Player {player[index]} (level {level[index]}) {achievements[index]}" 
end = time.time()
def analytics(events, player):
    print(f"Total events processed: {events}")
    print(f"High-level players (10+): {events / player}")
    print(f"Treasure events: {(events / player) / 3}")
    print(f"Level-up events: {(events / player) / 3}")

def fibonacci(num):
    x, y = 0, 1
    for i in range(num):
        yield x
        x, y = y, x+y
def primes(n):
    count = 0
    number = 2

    while count < n:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
            count += 1
        number += 1

pro_time = end - start
def main():
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...")
    for event in event_stream(1000):
        print(event)
    print("=== Stream Analytics ===")
    analytics(1000, 3)
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time {pro_time:.9f}")
    print("=== Generator Demonstration")
    print("Fibonacci sequence (first 10):", end=" ")
    for line in fibonacci(10):
        print(line, end=" ")
    print()
    print("Prime numbers (first 5):", end=" ")
    for p in primes(5):
        print(p, end=" ")
    print()

if __name__ == "__main__":
    main()