import sys


def argcount() -> list[int] | None:
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return None
    scores = []
    for j in range(1, len(sys.argv)):
        try:
            scores.append(int(sys.argv[j]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[j]}'")
    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return None
    return scores


def stats(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = argcount()
    if scores is not None:
        stats(scores)


if __name__ == "__main__":
    main()