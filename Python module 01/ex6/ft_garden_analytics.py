class Gardenmanager:
    def __init__(self, gardener):
        self.gardener = gardener


class Node:
    def __init__(self, gardener, name, manager, bloom, prize):
        self.gardener = gardener
        self.name = name
        self.manager = manager
        self.bloom = False
        self.prize = prize
        self.next = None


class Alice:
    def __init__(self):
        pass


class Bob:
    def __init__(self):
        pass


class Plant:
    def __init__(self, name, height, age):
        super().__init__()


class FloweringPlant(Plant):
    def __init__(self):
        super().__init__()


class PrizeFlower(FloweringPlant):
    def __init__(self):
        super().__init__()
