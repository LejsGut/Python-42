import random

def main():
    print("=== Game Data Alchemist ===")
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")
    big = [name for name in players if name[0].isupper()]
    small = [name for name in players if not name[0].isupper()]
    all_big = [name.capitalize() for name in players]

    score_dict = {name: random.randint(0, 1000) for name in all_big}
    print(f"Players with capital names: {big}")
    print(f"Players with lowercase names: {small}")
    print(f"All players capitalized: {all_big}")
    print(f"Player scores: {score_dict}")
    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average: {average}")
    above_average = {name: score for name, score in score_dict.items() if score > average}
    print(f"Players above average: {above_average}")

if __name__ == "__main__":
    main()