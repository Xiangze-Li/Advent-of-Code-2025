import utils


def solve(data: str) -> None:
    grids = data.splitlines()
    I, J = len(grids), len(grids[0])
    adj: dict[tuple[int, int], int] = {}

    for i, j, c in utils.enumerate_grid(grids):
        if c != "@":
            continue
        cc = 0
        for di, dj in utils.DELTA_8:
            ni, nj = i + di, j + dj
            if 0 <= ni < I and 0 <= nj < J and grids[ni][nj] == "@":
                cc += 1
        adj[(i, j)] = cc

    initial_size = len(adj)

    to_remove: set[tuple[int, int]] = {k for k in adj if adj[k] < 4}
    print(len(to_remove))

    while len(to_remove) > 0:
        next_remove: set[tuple[int, int]] = set()
        for k in to_remove:
            del adj[k]
            i, j = k
            for di, dj in utils.DELTA_8:
                ni, nj = i + di, j + dj
                if (ni, nj) in adj and not (ni, nj) in to_remove:
                    adj[(ni, nj)] -= 1
                    if adj[(ni, nj)] < 4:
                        next_remove.add((ni, nj))
        to_remove = next_remove

    print(initial_size - len(adj))


if __name__ == "__main__":
    import example

    solve(example.get(4))
