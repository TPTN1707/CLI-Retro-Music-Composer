# CLI Retro Music Composer

A simple, fun command-line tool written in Python that translates text-based musical notes into retro 8-bit beep sounds.

## Requirements

- Python 3.12+ (managed via `uv` or standard Python)
- Windows OS (uses the built-in `winsound` library)

## How to Run

Clone the repository and run the program:

```bash
uv run main.py
```
*(Or use `python main.py` if you are not using uv)*

## Music Notation Syntax

You can compose your own songs using space-separated tokens in the format `Note:Duration`.

- **Notes:** Supported notes are from `C4` to `E5` (e.g., `C4`, `D4`, `E4`, `F4`, `G4`, `A4`, `B4`, `C5`).
- **Rest (Silence):** Use `R` for a silent pause.
- **Duration:** A multiplier for the base note length (e.g., `:1` for normal, `:2` for double length, `:0.5` for half length).

### Example
`C4:1 D4:1 E4:1 C4:1 E4:1 C4:1 G4:2`