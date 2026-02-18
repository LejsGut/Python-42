import sys

def main(argv: list[str]) -> None:
    print("Command Quest")

    ft_command_quest = argv[0]

    if(len(argv) == 1):
        print("No arguments provided!")
        print(f"Program name: ft_command_quest")
        print("Total arguments: 1")
        return

    counter = 1
    for i in argv[1:]:
        print(f"Argument {counter}: {i}")
        counter += 1
    
    print(f"Total amount of arguments is {counter}")

if __name__ == "__main__":
    main(sys.argv)
#python3 ft_command_quest.py "hello send help" "" 
#python3 ft_command_quest.py "hello send help" "  1  2"
#python3 ft_command_quest.py hello send help