class Plant:
    def __init__(self, name, height, age, grow, grow_day):
        self.name = name
        self.height = height
        self.age = age
        self.grow = grow
        self.grow_day = grow_day

    def growing(self):
        self.height += self.grow
    
    def aging(self):
        self.age += 1

    def info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

rose = Plant("Rose", 25, 30, 2, 7)
day_count = 1
while(day_count <= rose.grow_day):
    if(day_count == 1 or day_count == rose.grow_day):
        print(f"=== Day {day_count} ===")
        rose.info()
        if(day_count == rose.grow_day):
            print(f"Growth this week: +{rose.grow * rose.grow_day - rose.grow}cm")
    rose.growing()
    rose.aging()
    day_count += 1