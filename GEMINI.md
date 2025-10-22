# Project: JoyBooking

## Project Overview

This project is a simple web application for booking appointments, named "JoyBooking". It is built as a Minimum Viable Product (MVP).

**Key Technologies:**

*   **Backend:** Python with the Bottle micro-framework.
*   **Database:** SQLite for data storage.
*   **Frontend:** HTML with Bootstrap 5 for styling.

**Architecture:**

The application is a monolithic web application contained in a single Python file, `app.py`. It follows a simple structure:

*   `app.py`: The main application file, containing the web server logic, routes, and database interactions.
*   `bottle.py`: The Bottle framework is included directly in the repository, making the project self-contained.
*   `booking.db`: An SQLite database file that is created automatically to store services and reservations.
*   `prenota.html`: The main HTML template for the booking form.
*   `success.html`: A simple success page shown after a booking is made.
*   `static/`: A directory for static assets, such as the favicon.

## Building and Running

The application can be run directly from the command line.

**To run the application:**

```bash
python app.py
```

This will start a development web server on `http://localhost:8080`.

**Dependencies:**

The project has no external dependencies that need to be installed, as the `bottle.py` framework is included in the repository.

## Development Conventions

*   **Linting:** The project uses [Ruff](https://github.com/astral-sh/ruff) for linting. The configuration is in `ruff.toml`.
*   **Code Style:** The preferred string quote style is single quotes, as defined in `ruff.toml`.
*   **Database:** The application uses a local SQLite database (`booking.db`). The database is initialized with some sample data when the application starts for the first time.
