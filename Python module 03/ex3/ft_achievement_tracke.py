import sys

def main():
    print("=== Achievement Tracker System ===")
    print()

    alice = {"first kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first kill", "level_10", "boss_slayer", "colletor"}
    charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}
    
    players = {
        "alice": alice,
        "bob": bob,
        "charlie": charlie
    }

    for name, achievements in players.items():
        print(f"Player {name} achievements: {achievements}")
    print()
    print("=== Achievement Analytics ===")

    all_possible = alice | bob | charlie
    print(f"ALL unique achievements: {all_possible}") 
    print(f"Total unique achievements {len(all_possible)}")

    same = alice.intersection(bob, charlie)
    print()
    print(f"Common to all players: {same}")

    achievement_count = {}

    for achievements in players.values():
        for achievement in achievements:
            if achievement in achievement_count:
                achievement_count[achievement] += 1
            else:
                achievement_count[achievement] = 1
    rare = {a for a, count in achievement_count.items() if count == 1}

    print(f"Rare achievements (1 player): {rare}")
    print()
    a_and_b = alice.intersection(bob)
    print(f"Alice vs Bob common: {a_and_b}")
    a_diff = alice.difference(bob)
    b_diff = bob.difference(alice)
    print(f"Alice unique: {a_diff}")
    print(f"Bob unique: {b_diff}")

if __name__ == "__main__":
    main()