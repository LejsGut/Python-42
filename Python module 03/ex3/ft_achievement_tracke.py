import random

ALL_ACHIEVEMENTS = {
    'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme',
    'Untouchable', 'Boss Slayer', 'Strategist', 'Unstoppable', 'Speed Runner',
    'Survivor', 'Treasure Hunter', 'First Steps', 'Sharp Mind', 'Hidden Path Finder'
}


class Player:
    def __init__(self, name):
        self.name = name
        self.achievements = set()


class Alice(Player):
    pass


class Bob(Player):
    pass


class Charlie(Player):
    pass


class Dylan(Player):
    pass


def gen_player_achievements():
    number = random.randint(1, len(ALL_ACHIEVEMENTS))
    return set(random.sample(list(ALL_ACHIEVEMENTS), number))


def achievements_stats(players, distinct):
    common = set.intersection(*(p.achievements for p in players))
    print(f"Common achievements: {common}")
    for player in players:
        others = [p.achievements for p in players if p != player]
        others_union = others[0].union(others[1]).union(others[2])
        print(f"Only {player.name} has: {player.achievements.difference(others_union)}")
    for player in players:
        print(f"{player.name} is missing: {ALL_ACHIEVEMENTS.difference(player.achievements)}")


def main():
    print("=== Achievement Tracker System ===")
    players = [Alice("Alice"), Bob("Bob"), Charlie("Charlie"), Dylan("Dylan")]
    for player in players:
        player.achievements = gen_player_achievements()
        print(f"Player {player.name}: {player.achievements}")
    distinct = players[0].achievements.union(
        players[1].achievements).union(
        players[2].achievements).union(
        players[3].achievements)
    print(f"All distinct achievements: {distinct}")
    achievements_stats(players, distinct)


if __name__ == "__main__":
    main()