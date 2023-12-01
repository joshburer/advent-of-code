from typing import List, Set
import types
from dataclasses import dataclass, field
from collections import deque


LOGS = False
EXAMPLE = False
INPUT = "example.txt" if EXAMPLE else "input.txt"


chars = types.SimpleNamespace()
chars.GROUND = "."
chars.WALL = "#"
chars.BLIZ_RIGHT = ">"
chars.BLIZ_LEFT = "<"
chars.BLIZ_UP = "^"
chars.BLIZ_DOWN = "v"

CHAR_TO_DELTA_TABLE = {
    chars.BLIZ_RIGHT: (0, 1),
    chars.BLIZ_LEFT: (0, -1),
    chars.BLIZ_UP: (-1, 0),
    chars.BLIZ_DOWN: (1, 0),
}


grid: List[List[str]] = [[]]
with open(INPUT) as f:
    grid = [list(l.strip()) for l in f.readlines()]


h = len(grid)
w = len(grid[0])


@dataclass
class GameState:
    blizzards: list = field(default_factory=lambda: [])
    blizz_cache: dict = field(default_factory=lambda: {})
    starting_point: tuple = (0, 0)
    player_point: tuple = (0, 0)
    ending_point: tuple = (0, 0)
    target_point: tuple = (0, 0)
    visited: Set = field(default_factory=lambda: set())
    switchbacks: int = 0


state = GameState()


def log(*msg):
    if LOGS:
        print(*msg)


# Locale ye olde walls, blizzardos, and start/finish points
for row in range(h):
    for col in range(w):
        current = grid[row][col]
        match current:
            case chars.WALL:
                continue
            case chars.GROUND:
                if row == 0:
                    state.starting_point = state.player_point = (row, col)

                if row == h - 1:
                    state.target_point = state.ending_point = (row, col)
            case other:
                state.blizzards.append([row, col, CHAR_TO_DELTA_TABLE[other]])


# Tick ye olde blizzard state, memoed by minute (step) since start
def update(blizzards, minute):
    if minute not in state.blizz_cache:

        log("cache miss:", minute)

        dupe = [[*b] for b in blizzards]

        for blizz in dupe:
            _, _, delta = blizz
            blizz[0] += delta[0]
            blizz[0] = ((blizz[0] - 1) % (h - 2)) + 1
            blizz[1] += delta[1]
            blizz[1] = ((blizz[1] - 1) % (w - 2)) + 1

        lookup_table = set((r, c) for r, c, _ in dupe)
        state.blizz_cache[minute] = [dupe, lookup_table]

    return state.blizz_cache[minute]


# Determine thine fate.
def get_moves(player_position, grid, blizz, minute):
    pr, pc = player_position

    # Get "next step" blizzard state to try and trim down our viable moves.
    # If you end up in a blizzardo, to you be woe!
    _, lut = update(blizz, minute)

    viable = []
    for move in [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (0, 0),
    ]:
        dr, dc = move
        nr = pr + dr
        nc = pc + dc

        # Basic bounds checking
        if nr < 0 or nr >= h or nc < 1 or nc >= w - 1:
            continue

        if grid[nr][nc] == chars.WALL:
            continue

        if (nr, nc) in lut:
            continue

        if ((nr, nc), minute + 1) in state.visited:
            continue

        viable.append(move)

    return viable


# Conjurest thou a clairvoyant solution,
# Answers you seek will blonko-bol-glution
def solve():

    best = float("inf")

    moves_queue = deque(
        [
            (state.starting_point, move, state.blizzards, 0)
            for move in get_moves(state.starting_point, grid, state.blizzards, 0)
        ]
    )

    while len(moves_queue):
        old_pp, move, blizz, steps = moves_queue.popleft()
        new_pp = old_pp[0] + move[0], old_pp[1] + move[1]

        if (new_pp, steps) in state.visited:
            continue
        state.visited.add((new_pp, steps))

        if new_pp == state.target_point:
            if state.switchbacks == 0:
                log("running back to start", new_pp, state.target_point)
                state.target_point = state.starting_point
                moves_queue = deque([])

            if state.switchbacks == 1:
                log("running back to end", new_pp, state.target_point)
                state.target_point = state.ending_point
                moves_queue = deque([])

            if state.switchbacks == 2:
                return steps + 1

            state.switchbacks += 1

        next_blizz, lut = update(blizz, steps)

        if new_pp in lut:
            raise "Shouldn't happen!"

        new_moves = [
            (new_pp, move, next_blizz, steps + 1)
            for move in get_moves(new_pp, grid, next_blizz, steps + 1)
        ]

        moves_queue.extend(new_moves)

    return best


solution = solve()
print("Done!")
print(solution)
