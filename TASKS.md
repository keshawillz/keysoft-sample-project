# Your tasks

This repo is a small (deliberately imperfect) Python order service. Across Week 3
you'll make Claude Code work *with* it — configure it, extend it, and review it.
The same repo carries through all three days.

## The house style (nothing is written down yet — that's the point)

These are the conventions `service.py` already follows. `api.py` has drifted from
them on purpose:

- Use the `logging` logger, never `print()`.
- Public functions have **type hints**.
- On failure, **raise** a domain error or return a structured `{"ok": False, "error": ...}` —
  never a silent empty result.
- Tests live in `tests/`, named `test_*.py`.

## Tuesday — Real-project config  (Domain 3)

1. **Fork** this repo, then open your fork in a Codespace (Claude Code is pre-installed).
2. Run `claude` and ask it to *"add a `handle_refund` function to `api.py`"*. Notice what it
   does with **no** configuration — does it match the house style, or the drift in `api.py`?
3. Write a project **`CLAUDE.md`** capturing the house style above, kept modular with
   `@path` imports if you like. Add a **path-scoped rule** under `.claude/rules/` — e.g. one
   that only loads for `tests/**`.
4. Re-run the same request and watch Claude Code follow your rules. Then ask it to
   **bring `api.py` back in line** with `service.py`.
5. Trap to reproduce: put a team standard in `~/.claude/CLAUDE.md` and confirm a teammate
   (or a fresh Codespace) does **not** get it — then move it to the project `CLAUDE.md`.

## Wednesday — Build a skill  (lab)

Build a **`deps-report`** skill under `.claude/skills/` (with `context: fork`) that lists
the project's dependencies and flags anything outdated. Run it and confirm only the
**summary** returns to your main session, not the verbose output.

## Thursday — Skill + MCP + CI

1. Build a **`review`** skill that checks a diff against `CLAUDE.md`.
2. Finish `.github/workflows/review.yml` so it runs `claude -p` on each PR and posts
   findings (add the `ANTHROPIC_API_KEY` repo secret first).
3. Open a PR that violates the house style (e.g. adds a `print()` to `service.py`) and
   watch the review flag it. Give the skill an MCP server and scope it to just the tools
   its job needs.

## Running the tests

In a Codespace the environment is ready — just:

    pytest

On your own machine, set up a virtual environment first (the `orders` package must be
installed before the tests can import it):

    python -m venv .venv
    source .venv/bin/activate          # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    pytest

Run `pytest`, not `python tests/test_service.py` — the editable install puts the
`orders` package on the path so the imports resolve.
