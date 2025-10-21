import sqlite3
from bottle import route, run, template, request, redirect


# --- Database Setup ---
def init_db():
    conn = sqlite3.connect("booking.db")
    c = conn.cursor()
    # Create Services table
    c.execute("""
        CREATE TABLE IF NOT EXISTS Services (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            duration INTEGER NOT NULL
        )
    """)
    # Create Reservations table
    c.execute("""
        CREATE TABLE IF NOT EXISTS Reservations (
            id INTEGER PRIMARY KEY,
            client_name TEXT NOT NULL,
            client_phone TEXT NOT NULL,
            service_id INTEGER NOT NULL,
            slot TEXT NOT NULL,
            FOREIGN KEY (service_id) REFERENCES Services(id)
        )
    """)
    # Populate Services if empty
    c.execute("SELECT COUNT(*) FROM Services")
    if c.fetchone()[0] == 0:
        sample_services = [
            ("Men's Cut", 30),
            ("Women's Cut", 60),
            ("Color & Style", 120),
        ]
        c.executemany(
            "INSERT INTO Services (name, duration) VALUES (?, ?)", sample_services
        )
    conn.commit()
    conn.close()


# --- Time Slots Generation ---
def get_time_slots():
    slots = []
    for hour in range(9, 18):
        slots.append(f"{hour:02d}:00")
        slots.append(f"{hour:02d}:30")
    return slots


# --- Routes ---
@route("/")
def index():
    conn = sqlite3.connect("booking.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Services")
    services = c.fetchall()
    conn.close()
    return template("prenota.html", services=services, slots=get_time_slots())


@route("/book", method="POST")
def book():
    client_name = request.forms.get("client_name")
    client_phone = request.forms.get("client_phone")
    service_id = request.forms.get("service_id")
    slot = request.forms.get("slot")

    conn = sqlite3.connect("booking.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO Reservations (client_name, client_phone, service_id, slot) VALUES (?, ?, ?, ?)",
        (client_name, client_phone, service_id, slot),
    )
    conn.commit()
    conn.close()

    return redirect("/success")


@route("/success")
def success():
    return template("success.html")


# --- Main ---
init_db()

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
