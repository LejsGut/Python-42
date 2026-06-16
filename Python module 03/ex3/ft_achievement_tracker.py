import random


ALL_ACHIEVEMENTS = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer", "Strategist",
    "Unstoppable", "Speed Runner", "Survivor", "Treasure Hunter",
    "First Steps", "Sharp Mind", "Hidden Path Finder",
]
ALL_SET = set(ALL_ACHIEVEMENTS)


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.achievements: set[str] = set()


def gen_player_achievements() -> set[str]:
    number = random.randint(len(ALL_ACHIEVEMENTS) // 2, len(ALL_ACHIEVEMENTS))
    return set(random.sample(ALL_ACHIEVEMENTS, number))


def main() -> None:
    print("=== Achievement Tracker System ===")
    players = [Player("Alice"), Player("Bob"),
               Player("Charlie"), Player("Dylan")]
    for player in players:
        player.achievements = gen_player_achievements()
        print(f"Player {player.name}: {player.achievements}")

    distinct: set[str] = set()
    for player in players:
        distinct = distinct.union(player.achievements)
    print(f"All distinct achievements: {distinct}")

    common = set.intersection(*(p.achievements for p in players))
    print(f"Common achievements: {common}")

    for player in players:
        others: set[str] = set()
        for other in players:
            if other is not player:
                others = others.union(other.achievements)
        print(f"Only {player.name} has: "
              f"{player.achievements.difference(others)}")

    for player in players:
        print(f"{player.name} is missing: "
              f"{ALL_SET.difference(player.achievements)}")


if __name__ == "__main__":
    main()
