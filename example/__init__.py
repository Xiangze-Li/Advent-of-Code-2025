def get(day: int) -> str:
    with open(f"example/{day:02}.txt") as f:
        return f.read()
