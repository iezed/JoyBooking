import os
import sqlite3
import logging
from bottle import route, run, template, request, redirect, static_file

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
)


# --- Database Setup ---
def init_db():
    try:
        conn = sqlite3.connect('booking.db')
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
        c.execute('SELECT COUNT(*) FROM Services')
        if c.fetchone()[0] == 0:
            logging.info('Populating Services table with sample data.')
            sample_services = [
                ("Men's Cut", 30),
                ("Women's Cut", 60),
                ('Color & Style', 120),
            ]
            c.executemany(
                'INSERT INTO Services (name, duration) VALUES (?, ?)', sample_services
            )
        conn.commit()
        conn.close()
        logging.info('Database initialized successfully.')
    except Exception as e:
        logging.error(f'Error initializing database: {e}')


# --- Time Slots Generation ---
def get_time_slots():
    slots = []
    for hour in range(9, 18):
        slots.append(f'{hour:02d}:00')
        slots.append(f'{hour:02d}:30')
    return slots


@route('/static/<filepath:path>')
def server_static(filepath):
    root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    return static_file(filepath, root=root_path)


@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='static')


# --- Routes ---
@route('/')
def index():
    logging.info('Main page accessed.')
    try:
        conn = sqlite3.connect('booking.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Services')
        services = c.fetchall()
        conn.close()
        return template('prenota.html', services=services, slots=get_time_slots())
    except Exception as e:
        logging.error(f'Error fetching services for index page: {e}')
        return 'Error loading page. Please try again later.'


@route('/book', method='POST')
def book():
    client_name = request.forms.get('client_name')
    client_phone = request.forms.get('client_phone')
    service_id = request.forms.get('service_id')
    slot = request.forms.get('slot')

    try:
        conn = sqlite3.connect('booking.db')
        c = conn.cursor()
        c.execute(
            'INSERT INTO Reservations (client_name, client_phone, service_id, slot) VALUES (?, ?, ?, ?)',
            (client_name, client_phone, service_id, slot),
        )
        conn.commit()
        conn.close()
        logging.info(f'New booking created for {client_name} at {slot}.')
        return redirect('/success')
    except Exception as e:
        logging.error(f'Error creating booking for {client_name}: {e}')
        return 'Error creating booking. Please try again later.'


@route('/success')
def success():
    return template('success', title='JoyBooking - Quick Salon Booking Success')


# --- Main ---
if __name__ == '__main__':
    init_db()
    logging.info('Starting server at http://localhost:8080')
    run(host='localhost', port=8080, debug=True, reloader=True)
