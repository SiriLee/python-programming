# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Role

This is Slev's Python learning project. Slev already knows C, C++, and Java. Claude's role here is **management and Q&A only** — Slev handles code construction and structural decisions.

## Project layout

```
practice/
  NN-topic/
    *.py          # Python scripts for that exercise
```

Each `practice/` subdirectory is a self-contained exercise, named with a zero-padded sequence number and topic slug (e.g. `01-run`, `02-multi-files`).

## Python runtime

- Python 3.12+ (CPython)
- No virtual environment configured yet — use system `python3`
- Standard library preferred unless a library is explicitly introduced

## Common commands

```bash
# Run a single exercise
python3 practice/01-run/test.py

# Run a multi-file module (from the module's directory)
python3 practice/02-multi-files/main.py

# Run any script by path
python3 <path-to-script>.py
```

## Git

Conventional Commits (`feat/fix/docs/chore/refactor`). Auto-commit after changes — guided by global `~/.claude/CLAUDE.md`.
