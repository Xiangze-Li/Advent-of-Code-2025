def get(day: int) -> str:
    with open(f"input/{day:02}.txt") as f:
        return f.read()
