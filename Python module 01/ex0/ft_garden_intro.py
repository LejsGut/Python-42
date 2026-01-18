class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        pass

rose = Plant("rose", "15cm", "2 months")

if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    print(f"Plant: {rose.name}")
    print(f"Height: {rose.height}")
    print(f"Age: {rose.age}")
    print("=== End of Program ===")
