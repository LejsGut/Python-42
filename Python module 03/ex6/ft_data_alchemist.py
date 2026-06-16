import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam",
    ]
    print(f"Initial list of players: {players}")

    all_capitalized = [name.capitalize() for name in players]
    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {capitalized_only}")

    scores = {name: random.randint(0, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")
    average = sum(scores[name] for name in scores) / len(scores)
    print(f"Score average is {round(average, 2)}")
    high_scores = {
        name: scores[name] for name in scores if scores[name] > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
