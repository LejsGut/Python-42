import sys

def main(argv: list[int]) -> None:

    ft_score_analytics = argv[0]
    print("=== Player Score Analytics ===")

    if(len(argv) == 1):
        print("No arguments provided!")
        print(f"Program name: ft_score_analytics")
        print("Total arguments: 1")
        return 
    scores = []
    counter = 1
    for i in argv[1: ]:
        try:
            num = int(i)
        except ValueError:
            print(f"Invalid score: {i}")
            print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
            return
        else:
            scores.append(num)
        counter += 1

    res = sum(scores)
    average = res / (counter - 1)

    print(f"Scores processed: {scores}")
    print(f"Total players: {counter - 1}")
    print(f"Total score: {res}")
    print(f"Average score: {average}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range {max(scores) - min(scores)}")

if __name__ == "__main__":
    main(sys.argv)