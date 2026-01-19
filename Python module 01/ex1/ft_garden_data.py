class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        pass


rose = Plant("Rose:", "15cm", "1 week")
tulip = Plant("Tulip:", "25cm", "1 weeks")
orchid = Plant("Orchid:", "35cm", "3 weeks")

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    print(f"{rose.name} {rose.height}, {rose.age}")
    print(f"{tulip.name} {tulip.height}, {tulip.age}")
    print(f"{orchid.name} {orchid.height}, {orchid.age}")
