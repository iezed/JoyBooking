# Project: JoyBooking

## Project Overview

This project is a simple web application for booking appointments, named "JoyBooking". It is built as a Minimum Viable Product (MVP).

**Key Technologies:**

* **Backend:** Python with the Bottle micro-framework.
* **Database:** SQLite for data storage.
* **Frontend:** HTML with Bootstrap 5 for styling.

**Architecture:**

The application is a monolithic web application. It follows a simple structure:

* `app.py`: The main application file, containing the web server logic, routes, and database interactions. It uses `database.py` to manage the database.
* `database.py`: This file handles all the database operations, including initialization, and CRUD operations for services and bookings.
* `booking.db`: An SQLite database file that is created automatically by `database.py` to store services and reservations.
* `views/`: This directory contains the HTML templates:
  * `base.tpl`: A template used for base for all pages.
  * `booking.tpl`: The main HTML template for the booking form.
  * `success.tpl`: A simple success page shown after a booking is made.
* `static/`: A directory for static assets:
  * `css/`: Contains stylesheets:
    * `app.css`: Custom application styles.
    * `bootstrap.min.css`: Bootstrap 5 framework.
  * `js/`: Contains JavaScript files:
    * `bootstrap.bundle.min.js`: Bootstrap 5 JavaScript bundle.
  * `favicon.ico`: The favicon for the application.

## Building and Running

The application can be run directly from the command line.

**To run the application:**

```bash
python3 app.py
```

This will start a development web server on `http://localhost:8080`.

**Dependencies:**

The project's primary dependency is the Bottle framework.

## Development Conventions

* **Linting:** The project uses [Ruff](https://github.com/astral-sh/ruff) for linting. The configuration is in `ruff.toml`.
* **Code Style:** The preferred string quote style is single quotes, as defined in `ruff.toml`.
* **Database:** The application uses a local SQLite database (`booking.db`). The database is initialized with some sample data when the application starts for the first time.
