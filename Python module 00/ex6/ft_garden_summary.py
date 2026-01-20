def garden_summary():
    name = input("Enter garden name: ")
    amount = int(input("Enter number of plants: "))
    print(f"Garden: {name}")
    print(f"Plants: {amount}")
    print("Status: Growing well!")


if __name__ == "__main__":
    garden_summary()
