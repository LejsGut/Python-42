def ft_count_harvest_recursive(current=1, days=None):
    if (days is None):
        days = int(input("Days until harvest: "))
    print(f"Day {current}")
    if (current >= days):
        print("Harvest time!")
        return
    ft_count_harvest_recursive(current + 1, days)
    pass
