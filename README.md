# keysoft-sample-project

A small Python order service used across **Week 3** of the Keysoft CCAR-F cohort to
practice **Claude Code** configuration, skills, and CI review. It's intentionally a
little imperfect — that's what gives your configuration something to enforce.

## Get started (Codespaces)

1. **Fork** this repo (top-right).
2. On your fork: **Code → Codespaces → Create codespace on main**. The devcontainer
   installs Python, creates a virtual environment (`.venv`), installs the project, and
   installs the **Claude Code** CLI (`claude`).
3. Give Claude Code your key: add a Codespaces secret named **`ANTHROPIC_API_KEY`**
   (repo → Settings → Secrets and variables → Codespaces), or run `claude login`.
4. Open a terminal and run `claude` to start Tuesday's tasks (see `TASKS.md`).

## Run the tests

The devcontainer already set up the environment. From the repo root:

```bash
pytest        # -> 3 passing tests
```

**Running it on your own machine** (or if `pytest` isn't found in the Codespace)? Set
up a virtual environment first — the `orders` package has to be installed before the
tests can import it:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt    # installs this project (editable) + pytest
pytest
```

Run **`pytest`**, not `python tests/test_service.py` — the editable install
(`pip install -e .`, via `requirements.txt`) puts the `orders` package on the import
path so `from orders import ...` resolves from anywhere.

## What's here

    src/orders/      the service — service.py is clean; api.py has drifted on purpose
    tests/           pytest tests
    TASKS.md         your Tuesday / Wednesday / Thursday tasks
    .devcontainer/   Codespaces setup (venv + Claude Code pre-installed)
    .github/         a seed CI workflow you finish on Thursday
    pyproject.toml   packaging + pytest config
