import sys


def show_arguments() -> None:
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print("Total arguments: 1")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        index = 1
        for arg in sys.argv[1:]:
            print(f"Argument {index}: {arg}")
            index += 1
        print(f"Total arguments: {len(sys.argv)}")


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    show_arguments()


if __name__ == "__main__":
    main()
