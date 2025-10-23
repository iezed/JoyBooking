# Repository Guidelines

## Project Structure & Module Organization
```
├─ app.py                # Bottle web server entry point
├─ database.py           # SQLite helper functions
├─ bottle.py             # Embedded Bottle framework (no external deps)
├─ static/               # CSS, JS, images served as static assets
│   ├─ css/app.css
│   └─ js/bootstrap.bundle.min.js
├─ views/                # Bottle template files (.tpl)
├─ public/               # Legacy static HTML (currently unused)
└─ ruff.toml             # Linting / formatting configuration
```
* **Source code** – `app.py`, `database.py`, and the bundled `bottle.py`.
* **Templates** – stored under `views/` and referenced with `template()`.
* **Static assets** – under `static/`; accessed via the `/static/<filepath>` route.
* **Configuration** – a minimal `ruff.toml` drives code style; no external config files.

## Build, Test, and Development Commands
| Command | Description |
|---------|-------------|
| `python app.py` | Starts the development server on `http://localhost:8080`. The database is created/filled automatically on first run. |
| `ruff check .` | Lints the entire repository using the rules from `ruff.toml`. |
| `ruff format .` | Auto‑formats files (single‑quote strings, trailing‑comma handling, etc.). |
| `pytest` *(optional)* | Run any tests you add under a `tests/` directory. |

## Coding Style & Naming Conventions
* **Indentation** – 4 spaces, no tabs.
* **String quotes** – single quotes as enforced by `ruff` (`quote-style = "single"`).
* **Naming** – `snake_case` for variables/functions, `PascalCase` for classes.
* **Imports** – standard library first, then third‑party, then local modules; each group separated by a blank line.
* **Linting** – run `ruff check .` before committing. Fix issues with `ruff format .`.

## Testing Guidelines
* **Framework** – we recommend `pytest` (or the built‑in `unittest`). Add tests under a top‑level `tests/` folder mirroring the source layout (e.g., `tests/test_database.py`).
* **Naming** – test files must start with `test_` and test functions with the same prefix.
* **Running** – simply execute `pytest` from the repository root. Coverage is optional but encouraged (`pytest --cov`).

## Commit & Pull Request Guidelines
* **Commit messages** – start with a concise imperative title (≤50 characters), followed by an optional blank line and a short body explaining *what* and *why*.
  ```
  Add booking pagination support

  Extend /bookings route to paginate results (10 per page) and update the template.
  ```
* **Atomic commits** – keep each logical change in its own commit.
* **Pull requests** – include a clear description, reference related issue numbers (`Closes #23`), and ensure the branch passes `ruff` checks and any existing tests.
* **Screenshots** – for UI changes, attach a screenshot of the rendered page.

## Additional Recommendations
* **Security** – never expose the raw SQLite file (`booking.db`) in the public repository; it is generated at runtime.
* **Configuration** – future environment‑specific settings should live in a `.env` file and be loaded with `python‑dotenv` (not yet required).
* **Documentation** – keep the `README.md` up‑to‑date with setup steps; add sections here when the project evolves.

