class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("rose", "15cm", "2 months")
    print("=== Welcome to My Garden ===")
    print(f"Plant: {rose.name}")
    print(f"Height: {rose.height}")
    print(f"Age: {rose.age}")
    print("=== End of Program ===")
