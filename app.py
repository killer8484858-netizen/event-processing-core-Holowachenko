print("Main branch logging")
print("Logging enabled")
print("Debug mode")


def add(a: int, b: int) -> int:
    if a is None:
        return b
    return a + b
