# Recursion

A tiny **Python 3** playground that explores classic recursive back‑tracking by generating every possible game continuation for simplified **Othello/Reversi** boards.

---

## About

This repository began life as a university assignment on recursion techniques. It now stands as a **minimal, dependency‑free** showcase of how to:

1. Parse a text‑file representation of an Othello board.
2. Recursively build the full game tree from the current position.
3. Count end‑states where **Black wins**, **White wins**, or **the game is a draw**.

All of the heavy‑lifting lives in `program01.py` (≈ 140 LOC). Board snapshots of increasing size/complexity live under `boards/` to help you benchmark how the recursion scales. ([github.com](https://github.com/bgkcsav4/Recursion/commit/4aad3a85229b30436e10e6b6615bd270558596a3))


## How It Works

### Board Format

Each board file is a plain‑text grid where:

* `B` = Black disc
* `W` = White disc
* `.` = Empty square

Cells are space‑separated for readability; row length determines the board width.

### Key Functions

| Function                                 | Purpose                                                                                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `file_info(path)`                        | Reads a board file and converts it into a 2‑D list plus `(width, height)` tuple.                                                      |
| `generate_possible_moves(board, player)` | Returns a list of empty squares that legally neighbour an opponent disc.                                                              |
| `make_move()` / `capture_in_direction()` | Place a disc **and** flip any encircled opponent discs in 8 directions.                                                               |
| `generate_game_tree()`                   | Depth‑first recursion that tries every valid move, swapping players until no further moves exist; leaves are appended to `game_tree`. |
| `dumbothello(path)`                      | Convenience wrapper that loads a board, builds the tree (Black to move), and tallies **Black wins / White wins / Draws**.             |

The recursion terminates when `generate_possible_moves()` returns an empty list, i.e. the current player has no legal move—this is treated as a leaf node. 


## License

This project is released under the MIT License—see `LICENSE` for details.
