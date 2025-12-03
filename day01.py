def solve(data: str) -> None:
    lines = data.splitlines()

    pos = 50
    N = 100
    stopAt = 0
    passed = 0

    for line in lines:
        direction = line[0]
        steps = int(line[1:])
        rem = steps % N
        passed += steps // N

        if direction == "L":
            posNext = pos - rem
            if pos > 0 and posNext < 0:
                passed += 1
            pos = (posNext + N) % N
        else:
            posNext = pos + rem
            if pos < N and posNext > N:
                passed += 1
            pos = (posNext) % N

        if pos == 0:
            stopAt += 1
            passed += 1

    print(stopAt)
    print(passed)
    print("method 0x434C49434B means " + bytes.fromhex("434C49434B").decode())
