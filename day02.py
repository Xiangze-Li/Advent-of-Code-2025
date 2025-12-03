import math


def solve(data: str) -> None:
    ranges = [s.split("-", 2) for s in data.split(",")]

    ids_1: set[int] = set()
    ids_2: set[int] = set()
    for r in ranges:
        ids_1_update, ids_2_update = solve_range(int(r[0]), int(r[1]))
        ids_1.update(ids_1_update)
        ids_2.update(ids_2_update)

    print(sum(ids_1))
    print(sum(ids_2))


def solve_range(lb: int, ub: int) -> tuple[set[int], set[int]]:
    digit_min = int(math.log10(lb + 1)) + 1
    digit_max = int(math.log10(ub + 1)) + 1

    ids_1: set[int] = set()
    ids_2: set[int] = set()

    for digit in range(digit_min, digit_max + 1):
        for pattern_len in range(1, (digit // 2) + 1):
            if digit % pattern_len != 0:
                continue
            pattern_count = digit // pattern_len
            pattern_base = 10**pattern_len
            pattern_mul = 0
            for _ in range(pattern_count):
                pattern_mul *= pattern_base
                pattern_mul += 1

            mul_lb = max(math.ceil(lb / pattern_mul), pattern_base // 10)
            mul_ub = min(math.floor(ub / pattern_mul), pattern_base - 1)
            for m in range(mul_lb, mul_ub + 1):
                if lb <= m * pattern_mul <= ub:
                    ids_2.add(m * pattern_mul)
                    if pattern_count == 2:
                        ids_1.add(m * pattern_mul)

    return (ids_1, ids_2)


if __name__ == "__main__":
    import example
    solve(example.get(2))
