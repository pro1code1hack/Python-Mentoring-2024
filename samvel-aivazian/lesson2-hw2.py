# Task 2: Nested loops.

def nested_loops() -> None:
    for i in range(1, 6):
        for _ in range(i):
            print(i, end="")
        print()


nested_loops()
