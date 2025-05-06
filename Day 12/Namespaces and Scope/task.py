my_global_enemies = 1


def increase_enemies():
    my_global_enemies= 2
    print(f"enemies inside function: { my_global_enemies}")
    print(my_global_enemies)

increase_enemies()
print(f"enemies outside function: {my_global_enemies}")
